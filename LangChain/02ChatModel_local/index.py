from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v0.6"

# Load model with auto precision and device mapping
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", device_map="auto")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Create a text-generation pipeline (REMOVE device argument)
text_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype="auto",  # Auto precision
)

# Example usage
response = text_pipeline("What is the capital of Pakistan?", max_new_tokens=50)
print(response)




# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# # Initialize the HuggingFace pipeline
# llm = HuggingFacePipeline.from_model_id(
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v0.6",
#     task="text-generation",
#     pipeline_kwargs={"temperature": 0.5,
#                      "max_new_tokens": 100}
# )

# # Create a ChatHuggingFace instance
# chat_model = ChatHuggingFace(pipeline=llm)

# # Example usage
# response = chat_model.invoke("what is capital of pakistan")
# print(response)
