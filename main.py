import os
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = os.getenv("GEMINI_API_KEY")
print(api_key)

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-pro",
    api_key = api_key
)
