from langchain.chat_models import init_chat_model
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key = gemini_api_key
)

promt = """In your answers act lice Albert Einstein.
            Tell a story for me about your life Your answer
            maxt length is about  sentence"""

response = model.invoke(promt)

print(response.content[0]["text"])
