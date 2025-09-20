import streamlit as st
import base64

st.set_page_config(
    page_title="Profesores LIFI",
    page_icon=":telescope:",
    layout="wide",    
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)

# Función para convertir imagen a base64
def get_base64_from_file(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        st.error(f"Error al leer la imagen: {e}")
        return None

# Cargar imagen de fondo
file_path = '/mount/src/modularesbasicas/app/maestros_bg.jpg'
img_base64 = get_base64_from_file(file_path)

if img_base64:
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            opacity: 0.4;
            z-index: 0;
        }}
        [data-testid="stAppViewContainer"] > * {{
            position: relative;
            z-index: 1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Estilos CSS
st.markdown("""
<style>
/* Tarjeta principal */
.profesor-card {
    display: flex;
    flex-direction: row;
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.2s;
    align-items: center; /* Centra verticalmente todos los elementos */
}
.profesor-card:hover {
    transform: translateY(-5px);
}
.profesor-imagen {
    width: 150px;
    height: 150px;
    border-radius: 10px;
    margin-right: 20px;
}
.profesor-info {
    flex: 1;
}

.profesor-nombre {
    font-size: 24px;
    font-weight: bold;
    color: #1e3d59;
    margin-bottom: 5px;
}

.profesor-nombre a {
    text-decoration: none;
    color: #1e3d59;
    transition: color 0.3s, text-decoration 0.3s;
}

.profesor-nombre a:hover {
    color: #3498db;
    text-decoration: underline;
    cursor: pointer;
}

.profesor-grado {
    font-size: 16px;
    font-style: italic;
    color: #5e6572;
    margin-bottom: 10px;
}

.profesor-correo {
    font-size: 14px;
    color: #3498db;
    margin-bottom: 10px;
}

.profesor-linea {
    font-size: 15px;
    color: #2c3e50;
    padding: 8px 10px;
    background-color: #e9ecef;
    border-radius: 5px;
    display: inline-block;
    margin-bottom: 5px;
}

.requisitos-container {
    margin-top: 13px;
}
.requisitos-titulo {
    font-size: 14px;
    font-weight: bold;
    color: #1e3d59;
    cursor: pointer;
    background-color: #f8f9fa;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
}

.requisitos-content {
    display: none;
    font-size: 13px;
    margin-top: 10px;
    padding: 10px;
    background-color: #f0f0f0; /* Cambia el color de fondo a un gris claro */
    color: #333; /* Cambia el color del texto a un gris oscuro para mejor legibilidad */
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    animation: slideDown 1s ease-out;
}
.requisitos-container input[type="checkbox"] {
    display: none;
}
.requisitos-container input[type="checkbox"]:checked ~ .requisitos-content {
    display: block;
}.requisitos-container input[type="checkbox"]:checked ~ .requisitos-titulo::after {
    content: "▲";
}

/* Diseño para moviles */
@media (max-width: 768px) {
    .profesor-card {
        flex-direction: column; /* Cambiar a columna para móviles */
        text-align: center; /* Centrar contenido */
        padding: 15px; /* Reducir padding */
    }
    .profesor-imagen {
        margin-right: 0; /* Eliminar margen derecho */
        margin-bottom: 15px; /* Añadir margen inferior */
        width: 120px; /* Ajustar tamaño de imagen */
        height: 120px;
    }
    .profesor-info {
        width: 100%; /* Ocupar ancho completo */
    }
    .profesor-nombre {
        font-size: 20px; /* Reducir tamaño de fuente */
    }
    .profesor-grado {
        font-size: 14px; /* Reducir tamaño de fuente */
    }
    .profesor-linea {
        display: block; /* Asegurar que ocupe todo el ancho */
        margin-bottom: 10px;
    }
}
</style>
""", unsafe_allow_html=True)

# Función para mostrar un profesor
def mostrar_profesor(imagen, nombre, puesto, correo, aptitudes, SNI=None, enlace=None, *lineas ):
    # Crear un ID único basado en el nombre (sin espacios ni caracteres especiales para HTML)
    profesor_id = "".join(c for c in nombre if c.isalnum()).lower()
    
    lineas_html = ''.join([f'<span class="profesor-linea">📑 {linea}</span><br>' for linea in lineas])
    
    requisitos_html = f"""
    <div class="requisitos-container">
        <label class="requisitos-titulo" for="requisitos-{profesor_id}">Mostrar Requisitos</label>
        <input type="checkbox" id="requisitos-{profesor_id}">
        <div class="requisitos-content">
            <div class="alumno-aptitudes">{aptitudes}
    """
    sni_html = f"<div class='profesor-sni' style='font-size: 14px; color: #5e6572;'>{SNI}</div>" if SNI else ""

    html_nombre = f'<div class="profesor-nombre"><a href="{enlace}" class="profesor-nombre">{nombre}</a></div>' if enlace else f'<div class="profesor-nombre">{nombre}</div>'
    
    html = f"""
    <div class="profesor-card">
        <img src="data:image/jpeg;base64,{imagen}" class="profesor-imagen">
        <div class="profesor-info">
            {html_nombre}
            <div class="profesor-grado">{puesto}</div>
            {sni_html}
            <div class="profesor-correo"><a href="mailto:{correo}">{correo}</a></div>
            <div>{lineas_html}</div>
            {requisitos_html}

    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

    
st.title("Profesores para Modulares")
st.header("Licenciatura en Física")

col1, col2 = st.columns(2)

with col1:
    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/chan.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Néstor García Chan",
            "Profesor Investigador Titular B",
            "nestor.gchan@academicos.udg.mx",
            "EDP, Programación, Métodos Numéricos",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://academicos.cucei.udg.mx/academicos/2306093",
            "Modelación Matemática y Simulación en Problemas Medioambientales"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/quiñones.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. José Guadalupe Quiñones Galván",
            "Profesor Investigador Titular A",
            "jose.quinones@academicos.udg.mx",
            "Electromagnetismo",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://academicos.cucei.udg.mx/academicos/2955507",
            "Síntesis de Materiales por Técnicas Físicoquímicas"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/zamudio.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Adalberto Zamudio Ojeda",
            "Profesor Investigador Titular A",
            "adalberto.zojeda@academicos.udg.mx",
            "Ganas de aprender",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://academicos.cucei.udg.mx/academicos/2724499",
            "Síntesis de Nanomateriales"
            )
        
    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/espinosa_ramirez.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Alejandro Camilo Espinosa Ramírez",
            " ",
            "alejandro.espinosa@academicos.udg.mx",
            "Haber cursado la asignatura de Mecánica del Medio Contínuo",
            " ",
            "",
            "Oceanografía y Modelación Numérica de Fluidos"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/gonzalez_romero.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Jaime Ricardo González Romero",
            "Profesor de Asignatura B y Técnico Académico Asociado B",
            "jaimer.gonzalezr@academicos.udg.mx",
            "De 2do semestre en adelante, con la posibilidad de tésis para los modulares II y III",
            "Candidato a Miembro del Sistema Nacional de Investigadores",
            "https://academicos.cucei.udg.mx/academicos/2955571",
            "Detección de Ondas de Choque por Medios Ópticos",
            "Simulaciones FEM y Tratamiento LSP", 
            "Espectroscopía e Instrumentación Óptica"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/marquez_lugo.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Ramón Alejandro Márquez Lugo",
            "Profesor Investigador Titular A",
            "alejandro.marquez@academicos.udg.mx",
            "Tiene mucha chamba",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "http://iam.cucei.udg.mx/marquez-lugo",
            "Astrofísica Estelar"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/cros.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dra. Anne Cros",
            "Profesora Investigadora Titular B",
            "anne.cros@academicos.udg.mx",
            "Autodidácta y autónomo",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://www.cucei.udg.mx/maestrias/fisica/es/anne-cros",
            "Interacción Fluido-Estructura"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/alcala.png'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Jaime Alcalá Gutiérrez",
            "Profesor Investigador Titular C",
            "jaime.alcala@academicos.udg.mx",
            "Ninguno",
            " ",
            "https://academicos.cucei.udg.mx/academicos/9427112",
            "Agrometeorología, Agroclimatología y Bioclimática"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/herminio.png'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Luis José Herminio Corral Escobedo",
            "Profesor Investigador Titular C",
            "luis.corral@academicos.udg.mx",
            "Chambeador",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "http://iam.cucei.udg.mx/dr-luis-jose-herminio-corral-escobedo",
            "Estrellas masivas y Cúmulos abiertos",
            "Técnicas de IA para Astrofísica"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/ramirez_ortega.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Jorge Alberto Ramírez Ortega",
            "Profesor Investigador Asociado A",
            "jorge.rortega@academicos.udg.mx",
            "Excelente actitud y disposición por estar en el laboratorio",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "https://scholar.google.com.mx/citations?user=dhmtSJcAAAAJ&hl=es",
            "Síntesis de Nanopartículas de Semiconductores Ternarios y su plicación"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/garcia_luna.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Jose Luis Garcia Luna",
            "Profesor Investigador Titular C",
            "jose.gluna@academicos.udg.mx",
            "Ninguno",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "https://academicos.cucei.udg.mx/academicos/8802629",
            "Física de Partículas"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/pantoja.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Diego Armando Pantoja González",
            "Profesor Investigador Asociado B",
            "diego.pantoja@academicos.udg.mx",
            "Saber MATLAB",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "https://academicos.cucei.udg.mx/academicos/2828367",
            "Modelación Numérica de Oceanografía y Limnología Física."
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/durruty.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Durruty Jesus De Alba Martínez",
            "Profesor de Asignatura B y Técnico Acádemico Titular A",
            "durruty.dealba@academicos.udg.mx",
            "Comprensión lectora en inglés",
            " ",
            "http://iam.cucei.udg.mx/directorio/durruty-jesus-de-alba-martinez",
            "Historia de la Física y la Astronomía en México"
            )

############################# COLUMNA 2 ##################################
with col2:
    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/romero_ibarra.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. José Luis Romero Ibarra",
            "Profesor Investigador Titular A",
            "jose.ribarra@academicos.udg.mx",
            "Aprobar examen de matemáticas",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "https://academicos.cucei.udg.mx/academicos/2604817",
            "Óptica e Información Cuántica"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/santana.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. José Luis Santana Fajardo",
            "Profesor Investigador Titular A",
            "jose.sfajardo@academicos.udg.mx",
            "Interés por la física educativa, apertura para la interdisciplinariedad entre ciencias sociales y ciencias físicas",
            "Candidato a Miembro del Sistema Nacional de Investigadores",
            "https://academicos.cucei.udg.mx/academicos/2405512",
            "Desarrollo y Evaluación de Competencias en Física",
            "Formación docente y Didáctica de la Física"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/gonzalez_ochoa.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Héctor Octavio González Ochoa",
            "Profesor Investigador Titular A",
            "hector.gochoa@academicos.udg.mx",
            "Amable y Responsable",
            " ",
            "https://academicos.cucei.udg.mx/academicos/2955330",
            "Física Estadística"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/mercado.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dra. Liliana Vázquez Mercado",
            "Profesora Investigadora Asociado B",
            "liliana.vmercado@academicos.udg.mx",
            "Ninguno",
            " ",
            "https://academicos.cucei.udg.mx/academicos/2003058",
            "Didáctica de la Física y Cursos Adaptativos de Física"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/michel_uribe.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Carlos Rafael Michel Uribe",
            "Profesor Investigador Titular B",
            "carlos.muribe@academicos.udg.mx",
            "Comporometidos con los objetivos de su trabajo",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://depfisica.cucei.udg.mx/dr-michel-uribe-carlos-rafael",
            "Sensores de luz y Fotocatálisis"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/ceballos.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Oscar Ceballos Sánchez",
            "Profesor Investigador Asociado C",
            "oscar.ceballos@academicos.udg.mx",
            "Gusto por el laboratorio de síntesis química",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "https://academicos.cucei.udg.mx/academicos/2960285",
            "Semiconductores"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/kemp.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Simon Nicholas Kemp",
            "Profesor Investigador Titular C",
            "simon.kemp@academicos.udg.mx",
            "Disponibilidad de ir al IAM y trabajar con IRAF/Linux",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://www.cucei.udg.mx/maestrias/fisica/?q=simon-nicholas-kemp",
            "Galaxias y Cúmulos de Galaxias"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/moreno.jpeg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dra. Claudia Moreno González",
            "Profesor Investigador Titular C",
            "claudia.moreno@academico.udg.mx",
            "Ninguno",
            "Miembro del Sistema Nacional de Investigadores Nivel III",
            "https://depfisica.cucei.udg.mx/dra-moreno-gonzalez-claudia",
            "Ondas gravitacionales (Teoría, Experimentación, Análisis de Datos)"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/santiago_hernandez.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Alberto Santiago Hernández",
            "Profesor de Asignatura B",
            "alberto.santiago@academicos.udg.mx",
            "Haber cursado electromagnetismo, óptica, algún tópico de partículas",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "alberto.santiago@academicos.udg.mx",
            "Ciencias Espaciales (Física Solar)"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/bravo_barcenas.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. David Israel Bravo Barcenas",
            " ",
            "david.bravo@academicos.udg.mx",
            "Interés por aprender temas relacionados con Ciencia de Materiales e Ingeniería de Superficies",
            "Miembro del Sistema Nacional de Investigadores Nivel I",
            "https://scholar.google.es/citations?user=Koyy3S8AAAAJ&hl=es",
            "Ingeniería de Biomateriales Metálicos "
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/cros.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            "",
            "Dra. Susana Muñóz Villegas",
            "Profesora de Asignatura B",
            "susana.munoz@academicos.udg.mx",
            "Gusto por las matemáticas y programación",
            " ",
            "",
            "Modelado matemático"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/santana_aranda.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Miguel Angel Santana Aranda",
            "Profesor Investigador Titular B",
            "msantana.aranda@academicos.udg.mx",
            "Disposición a aprender y recibir retroalimentación del grupo de trabajo",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://www.cucei.udg.mx/maestrias/fisica/es/miguel-angel-santana-aranda",
            "Desarrollo de nuevos materiales para el aprovechamiento de la energía solar y otras fuentes renovables"
            )

    foto_path = '/mount/src/modularesbasicas/app/LIFI/Profesores_LIFI/madriz.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. José Edgar Madriz Aguilar",
            "Profesor Investigador Titular B",
            "jose.madriz@academicos.udg.mx",
            "Responsable y seguro del área que trabajará",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://academicos.cucei.udg.mx/academicos/2947728",
            "Estudio de modelos teóricos sobre la evolución del universo en diferentes teorías de gravitación"
            )
