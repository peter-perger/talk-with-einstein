from functions.handle_input import handle_input
import streamlit as st


st.title("Talk with Einstein!")
st.write("Welcome to a digital bridge across time. This platform isn't just a chat interface; it is a specialized gateway designed to let you engage with the mind of Albert Einstein through the power of modern Generative AI.")

st.text_input(label="📜🧝", key="user_input", on_change=handle_input)

st.text_area(
    label="Einstein answer",
    key="einstein_answer",
    height=200
)

st.write("Powered by <strong>Perger Peter</strong>", unsafe_allow_html=True)
