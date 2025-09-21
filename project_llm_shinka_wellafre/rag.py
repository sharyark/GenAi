
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
x = load_dotenv()
print(x)
def load_text_file(file_path):
    """
    Load the contents of a text file as a single string.
    Useful for ingesting into a RAG pipeline.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
    
def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

# Example usage
if __name__ == "__main__":
    file_path = "data_output/output.txt"
    document_text = load_text_file(file_path)
    # print(document_text[:1000])  # Print the first 1000 characters for preview
    spilter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    chunks = spilter.create_documents([document_text])
    # print(chunks[0].page_content[:1000])  # Print the first 1000 characters of the first chunk
    print(len(chunks))

    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vector_store = FAISS.from_documents(chunks,embeddings)

    retriever = vector_store.as_retriever(search_type='similarity',search_kwargs={'k':1})

    # print(retriever.invoke('molana rasheed'))

    google_api_key = os.getenv("GOOGLE_API_KEY")
    llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key)

    prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer  from the provided transcript context add by your self for clarify.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question'])

    # question          = "why should i turn off lights"
    # retrieved_docs    = retriever.invoke(question)

    # context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    # print(context_text)

    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })

    # print(parallel_chain.invoke('molana rasheed')['question'])

    parser = StrOutputParser()

    main_chain = parallel_chain | prompt | llm | parser
    x = input("Enter your question: ")
    print(main_chain.invoke(x))