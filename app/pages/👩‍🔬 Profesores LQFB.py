import streamlit as st
import base64

st.set_page_config(
    page_title="Profesores LQFB",
    page_icon=":microscope:",
    layout="wide",    
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)

############################ BACKGROUND ##############################################
# Definir una función para cargar la imagen como base64
def get_base64_from_file(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        st.error(f"Error al leer la imagen: {e}")
        return None

# Intentar encontrar la imagen relativa al directorio del script
file_path = '/mount/src/modularesbasicas/app/maestros_bg.jpg'
# Obtener la imagen en base64
img_base64 = get_base64_from_file(file_path)

st.markdown(
    f"""
    <style>
    /* Crear un pseudo-elemento para el fondo */
    [data-testid="stAppViewContainer"]::before {{
        content: "";
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: 50% auto;
        background-position: center; /* Hay top right, center, top left, bottom right, bottom, etc  */
        background-repeat: repeat;
        background-attachment: fixed;
        
        /* Posicionamiento para cubrir todo */
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        opacity: 0.5;  /* De 0 a 1 siendo % de opacidad */ 
        z-index: 0;  /* Coloca el fondo detrás del contenido */
    }}
    
    /* Asegura que el contenedor principal tenga posición relativa */
    [data-testid="stAppViewContainer"] {{
        position: relative;
        overflow: auto !important;
        height: 100vh;
    }}
    
    /* Asegura que el texto tenga la opacidad completa */
    [data-testid="stAppViewContainer"] > * {{
        opacity: 1 !important;
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

##### Inicio de página #####
    
st.title("Profesores para Modulares")
st.header("Licenciatura en Químico Farmacéutico Biólogo")

col1, col2 = st.columns(2)

with col1:
    foto_path = '/mount/src/modularesbasicas/app/LIFI/chan.jpg'
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
#    .sidebar .sidebar-content {{background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})}} para el sidebar
