# Modulares Básicas — UDG (Web App)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Made with: Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-blue)](https://streamlit.io/)

Aplicación web (Python + **Streamlit** + HTML/CSS/JS) para orientar a estudiantes de la UDG en **Modulares Básicas**: qué son, **cómo realizarlas**, **posibles asesores/profesores** y una **malla curricular dinámica** para planear y **visualizar tu progreso**.

> Público objetivo: estudiantes de **CUCEI / División de Ciencias Básicas** que buscan organizar su trayectoria y entender requisitos/prerrequisitos.

---

## ✨ Características

- **Malla curricular interactiva**: marca módulos completados, valida **prerrequisitos** y calcula **porcentaje de avance** en tiempo real.
- **Directorio de asesores/profesores**: búsqueda/filtrado por área y datos de contacto (opcional).
- **Recursos**: PDFs/guías/material adicional para apoyar la realización de Modulares.
- **Persistencia local** (opcional): guarda el estado en `localStorage` (navegador) o en un archivo JSON.
- **UI ligera y responsive**: estilos personalizados y controles accesibles.
- **Licencia MIT** (ver `LICENSE`).

---

## 🧭 Estructura del proyecto (sugerida)

```
modulares-basicas-app/
├─ app/                    # Código principal (Streamlit / Python)
│  ├─ app.py               # Punto de entrada
│  ├─ components/          # Componentes UI (helpers/HTML)
│  └─ utils/               # Utilidades (validaciones, carga de datos, etc.)
├─ data/                   # (Opcional) JSON con asesores, plan y reglas
├─ assets/                 # Logos, íconos, capturas de pantalla
├─ css/                    # Estilos
├─ js/                     # Scripts auxiliares
├─ LICENSE                 # MIT
└─ README.md               # Este archivo
```

> Si tu estructura difiere, ajusta los nombres de rutas en este README.


---

## 🚀 Ejecución local

1) **Clonar** el repo
```bash
git clone https://github.com/DorianKid/modulares-basicas-app
cd modulares-basicas-app
```

2) **Crear entorno** e **instalar dependencias** (ejemplo con `pip`)
```bash
python -m venv .venv
# Activa el entorno
#   Windows: .venv\Scripts\activate
#   macOS/Linux: source .venv/bin/activate

pip install --upgrade pip
# Si tienes requirements.txt:
# pip install -r requirements.txt

# Si no, instala lo mínimo para correr Streamlit
pip install streamlit
```

3) **Ejecutar la app**
```bash
# Si el entrypoint está en app/app.py
streamlit run app/app.py
# o si está en la raíz:
# streamlit run app.py
```

4) Abre `http://localhost:8501` en tu navegador.


---

## 🖱️ Cómo funciona la malla

- Cada **tarjeta** representa un módulo: puedes marcarla como **completada**.
- Los **prerrequisitos** se validan automáticamente antes de permitir el check.
- El **porcentaje de avance** se calcula con base en los créditos/total de módulos.
- **Estado/persistencia** (opcional): se puede guardar y restaurar el progreso del usuario.

> Sugerencia técnica: mantener la lista de módulos y sus relaciones en `data/malla.json` para no tocar el HTML/Python al actualizar.


---

## 🧩 Datos dinámicos (opcional)

Estructuras JSON sugeridas:

**`data/asesores.json`**
```json
[
  {
    "nombre": "Dra. Nombre Apellido",
    "area": "Física / Matemáticas / Computación",
    "correo": "nombre@udg.mx",
    "centro": "CUCEI",
    "notas": "Temas de interés, horarios, etc."
  }
]
```

**`data/malla.json`**
```json
[
  {
    "clave": "MB101",
    "nombre": "Módulo A",
    "creditos": 8,
    "prerrequisitos": ["MB001", "MB050"]
  }
]
```

---

## 📸 Capturas (coloca tus imágenes)

- `assets/screenshot-home.png` — Portada
- `assets/screenshot-malla.png` — Malla en acción
- `assets/screenshot-asesores.png` — Buscador de asesores

> Tip: Recorta imágenes y usa nombres consistentes para facilitar el mantenimiento.


---

## 🧪 Testing rápido (sugerido)

- **Validación de prerrequisitos**: casos con dependencias en cadena y ciclos.
- **Persistencia**: simular recarga de página y restauración del estado.
- **Accesibilidad**: navegación por teclado y contraste.
- **Responsive**: ver en móvil/tablet/escritorio.


---

## 🤝 Contribución

Las PRs y sugerencias son bienvenidas. Lineamientos breves:

- Sigue el estilo del proyecto (nombres de clases/archivos consistentes).
- Evita dependencias pesadas sin justificación.
- Incluye una breve descripción y capturas en cambios de UI.
- Si agregas nuevos datos JSON, valida el esquema (prerrequisitos existentes, claves únicas).


---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta [`LICENSE`](./LICENSE).


---

## ℹ️ Notas

- El objetivo del proyecto es **informar** a alumnas/os sobre Modulares Básicas y ofrecer una **herramienta práctica** para planear la trayectoria académica.
- Si deseas desplegarlo, puedes usar **Streamlit Community Cloud** o cualquier hosting que soporte apps Python/Streamlit.

