import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

# API client (key ide zo Streamlit Secrets)
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# input
user_input = st.text_input("Napíš správu:")

# AI response
def get_response(message):
    completion = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct:free",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return completion.choices[0].message.content

# logic
if user_input:
    st.session_state.chat.append(("You", user_input))

    try:
        bot_response = get_response(user_input)
    except Exception as e:
        bot_response = f"Error: {str(e)}"

    st.session_state.chat.append(("Bot", bot_response))

# render chat
for role, msg in st.session_state.chat:
    if role == "You":
        st.markdown(f"**🧑 Ty:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
