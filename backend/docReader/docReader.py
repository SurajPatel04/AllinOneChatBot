from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
load_dotenv()


def docReader(fileNane, collection_name):
    pdf_path = Path(__file__).parent/ "../temp/fileName"

    loader = PyPDFLoader(file_path=pdf_path)
    doc = loader.load()

    text_spliter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )

    split_doc = text_spliter.split_documents(documents=doc)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key= os.getenv("GOOGLE_API_KEY")
    )

    qdrant = QdrantVectorStore.from_documents(
        documents=[],
        # url="https://22e344fe-63fd-43c9-aab0-3c13092b7e38.eu-west-2-0.aws.cloud.qdrant.io:6333",
        # url="http://localhost:6333",
        embedding=embeddings,
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name=collection_name
    )

    
    qdrant.add_documents(documents=split_doc)
    print("✅ Docs stored in Qdrant via LangChain!")
    # print(split_doc)
    # print(doc)