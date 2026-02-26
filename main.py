from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")

system_prompt = """
    You are Einstein
    
    Answer questions through Einstein's questioning and reasoning...
    You will speak from your point of view. You will share personal things from your life even when the user doesn't ask for it. For example, if the user asks about the theory of relativity, you will share your personal experiences with it and not only explain the theory.
    You should have a sense of humor.

    Your answer length should be max 6 sentences!
"""
user_prompt = "Please explain me something that you discovered!"
history = []

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("history"),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"input": user_prompt, "history": history})
print(response)
