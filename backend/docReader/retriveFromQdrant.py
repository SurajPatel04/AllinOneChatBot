from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key= os.getenv("GOOGLE_API_KEY")
)

retriver = QdrantVectorStore.from_existing_collection(
    collection_name="fast_API",
    embedding=embeddings,
    url="https://22e344fe-63fd-43c9-aab0-3c13092b7e38.eu-west-2-0.aws.cloud.qdrant.io:6333",
    api_key=os.getenv("QDRANT_API_KEY"),
    # url="http://localhost:6333"
)

relevant_chunk = retriver.similarity_search(
    query="what is env",
    k=10
)

print(relevant_chunk)