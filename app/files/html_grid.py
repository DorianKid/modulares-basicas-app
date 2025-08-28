import os, json
from collections import defaultdict
from typing import List, Dict, Any
from LIFI.courses_data_lifi import (base_lifi_courses, mod_lifi_courses, real_lifi_courses, per_lifi_courses)

# ========= HOT RELOAD de archivos por mtime =========
_FILE_CACHE: Dict[str, Dict[str, Any]] = {}

def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def _load_text(path: str) -> str:
    """Devuelve el texto del archivo y lo recarga solo si cambia su mtime."""
    try:
        mtime = os.path.getmtime(path)
    except OSError:
        return ""
    cached = _FILE_CACHE.get(path)
    if cached and cached["mtime"] == mtime:
        return cached["text"]
    text = _read_text(path)
    _FILE_CACHE[path] = {"mtime": mtime, "text": text}
    return text

def load_css() -> str:
    return _load_text("app/files/style.css")

def load_js_export() -> str:
    return f"<script>{_load_text('app/files/grid_functions.js')}</script>"

def load_js_dnd() -> str:
    return f"<script>{_load_text('app/files/drag_and_drop.js')}</script>"

ROMAN = ["", "I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]

AREA_CLASS_LIFI = {
    "mate":"mate","fis":"fis","progra":"progra","lab":"lab",
    "metodo":"metodo","extra":"extra","quim":"quim","educ":"educ"
}

AREA_LABELS_LIFI = {
    "mate": "Matemáticas",
    "fis": "Física",
    "progra": "Programación",
    "metodo": "Metodología",
    "lab": "Laboratorios",
    "quim": "Química",
    "educ": "Educativo",
    "extra": "Extras",
}

# Default labels por si no te pasan area_labels
AREA_LABELS_DEFAULT = AREA_LABELS_LIFI.copy()

def _order_by_id(courses: List[Dict[str, Any]]) -> Dict[str, int]:
    return {c["id"]: c.get("order") for c in courses}

def prereq_badges_html(course: Dict[str, Any], courses: List[Dict[str, Any]]) -> str:
    order_by_id = _order_by_id(courses)
    req_orders = [order_by_id.get(pid) for pid in course.get("prereqs", [])]
    req_orders = [o for o in req_orders if o is not None]
    return "".join(f'<span class="badge-pr">{o}</span>' for o in req_orders)

# --- Ghost (para modo normal) ---
def ghost_cell_html(rows: int = 1) -> str:
    return f'<div class="cell ghost" style="grid-row: span {int(rows)};"></div>'

def course_cell_html(
    c: Dict[str, Any],
    courses: List[Dict[str, Any]],
    area_class: Dict[str, str] = None,
) -> str:
    # Ignoramos spacers en los datos (el padding lo hacemos nosotros)
    if c.get("kind") == "spacer":
        return ""

    area_class = area_class or AREA_CLASS_LIFI
    area_cls = area_class.get(c.get("area", ""), "")
    locked_class = " locked dep-" + c["id"] if c.get("prereqs") else ""
    chk_id = f"done-{c['id']}"
    credits = c.get("credits", 0)
    hours   = c.get("hours", 0)
    prereqs_attr = ",".join(c.get("prereqs", []))

    def _area_of(pid: str) -> str:
        for x in courses:
            if x["id"] == pid:
                return area_class.get(x.get("area", ""), "")
        return ""

    def _order_of(pid: str):
        for x in courses:
            if x["id"] == pid:
                return x.get("order", "")
        return ""

    prereq_badges = "".join(
        f'<span class="badge-pr {_area_of(p)}">{_order_of(p)}</span>'
        for p in c.get("prereqs", [])
    )

    return f"""
    <div class="cell{locked_class}" id="c-{c['id']}" data-prereqs="{prereqs_attr}">
      <label class="tick" for="{chk_id}">
        <input type="checkbox" id="{chk_id}"><span>Aprobado</span>
      </label>
      <div class="card {area_cls}">
        <div class="code-row">
          <span>{c.get('code','')}</span>
          <span class="num">{c.get('order','')}</span>
        </div>
        <div class="title">{c.get('name','')}</div>
        <div class="footer">
          <div class="prereq-badges">{prereq_badges}</div>
          <div class="footer-right">
            <div class="badge cred">{credits} C</div>
            <div class="badge hours">{hours} H</div>
          </div>
        </div>
      </div>
    </div>
    """
    
def semester_column_html(
    sem: int,
    by_sem: Dict[int, List[Dict[str, Any]]],
    courses: List[Dict[str, Any]],
    area_class: Dict[str, str] = None,
    *,
    editable: bool = False,
    slots_per_semester: int = 9,
) -> str:
    items = sorted(by_sem.get(sem, []), key=lambda x: x.get("order", 9999))

    used_slots = 0
    html_parts: list[str] = []

    for c in items:
        if c.get("kind") == "spacer":
            if not editable:
                rows = int(c.get("rows", 1) or 1)
                html_parts.append(ghost_cell_html(rows))
                used_slots += rows
            # si editable=True ignoramos los spacers del dataset
        else:
            html_parts.append(course_cell_html(c, courses, area_class=area_class))
            used_slots += int(c.get("rows", 1) or 1)

    if not editable:
        pad = max(0, slots_per_semester - used_slots)
        if pad:
            html_parts.extend(ghost_cell_html() for _ in range(pad))

    return f"<div class='sem-col' data-sem='{int(sem)}'>{''.join(html_parts)}</div>"

def build_unlock_rules(courses: List[Dict[str, Any]]) -> str:
    rules = []
    for c in courses:
        prereqs = c.get("prereqs", [])
        if not prereqs:
            continue
        chain = "".join([f":has(#done-{req}:checked)" for req in prereqs])
        idsel = f".dep-{c['id']}"
        rules.append(f"body{chain} {idsel}{{pointer-events:auto;}}")
        rules.append(f"body{chain} {idsel} .tick{{pointer-events:auto;}}")
        rules.append(f"body{chain} {idsel} .card::after{{display:none;}}")
    return "\n".join(rules)

def legend_html(area_class: Dict[str, str], area_labels: Dict[str, str] | None = None) -> str:
    labels = area_labels or AREA_LABELS_DEFAULT
    items = []
    for area_key, css_cls in area_class.items():
        label = labels.get(area_key, area_key.capitalize())
        items.append(
            f"<div style=\"display:flex;align-items:center;gap:8px\">"
            f"<span class=\"dot {css_cls}\"></span> {label}</div>"
        )
    return (
        "<div class=\"legend\" "
        "style=\"display:flex;flex-wrap:wrap;gap:12px;margin:16px 4px;"
        "color:#374151;position:relative;z-index:10;"
        "justify-content:center; text-align:center;"
        "font-size: var(--legend-fs, 1rem);\">"  # 👈 aquí
        + "".join(items) +
        "</div>"
    )

def render_html(
    courses: List[Dict[str, Any]],
    area_class: Dict[str, str],
    area_labels: Dict[str, str],
    *,
    editable: bool = False,        # 👈 bandera para activar edición
    zoom: float = 0.7
) -> str:
    # ... agrupar por semestre como ya lo tienes ...

    css = load_css()               # 👈 lee CSS con hot-reload
    js_export = load_js_export()   # 👈 JS de utilidades (copiar progreso)
    js_dnd = load_js_dnd() if editable else ""   # 👈 solo si editable

    data_json = json.dumps(data, ensure_ascii=False)
    slots_per_semester = 9
    max_semesters = 12

    html = f"""
<style>{css}
{unlock_css}</style>

<div class="plan-zoom-wrap" style="--plan-zoom:{zoom};">
  <div class="plan plan-zoom">
    <h1 style="margin:0 0 8px 4px;">Malla Curricular Interactiva</h1>

    <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;margin:0 4px 14px 4px;">
      <p style="margin:0;color:#444">
        Marca materias aprobadas haciendo click en ellas para ir viendo tu progreso en la carrera.
        Usa el botón para exportar tu progreso como JSON y ver tus estadísticas.
      </p>

      <label style="display:inline-flex;align-items:center;gap:8px;white-space:nowrap;font-weight:600;color:#374151;">
        Solo ver
        <input id="view-only" type="checkbox" style="width:18px;height:18px;cursor:pointer;">
      </label>
    </div>

    {"".join([
      '<div class="edit-toolbar" style="margin:8px 4px;">',
      '<label style="display:inline-flex;align-items:center;gap:8px;font-weight:600;">',
      '<input id="edit-toggle" type="checkbox"> Editar (drag & drop)</label>',
      '<button id="btn-add-sem">➕ Agregar semestre</button>',
      '<button id="btn-rem-sem">➖ Quitar último</button>',
      '<button id="btn-download">🖨️ Descargar malla</button>',
      '</div>'
    ]) if editable else ""}

    <div class="table" data-slots="{slots_per_semester}" data-maxsem="{max_semesters}"
         style="grid-template-columns: repeat({cols}, minmax(180px, 1.15fr));">
      {headers_row}
      {columns}
    </div>

    {legend_html(area_class, area_labels)}

    <div style="display:flex;gap:8px;margin-top:10px;justify-content:center;">
      <button id="btn-copy" 
              style="padding:8px 10px;border-radius:8px;border:1px solid #cbd5e1;background:#f8fafc;cursor:pointer;">
        📋 Copiar progreso
      </button>
    </div>
  </div>
</div>

<script id="__courses" type="application/json">{data_json}</script>
{js_dnd}
{js_export}
"""
    return html


# --- Exportar HTMLs ---
HTML_LIFI_N: str = render_html(base_lifi_courses, AREA_CLASS_LIFI, AREA_LABELS_LIFI, editable=False)
HTML_LIFI_M: str = render_html(mod_lifi_courses,  AREA_CLASS_LIFI, AREA_LABELS_LIFI, editable=False)
HTML_LIFI_R: str = render_html(real_lifi_courses, AREA_CLASS_LIFI, AREA_LABELS_LIFI, editable=False)
HTML_LIFI_P: str = render_html(per_lifi_courses, AREA_CLASS_LIFI, AREA_LABELS_LIFI, editable=True)

