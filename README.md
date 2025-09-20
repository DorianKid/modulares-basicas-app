# Modulares Básicas — UDG (Web App)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#licencia)  
Aplicación web (licencia MIT) para orientar a estudiantes de la UDG sobre **Modulares Básicas**: qué son, **cómo realizarlas**, **posibles asesores/profesores**, y una **malla curricular dinámica** para planear y **visualizar tu progreso**.

## ✨ Características
- **Guía práctica** de requisitos, proceso y recomendaciones para cursar Modulares Básicas.
- **Directorio de asesores/profesores** con áreas, disponibilidad y formas de contacto.
- **Malla curricular interactiva**: marca módulos completados, prerrequisitos y porcentaje de avance.
- **Interfaz responsive** y ligera (HTML/CSS/JavaScript, sin backend).

## 🧭 Estructura del proyecto (sugerida)
```
modulares-basicas-app/
├─ index.html              # Portada y navegación principal
├─ asesores.html           # Listado/consulta de asesores
├─ malla.html              # Malla curricular dinámica (progreso)
├─ css/                    # Estilos (variables, layout, componentes)
├─ js/                     # Lógica de UI (estado de progreso, filtros, etc.)
├─ data/                   # (Opcional) JSON con asesores, planes y reglas
└─ assets/                 # Logos, íconos y recursos
```

## 🚀 Uso local
1. Clona el repositorio:
   ```bash
   git clone https://github.com/DorianKid/modulares-basicas-app
   cd modulares-basicas-app
   ```
2. Abre `index.html` en tu navegador **o** levanta un servidor estático:
   ```bash
   # Con Python
   python -m http.server 8000
   # Luego visita http://localhost:8000
   ```

## 🖱️ Cómo funciona la malla
- Cada **tarjeta** representa un módulo y puede marcarse como **completado**.
- Los **prerrequisitos** se validan para evitar marcar módulos bloqueados.
- El **porcentaje de avance** se calcula automáticamente.
- (Opcional) El estado puede guardarse en `localStorage` para persistencia en el navegador.

## 🧩 Datos dinámicos (opcional)
Puedes mantener asesores y plan de estudios en archivos `JSON` dentro de `data/`:
- `data/asesores.json` — nombre, área, contacto, campus/centro, notas.
- `data/malla.json` — lista de módulos, clave, nombre, prerrequisitos y créditos.

> Así no necesitas tocar el HTML para actualizar la información.

## 📸 Capturas (coloca tus imágenes)
- `assets/screenshot-home.png` — Portada  
- `assets/screenshot-malla.png` — Malla en acción  
- `assets/screenshot-asesores.png` — Buscador de asesores

## 🤝 Contribución
Las PRs y sugerencias son bienvenidas. Lineamientos breves:
- Mantén estilos y nombres de clases consistentes.
- No agregues dependencias pesadas sin justificar.
- Incluye una breve descripción y capturas en los cambios de UI.

## 📄 Licencia
Este proyecto está bajo la **Licencia MIT**. Consulta el archivo [`LICENSE`](./LICENSE).

---

**One-liner (EN):**  
MIT-licensed web app for UDG students: advisor directory and an interactive curriculum map to plan and track progress in “Modulares Básicas.”
