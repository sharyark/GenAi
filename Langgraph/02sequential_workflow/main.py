from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Fetch the API key from environment
groq_api_key = os.getenv("GROQ_API")

# print("GROQ API Key:", groq_api_key)

llm = ChatGroq(
    api_key=groq_api_key,
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)
print(llm.invoke("hello "))