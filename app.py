import streamlit as st

st.title("🤖 Free AI Chatbot (Portfolio)")

if "chat" not in st.session_state:
    st.session_state.chat = []

def respond(msg):
    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Hi 👋"
    elif "name" in msg:
        return "I am a free portfolio bot 🤖"
    elif "python" in msg:
        return "Python is great 🐍"
    elif "job" in msg:
        return "Keep building your portfolio 💼"
    else:
        return "I am a simple demo bot 🤖"

user = st.text_input("Type message:")

if user:
    bot = respond(user)

    st.session_state.chat.append(("You", user))
    st.session_state.chat.append(("Bot", bot))

for s, m in st.session_state.chat:
    st.write(f"**{s}:** {m}")
