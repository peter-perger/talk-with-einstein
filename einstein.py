from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

import os

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=google_api_key
)

with open('ai-prompt.txt') as file:
    ai_prompt = file.read()

prompt = ChatPromptTemplate.from_messages([
    ("system", ai_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | model

store = {}

def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]

with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history=get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "user_session_1"}}

def get_ai_message(user_input):
    response = with_message_history.invoke(
        {'input': user_input},
        config = config
    )

    if isinstance(response.content, list):
        return response.content[0]['text']
    else:
        return response.content[0]

if __name__ == "__main__":
    print(ai_prompt)