import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

VECTOR_DB_PATH = "data/embeddings_faiss"

def build_vector_db(text):
    embeddings = AzureOpenAIEmbeddings(
        deployment=os.getenv("AOAI_DEPLOY_EMBED_3_LARGE"),
        api_key=os.getenv("AOAI_API_KEY"),
        azure_endpoint=os.getenv("AOAI_ENDPOINT"),
        api_version=os.getenv("AOAI_API_VERSION")
    )

    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=300,
        chunk_overlap=100,
        length_function=len
    )
    docs = text_splitter.split_text(text)

    vectordb = FAISS.from_texts(docs, embeddings)
    vectordb.save_local(VECTOR_DB_PATH)
    return vectordb

def load_vector_db():
    embeddings = AzureOpenAIEmbeddings(
        deployment=os.getenv("AOAI_DEPLOY_EMBED_3_LARGE"),
        api_key=os.getenv("AOAI_API_KEY"),
        azure_endpoint=os.getenv("AOAI_ENDPOINT"),
        api_version=os.getenv("AOAI_API_VERSION")
    )

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
