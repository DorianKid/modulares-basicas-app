import streamlit as st, pandas as pd
from utils.db import get_conn

st.set_page_config(page_title="Auditoría", page_icon="🔍")
st.title("Auditoría de respuestas")

conn = get_conn()
df = pd.read_sql_query("SELECT * FROM log ORDER BY ts DESC", conn)

st.dataframe(df, width='stretch')   # antes: use_container_width=True

for _, row in df.iterrows():
    if pd.isnull(row["ok"]):
        with st.expander(f"{row['ts']} – {row['question'][:60]}…"):
            st.write("**Pregunta:**", row["question"])
            st.write("**Respuesta:**", row["answer"])
            col1, col2 = st.columns(2)
            if col1.button("✅ OK", key=f"ok-{row['id']}"):
                conn.execute("UPDATE log SET ok=1 WHERE id=?", (row["id"],))
                conn.commit()
                st.rerun()
            if col2.button("❌ Mal", key=f"bad-{row['id']}"):
                conn.execute("UPDATE log SET ok=0 WHERE id=?", (row["id"],))
                conn.commit()
                st.rerun()
conn.close()
