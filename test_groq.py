# test_groq.py
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))
response = llm.invoke("Test message: Hello, Groq!")
print(response.content)