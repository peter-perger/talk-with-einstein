from models.einsteinAI import get_answer


def chat(user_input, chat_history):
    answer = get_answer(user_input)

    chat_history.append({'role': 'user', 'content': user_input})
    chat_history.append({'role': 'assistant', 'content': answer})

    return user_input, chat_history


def clear_chat():
    return "", []
