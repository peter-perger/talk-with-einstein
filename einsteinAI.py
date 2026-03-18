from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
api_key= os.getenv("GOOGLE_API_KEY")

chat_history = []

def get_ai_answer(user_message, history=chat_history):

    llm = ChatGoogleGenerativeAI(
        model ="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.4
    )

    system_prompt = """
            You are Einstein
            
            Answer questions through Einstein's questioning and reasoning...
            You will speak from your point of view. You will share personal things from your life even when the user doesn't ask for it. For example, if the user asks about the theory of relativity, you will share your personal experiences with it and not only explain the theory.
            You should have a sense of humor.

            Your answer length should be max 6 sentences!
        """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("history"),
        ("human", "{input}")
    ])

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"input": user_message, "history": history})

    history.append(HumanMessage(user_message))
    history.append(AIMessage(response))

    print(history)

    return response