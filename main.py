from einstein import get_ai_message
import streamlit as st

st.set_page_config(page_title="Talk with Einstein", page_icon="🧠")

st.title("Talk With Einstein")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        assistant_message = get_ai_message(prompt)
        st.markdown(assistant_message)

    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
