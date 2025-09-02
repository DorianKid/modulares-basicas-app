from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.chains import RetrievalQA
from langchain_community.prompts import PromptTemplate
from transformers import pipeline

PERSIST = "vectorstore"

# 1) retriever local
def get_retriever():
    emb = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=PERSIST,
                collection_name="docs",
                embedding_function=emb)
    return db.as_retriever(search_kwargs={"k": 4})

# 2) LLM pequeño local (CPU)
qa_pipe = pipeline("text2text-generation",
                   model="google/flan-t5-small",
                   max_new_tokens=256)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "Responde SOLO con base en el siguiente texto. "
        "Si la información no está, di: 'No tengo información sobre eso'.\n\n"
        "Texto:\n{context}\n\nPregunta: {question}\nRespuesta:"
    )
)

def get_qa_chain():
    from langchain_community.llms import HuggingFacePipeline
    llm = HuggingFacePipeline(pipeline=qa_pipe)
    retriever = get_retriever()
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )
