from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
import os, glob

this_file_dir = os.path.dirname(__file__)
DATA_DIR = os.path.join(this_file_dir, "..", "data")
PERSIST = os.path.join(this_file_dir, "..", "vectorstore")

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

    emb = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    vectorstore = FAISS.from_documents(chunks, emb)
    vectorstore.save_local(PERSIST)
    return True
