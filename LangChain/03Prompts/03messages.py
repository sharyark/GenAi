from langchain_core.messages import SystemMessage, AIMessage,HumanMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize the LLM model with parameters
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

messages = [
    SystemMessage(content='you are a helpful bot'),
    HumanMessage(content='my name is sharyar'),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)