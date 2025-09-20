import streamlit as st, uuid, datetime
from utils.db import get_conn
from utils.rag_chain import get_qa_chain
from utils.build_index import build_or_refresh

st.set_page_config(page_title="Chatbot interno", page_icon="🤖")

# 1) generar índice si no existe
with st.spinner("Indexando documentos (solo la primera vez)…"):
    if not build_or_refresh():
        st.warning("No se encontraron PDF/txt en la carpeta data/.")
    qa_chain = get_qa_chain()

# 2) manejo de sesión
if "session" not in st.session_state:
    st.session_state.session = str(uuid.uuid4())

conn = get_conn()

st.title("Chatbot interno (sin costo)")
question = st.chat_input("Escribe tu pregunta…")
if question:
    with st.spinner("Pensando…"):
        answer = qa_chain.run(question).strip()
    st.chat_message("user").write(question)
    st.chat_message("assistant").write(answer)

    conn.execute(
        "INSERT INTO log (session, ts, question, answer) VALUES (?, ?, ?, ?)",
        (st.session_state.session,
         datetime.datetime.utcnow().isoformat(),
         question, answer)
    )
    conn.commit()

# 3) historial de la sesión
with st.expander("Ver historial de esta sesión"):
    rows = conn.execute(
        "SELECT ts, question, answer FROM log WHERE session=? ORDER BY ts",
        (st.session_state.session,)
    ).fetchall()
    for ts, q, a in rows:
        st.write(f"**{q}** → {a}")
conn.close()
