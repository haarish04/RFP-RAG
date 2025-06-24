from dotenv import load_dotenv
import os

load_dotenv()

TOGETHER_API_KEY=os.getenv("TOGETHER_API_KEY")
CHROMA_DB_PATH=os.getenv("CHROMA_DB_PATH")
EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL")
LLM_MODEL=os.getenv("LLM_MODEL")
CHROMA_DB_HOST=os.getenv("CHROMA_DB_HOST")
CHROMA_DB_PORT=int(os.getenv("CHROMA_DB_PORT"))
CHROMA_TENANT=os.getenv("CHROMA_TENANT")
CHROMA_DATABASE=os.getenv("CHROMA_DATABASE")