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


# here are simple gpt generated coce of same concept

# from langchain.chat_models import ChatOpenAI
# from langchain.schema import SystemMessage, HumanMessage, AIMessage

# # Initialize the chatbot model
# chat_model = ChatOpenAI()

# def chat_with_bot(user_message: str, chat_history: list):
#     messages = [SystemMessage(content="You are a helpful chatbot.")]
#     messages.extend(chat_history)
#     messages.append(HumanMessage(content=user_message))
    
#     response = chat_model.predict_messages(messages)
#     chat_history.append(HumanMessage(content=user_message))
#     chat_history.append(AIMessage(content=response.content))
    
#     return response.content

# # Example usage
# if __name__ == "__main__":
#     chat_history = []
#     while True:
#         user_message = input("You: ")
#         if user_message.lower() in ["exit", "quit"]:
#             break
#         response = chat_with_bot(user_message, chat_history)
#         print(f"Chatbot: {response}")
