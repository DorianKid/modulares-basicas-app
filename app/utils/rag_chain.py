from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

PERSIST = "vectorstore"   # carpeta donde se guarda el índice FAISS

# 1) retriever local con FAISS
def get_retriever():
    emb = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    db = FAISS.load_local(
        PERSIST,
        emb,
        allow_dangerous_deserialization=True  # necesario para FAISS local
    )
    return db.as_retriever(search_kwargs={"k": 4})

# 2) pipeline local
qa_pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    max_new_tokens=256,
    device=-1  # CPU
)

def get_qa_chain():
    llm = HuggingFacePipeline(pipeline=qa_pipe)
    retriever = get_retriever()
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "Responde SOLO con base en el siguiente texto. "
            "Si la información no está, di: 'No tengo información sobre eso'.\n\n"
            "Texto:\n{context}\n\nPregunta: {question}\nRespuesta:"
        )
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )
