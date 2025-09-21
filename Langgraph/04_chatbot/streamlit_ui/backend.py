from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API")

llm = ChatGroq(
    api_key=groq_api_key,
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    # assume state['messages'] already has history if any
    messages = state.get('messages', [])
    response: AIMessage = llm.invoke(messages)
    # return only new message; use add_messages to append
    return {'messages': [response]}

# build graph
builder = StateGraph(ChatState)
builder.add_node('chat_node', chat_node)
# add edges
builder.add_edge(START, 'chat_node')
builder.add_edge('chat_node', END)

# use MemorySaver checkpointer
memory = MemorySaver()
chatbot = builder.compile(checkpointer=memory)

# when invoking
initial_state = {
    'messages': [HumanMessage(content='What is the capital of India')]
}

config = {"configurable": {"thread_id": "thread1"}}
output = chatbot.invoke(initial_state, config=config)
print(output['messages'][-1].content)

# second invocation using same thread_id will load the past messages automatically
