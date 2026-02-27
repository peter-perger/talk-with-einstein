from models.einsteinAI import get_answer
import streamlit as st


def handle_input():
    question = st.session_state["user_input"]

    answer = get_answer(question)

    st.session_state["einstein_answer"] = answer
    st.session_state["user_input"] = ""
