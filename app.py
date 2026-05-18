import streamlit as st

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot Portfolio Project")

if "chat" not in st.session_state:
    st.session_state.chat = []

def respond(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hi! 👋 I am your AI chatbot."
    elif "name" in message:
        return "I am a portfolio AI assistant 🤖"
    elif "python" in message:
        return "Python is a powerful programming language 🐍"
    elif "job" in message:
        return "Keep building projects for your portfolio 💼"
    elif "help" in message:
        return "I can answer basic questions and chat with you 😄"
    else:
        return "I am a simple AI demo chatbot 🤖"

user_input = st.text_input("Type your message:")

if user_input:
    reply = respond(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", reply))

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.write(f"🧑 {msg}")
    else:
        st.write(f"🤖 {msg}")