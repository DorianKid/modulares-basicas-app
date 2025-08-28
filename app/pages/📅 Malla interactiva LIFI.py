import json
import streamlit as st
import streamlit.components.v1 as components
import importlib, files.html_grid as html_grid
from files.html_grid import (HTML_LIFI_N, HTML_LIFI_M, HTML_LIFI_R, HTML_LIFI_P)
from LIFI.courses_data_lifi import mod_lifi_courses

# Configuracion para el tabs
# 👇 Inyecta estilos ANTES de crear los tabs
st.markdown("""
<style>
/* Usa el MISMO gris que ya defines en tu hoja (— si ya existe, no dupliques) */
:root{ --bg:#eef2f7; }

/* Fondo global */
html, body{ background: var(--bg) !important; }

/* Envoltorios de Streamlit */
.stApp,
[data-testid="stAppViewContainer"],
header[data-testid="stHeader"],
[data-testid="stSidebar"], .stSidebar,
section.main, .block-container{
  background: var(--bg) !important;
}

/* Tabs bar */
.stTabs [data-baseweb="tab-list"]{
  background: var(--bg) !important;
  border-bottom: 1px solid rgba(0,0,0,.06);
}

/* Que la malla no meta un fondo distinto */
.plan{ background: transparent !important; box-shadow:none; }

/* Espaciado entre pestañas */
.stTabs [role="tablist"] {
  gap: 20px !important;
}

/* Botones de pestaña (base) */
.stTabs [role="tab"] {
  padding: 10px 20px !important;
  border-radius: 8px 8px 0 0 !important;
  background: transparent !important;
  color: #334155 !important;
}

/* Texto de la pestaña: captura p/span/div según la versión de Streamlit */
.stTabs [role="tab"] * {
  font-size: 1.5rem !important;  /* 👈 tamaño */
  font-weight: 800 !important;    /* 👈 negritas */
  line-height: 1.2 !important;
}

/* Pestaña activa */
.stTabs [role="tab"][aria-selected="true"] {
  color: #0f172a !important;
}

</style>
""", unsafe_allow_html=True)

# ---- Helpers ----
def is_real_course(c: dict) -> bool:
    """True si cuenta para métricas (descarta spacers u otros 'kind')."""
    return c.get("kind") != "spacer"

def num(x, default=0):
    """Convierte a número seguro (evita None/strings); usa default si falla."""
    try:
        return float(x)
    except Exception:
        return default

# ---- Calcular métricas (ignora spacers) ----
def calc_stats(approved_ids: set[str]):
    real_courses = [c for c in mod_lifi_courses if is_real_course(c)]
    real_ids     = {c["id"] for c in real_courses}

    # Solo consideramos aprobadas las que existen y son reales
    approved_real = real_ids.intersection(approved_ids)

    total_courses   = len(real_courses)
    approved_courses= len(approved_real)

    total_credits   = sum(num(c.get("credits", 0)) for c in real_courses)
    approved_credits= sum(num(c.get("credits", 0)) for c in real_courses
                          if c["id"] in approved_real)

    pct_courses = (approved_courses / total_courses * 100) if total_courses else 0
    pct_credits = (approved_credits / total_credits * 100) if total_credits else 0

    return approved_courses, total_courses, pct_courses, approved_credits, total_credits, pct_credits

# Configurar página 
st.set_page_config(page_title="Malla Curricular LIFI", page_icon="🎓", layout="wide")

tab1, tab2, tab3, tab4 = st.tabs([" Normal", " Real", " Recomendado", " Personalizado"])
altura = 1270
html_grid = importlib.reload(html_grid)

with tab1:
    # Embeber HTML
    components.html(html_grid.HTML_LIFI_N, height=altura, scrolling=True)
with tab2:
    # Embeber HTML
    components.html(html_grid.HTML_LIFI_R, height=altura, scrolling=True)  
with tab3:
    # Embeber HTML
    components.html(html_grid.HTML_LIFI_M, height=altura, scrolling=True)
with tab4:
    # Embeber HTML
    components.html(html_grid.HTML_LIFI_P, height=altura, scrolling=True)

# PArte para calcular estadisticas
st.markdown("### ¡Revisa tu progreso! (Estadísticas)")

col1, col, col2, cola = st.columns([2,1,2,1])

with col1:
  progreso_text = st.text_area(
      "Pega aquí la información copiada arriba de la malla y haz 'Ctrl+Enter':",
      height=100,
      placeholder='{"approved":["ICS181","EFI100"]}'
  )

with col2:
  # ---- UI ----
  if progreso_text.strip():
      try:
          data = json.loads(progreso_text)
          approved = set(data.get("approved", []))
          ac, tc, pc, acred, tcred, pcred = calc_stats(approved)
  
          st.write("")
        
          m1, m2, m3 = st.columns(3)

          m1.metric("Créditos aprobados", f"{int(acred)} / {int(tcred)}")
          m2.metric("Porcentaje de creditos", f"{pcred:.0f}%")
          m3.metric("Materias aprobadas", f"{ac} / {tc}")
      except Exception as e:
          st.error(
              "JSON inválido. Ejemplo válido: {\"approved\":[\"ICS181\",\"EFI100\"]}\n\n"
              f"Error: {e}"
          )
  else:
    st.write("")
    st.write("")

    st.info("Ingresa el JSON para poder ver tu progreso.")
