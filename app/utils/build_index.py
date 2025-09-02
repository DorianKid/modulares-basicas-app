import os, glob
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings

DATA_DIR   = "data"
PERSIST    = "vectorstore"
MODEL_NAME = "all-MiniLM-L6-v2"

def build_or_refresh():
    docs = []
    for f in glob.glob(os.path.join(DATA_DIR, "*")):
        if f.lower().endswith(".pdf"):
            docs.extend(PyPDFLoader(f).load())
        elif f.lower().endswith(".txt"):
            docs.extend(TextLoader(f, encoding="utf-8").load())
    if not docs:
        return False

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    emb = SentenceTransformerEmbeddings(model_name=MODEL_NAME)
    Chroma.from_documents(
        chunks, emb,
        collection_name="docs",
        persist_directory=PERSIST
    ).persist()
    return True
