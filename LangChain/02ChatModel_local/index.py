from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Initialize the HuggingFace pipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v0.6",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.5,
                     "max_new_tokens": 100}
)

# Create a ChatHuggingFace instance
chat_model = ChatHuggingFace(pipeline=llm)

# Example usage
response = chat_model.invoke("what is capital of pakistan")
print(response)
