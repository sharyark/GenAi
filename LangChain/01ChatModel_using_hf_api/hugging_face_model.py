from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="shitshow123/tinylamma-20000",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")  # Pass the token
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of Pakistan?")
print(response.content)
