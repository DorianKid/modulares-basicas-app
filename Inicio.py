import streamlit as st
import base64
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(
    page_title="Modulares",
    page_icon=":pencil:",
    layout="wide",    
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)

######################## FUNCIONES ##########################################
# Función para leer el archivo .tex
def read_tex_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
######################## ESTILOS CSS ########################################
# Aplicar estilos CSS para cambiar el color del botón normal
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;  /* Color de fondo */
        color: white;  /* Color del texto */
        border: none;  /* Sin borde */
        padding: 8px 13px;  /* Espaciado interno */
        text-align: center;  /* Alinear texto */
        text-decoration: none;  /* Sin subrayado */
        display: inline-block;  /* Mostrar en línea */
        font-size: 16px;  /* Tamaño de fuente */
        margin: 4px 2px;  /* Margen */
        cursor: pointer;  /* Cursor de puntero */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título principal con icono
st.title("📚 Proyectos Modulares: Evaluación Integral en CUCEI")

# Sección: ¿Qué son los modulares?
st.header("🔍 ¿Qué son los modulares?")
# Descripción inicial
st.markdown("""
Los [**Proyectos Modulares**](http://proyectosciencia.cucei.udg.mx) son una estrategia educativa clave en el modelo académico del 
Centro Universitario de Ciencias Exactas e Ingenierías (**CUCEI**) de la **Universidad de Guadalajara**. Estos proyectos constituyen un **sistema de evaluación integral** que permite a los estudiantes demostrar la adquisición y aplicación de competencias específicas en diversas etapas de su formación profesional.

Son actividades académicas estructuradas que evalúan la integración de **conocimientos, habilidades y actitudes** adquiridas durante un período determinado. Más que simples trabajos finales, representan **evidencias concretas** del desarrollo de competencias profesionales y metodológicas necesarias para el ejercicio de su profesión.
""")

# Importancia educativa con resaltado
st.success("📢 **Importancia Educativa:** Estos desempeñan un papel crucial en la formación académica, asegurando que los estudiantes adquieran competencias aplicables al mundo real.")

st.divider()

# Características comunes con diseño de columnas
st.header("📌 Características")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Enfoque progresivo")
    st.markdown("""
    - Se organizan en **niveles de complejidad creciente** a lo largo de la formación.
    - Integran **conocimientos de diversas asignaturas**.
    - Se enfocan en la **resolución de problemas reales o simulados** del ámbito profesional.
    """)

with col2:
    st.subheader("🔬 Desarrollo metodológico")
    st.markdown("""
    - Aplicación de **métodos científicos y técnicas específicas** según la disciplina.
    - **Evaluación integral**: se consideran proceso, metodología y competencias adquiridas.
    - **Asesoría especializada** por parte de profesores.
    """)

st.divider()

# Modalidades de presentación con diseño en columnas
st.header("📑 Modalidades de Presentación")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - 🗣️ **Presentaciones orales**: Exposiciones formales ante comités evaluadores.
    - 📊 **Pósters científicos**: Presentaciones visuales del trabajo realizado.
    - 🔧 **Prototipos**: Desarrollo de modelos físicos o funcionales.
    """)

with col2:
    st.markdown("""
    - 📋 **Reportes técnicos**: Documentos detallados del proceso y resultados.
    - 📄 **Artículos científicos**: Trabajos estructurados según estándares académicos.
    - 🖍️ **Materiales Educativos**: Creación de recursos didácticos para el aprendizaje
    """)
st.warning("⚠️ Importante: Los requerimientos y modalidades de presentación pueden variar según la carrera. Es recomendable revisar las especificaciones particulares de cada programa académico.")

st.divider()

# Física
st.header("🔭 Modulares en Física")
st.markdown("""
Los [proyectos modulares](https://www.cucei.udg.mx/carreras/fisica/proyectos-modulares) en Física evalúan progresivamente habilidades metodológicas, analíticas y creativas:
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### **Modular 1: Habilidades Básicas** *(Presentación en Póster)*
    - **Metodológicas:** Aplicación del método científico en planteamiento y resolución de problemas
    - **Capacidad Analítica:** Obtención de resultados con fundamentos científicos
    - **Creatividad:** Soluciones innovadoras al problema planteado
    
    #### **Modular 3: Habilidades Especializantes** *(Presentación Oral)*
    - **Metodológicas:** Aplicación en áreas de física contemporánea con métodos matemáticos
    - **Capacidad Analítica:** Resultados con amplia discusión teórica y experimental
    - **Creatividad:** Originalidad en contenido teórico o desarrollo experimental
    """)

with col2:
    st.markdown("""
    #### **Modular 2: Habilidades Fundamentales** *(Presentación Oral)*
    - **Metodológicas:** Disertación y fundamentación de temas específicos de física
    - **Capacidad Analítica:** Resultados analíticamente fundamentados con interpretación teórica
    - **Creatividad:** Originalidad en la resolución y discusión
    
    #### **Modular 4: Habilidad Inter o Multidisciplinar** *(Presentación Oral)*
    - **Metodológicas:** Aplicación de la física en otras ciencias o disciplinas
    - **Capacidad Analítica:** Resultados con perspectiva interdisciplinar
    - **Creatividad:** Contenido original o reportes técnicos/servicio social
    """)

st.info("🖇️ Informacion sobre la convocatoria en el siguiente [link](https://sites.google.com/academicos.udg.mx/convocatoria-modulares-lifi/convocatoria-pm)")


st.subheader("📑 Modalidades")
# Selección de modalidad
selected_modalidad = st.selectbox("Selecciona una modalidad:", ["Presentación Oral", "Presentación Póster"])

if selected_modalidad == "Presentación Oral":    
    st.markdown("""
        #### Instrucciones: Presentación Oral
        - **Duración**: Las presentaciones orales deben durar 20 minutos, seguidos de 5 minutos para preguntas.
        - **Formato**: Se aceptan únicamente presentaciones en formato PowerPoint o PDF. Si planeas incluir animaciones, verifica su compatibilidad y consulta en el área de registro si será posible visualizarlas en la sala.
        - **Envío de Presentaciones**: Envía tu presentación por correo a la Coordinación o entrégala personalmente para que se suba al sistema. Esto ayudará a evitar contratiempos durante las presentaciones.
    """)
else:
    # Sección de Presentación en Poster
    st.markdown("""
        #### Intrucciones: Presentación en Póster        
        - **Título**: 
          - Debe coincidir con el título del proyecto presentado.
          - El tamaño de fuente recomendado es de 48 puntos.
          - Incluye los nombres de los autores y la universidad de adscripción, con un tamaño de fuente de 48 a 60 puntos para los encabezados.
        
        - **Tamaño**: 
            - El tamaño máximo del póster debe ser de 90 x 120 cm.
        
        - **Tipografía**: 
          - Asegúrate de que el contenido sea legible desde una distancia de dos metros.
          - Utiliza una combinación de letras MAYÚSCULAS y minúsculas; evita el uso exclusivo de mayúsculas, ya que es difícil de leer.
          - No combines diferentes estilos de tipo o fuente.
        
        - **Contenido**:
          - El tamaño de fuente sugerido es de 24 a 32 puntos a espacio simple.
          - El texto debe ser conciso y de fácil lectura.
          - El mensaje del póster debe ser claro y comprensible sin requerir explicación oral. Presenta los métodos de manera simple y directa.
        
        - **Estructura**:
          - Los paneles más importantes son la Introducción y las Conclusiones. Estos deben ser simples, concisos y visualmente atractivos.
          - Los resultados deben presentarse gráficamente siempre que sea posible; evita grandes tablas de datos. Los resultados deben ser consistentes con los presentados en la propuesta de proyecto.
        
        - **Visuales**:
          - Utiliza dibujos, símbolos y colores. Las leyendas de las figuras son esenciales y deben ser breves pero informativas.
          - Si usas gráficos, asegúrate de que tengan un encabezado corto.
          - Los gráficos y fotografías no deben ser más pequeños que 12 cm x 18 cm.
          - Utiliza el espacio del póster para atraer a tu audiencia hacia la discusión, evitando detalles complejos de métodos y resultados.
    """)

# Ruta del archivo PDF
pdf_path = "files/PDFs/Plantilla_Modulares.pdf"  # Reemplaza con la ruta a tu archivo PDF

# Contenedor expandible para el PDF
with st.expander("Ver Plantilla", expanded=False):

    col1, col2 = st.columns(2)    
    with col1:
        contenido_tex = read_tex_file("files/PDFs/Plantilla_Modulares.tex")

        # Mostrar el contenido con desplazamiento
        st.text_area("Código LaTeX", value=contenido_tex, height=1250, disabled=True)
        #st.code(contenido_tex)
    
    with col2:
        annotations = [
                {
                "page": 1,
                "x": 0,
                "y": 792,
                "height": .1,
                "width": 595,
                "color": "red"
                },
                {
                "page": 2,
                "x": 0,
                "y": 792,
                "height": .1,
                "width": 595,
                "color": "red"
                }
            ]
        
        # Aquí deberías implementar tu función pdf_viewer
        pdf_viewer(input=pdf_path, annotations=annotations)    

st.divider()

tab1, tab2 = st.tabs(["Ejemplo 1", "Ejemplo 2"])

st.divider()

# Químico Farmacobiólogo
st.header("💊 Modulares en Químico Farmacéutico Biólogo")
st.markdown("""
Los [proyectos modulares](https://www.cucei.udg.mx/carreras/farmaceutica/es/documento/proyectos-modulares) en Químico Farmacéutico Biólogo se enfocan en competencias intermedias y avanzadas:
""")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### **Proyectos Modulares de Competencias Intermedias**
    - Determinación de parámetros físicos, químicos, biológicos y farmacéuticos
    - Análisis de componentes y factores en procesos biológicos e industriales
    - Aplicación de conocimientos para estrategias y productos innovadores
    - Análisis y procesamiento de datos con herramientas estadísticas
    - Comparación de referencias mediante uso adecuado de información
    """)

with col2:
    st.markdown("""
    #### **Proyectos Modulares de Competencias Avanzadas**
    - Desarrollo de habilidades avanzadas en investigación farmacéutica y biológica
    - Aplicación de conocimientos especializados en situaciones profesionales
    - Integración de fundamentos teóricos con aplicaciones prácticas
    """)

# Diccionario de archivos PDF con sus descripciones y número de páginas
pdf_files = {
    "📄 Trabajo de Investigación": {
        "path": "files/PDFs/Lineamientos_Trabajo_Investigacion.pdf",
        "pages": 11,  # Cambia esto al número real de páginas
        "description": "Desarrollo de proyectos con método científico, hipótesis y resultados analíticos."
    },
    "🖍️ Materiales Educativos": {
        "path": "files/PDFs/Lineamientos_Materiales_Educativos.pdf",
        "pages": 2,  # Cambia esto al número real de páginas
        "description": "Creación de recursos didácticos para el aprendizaje en ciencias farmacéuticas."
    },
    "🔧 Prototipo": {
        "path": "files/PDFs/Lineamientos_Prototipo.pdf",
        "pages": 4,  # Cambia esto al número real de páginas
        "description": "Desarrollo de modelos físicos o funcionales de productos farmacéuticos o biológicos."
    },
    "📋 Reporte": {
        "path": "files/PDFs/Lineamientos_Reporte.pdf",
        "pages": 3,  # Cambia esto al número real de páginas
        "description": "Documentación técnica de procesos o investigaciones específicas."
    },
    "🫂 Vinculación Social": {
        "path": "files/PDFs/Lineamientos_Vinculacion_Social.pdf",
        "pages": 3,  # Cambia esto al número real de páginas
        "description": "Proyectos con impacto en comunidades o sectores específicos."
    }
}

# Inicializa el estado de la página y el PDF actual
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1

if 'current_pdf' not in st.session_state:
    st.session_state.current_pdf = list(pdf_files.values())[0]["path"]  # Primer PDF por defecto

st.subheader("📑 Modalidades")
# Selección de modalidad
selected_modalidad = st.selectbox("Selecciona una modalidad:", list(pdf_files.keys()))

# Actualizar el PDF actual y la descripción según la modalidad seleccionada
st.session_state.current_pdf = pdf_files[selected_modalidad]["path"]
description = pdf_files[selected_modalidad]["description"]
total_pages = pdf_files[selected_modalidad]["pages"]

# Mostrar la descripción de la modalidad
st.markdown(f"#### {selected_modalidad}")
st.write(description)

# Contenedor expandible para el PDF
with st.expander("Ver Lineamientos", expanded=False):
    # Aquí deberías implementar tu función pdf_viewer
    pdf_viewer(
        input=st.session_state.current_pdf,
        pages_to_render=[st.session_state.current_page],  # Renderiza solo la página actual
    )

    # Botones para navegar entre las páginas
    col1, col2, col3 = st.columns([11, 11, 4])
    
    if col1.button("Página Anterior"):
        if st.session_state.current_page > 1:
            st.session_state.current_page -= 1

    # Leer el contenido del PDF para el botón de descarga
    with open(st.session_state.current_pdf, "rb") as f:
        pdf_data = f.read()
        
    # Mostrar el botón de descarga
    col2.download_button(
        'Descargar',
        pdf_data,
        file_name=selected_modalidad + '.pdf',
        mime='application/pdf',
        help=f"Haz clic para descargar el PDF de {selected_modalidad}."
    )
    
    if col3.button("Siguiente Página"):
        if st.session_state.current_page < total_pages:
            st.session_state.current_page += 1
            
st.divider()

tab1, tab2 = st.tabs(["Ejemplo 1", "Ejemplo 2"])

st.divider()
