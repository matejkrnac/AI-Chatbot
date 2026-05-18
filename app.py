import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="ChatGPT Clone", page_icon="💬", layout="centered")

st.title("💬 ChatGPT Clone")

# OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# model (JEDEN stabilný – žiadne free tagy)
MODEL = "mistralai/mistral-7b-instruct"

# render chat UI
def render_chat():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div style="text-align:right; margin:10px;">
                    <div style="
                        background:#2b7cff;
                        color:white;
                        padding:10px 14px;
                        border-radius:18px;
                        display:inline-block;
                        max-width:80%;
                    ">
                        {msg["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="text-align:left; margin:10px;">
                    <div style="
                        background:#2a2a2a;
                        color:white;
                        padding:10px 14px;
                        border-radius:18px;
                        display:inline-block;
                        max-width:80%;
                    ">
                        {msg["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# streaming answer
def stream_response(messages):
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True
    )

    full = ""
    placeholder = st.empty()

    for chunk in stream:
        if chunk.choices[0].delta.content:
            full += chunk.choices[0].delta.content
            placeholder.markdown(
                f"""
                <div style="text-align:left; margin:10px;">
                    <div style="
                        background:#2a2a2a;
                        color:white;
                        padding:10px 14px;
                        border-radius:18px;
                        display:inline-block;
                        max-width:80%;
                    ">
                        {full}▌
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    return full

# input
user_input = st.chat_input("Napíš správu...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    api_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    response = stream_response(api_messages)

    st.session_state.messages.append({"role": "assistant", "content": response})

# render
render_chat()
