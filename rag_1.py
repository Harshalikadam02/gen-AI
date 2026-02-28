from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

pdf_path = Path(__file__).parent /  "AIclasses.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

split_docs = text_splitter.split_documents(documents=docs)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key="OPENAI_API_KEY"

)
vector_store = QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333",
    embeddings=embeddings,
    collection_name="learning_langchain",

)

vector_store.add_documents(documents=split_docs)
print("Injection completed successfully!")

retriever = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    embeddings=embeddings,
    collection_name="learning_langchain",

)

relevant_chunks = retriever.similarity_search(
    query="What is Robotics?")

SYSTEM_PROMPT = """You are a helpful AI assistant who responds based on the available context. Use the following retrieved chunks to answer the question. If you don't know the answer, say you don't know.
{context}
{relevant_chunks}
"""