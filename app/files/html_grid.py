import json
from collections import defaultdict
from typing import List, Dict, Any
from LIFI.courses_data_lifi import (
    base_lifi_courses, mod_lifi_courses, real_lifi_courses, per_lifi_courses
)
from LQFB.courses_data_lqfb import (
    base_lqfb_courses, mod_lqfb_courses, per_lqfb_courses
)


# --- util: lee CSS/JS en cada render (sin cache) ---
def load_css() -> str:
    with open("app/files/style.css", "r", encoding="utf-8") as f:
        return f.read()

def load_js(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f"<script>{f.read()}</script>"

ROMAN = ["", "I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]

# LIFI COLORES y LABELS
AREA_CLASS_LIFI = {
    "mate":"mate","fis":"fis","progra":"progra","lab":"lab",
    "metodo":"metodo","extra":"extra","quim":"quim","educ":"educ"
}
AREA_LABELS_LIFI = {
    "mate":"Matemáticas","fis":"Física","progra":"Programación","metodo":"Metodología",
    "lab":"Laboratorios","quim":"Química","educ":"Educativo","extra":"Extras"
}

# LQFB COLORES y LABELS
AREA_CLASS_LQFB = {
    "mate":"mate","lab":"lab","metodo":"metodo","extra":"extra","quim":"quim", "med":"med", "fis":"fis", "farma":"farma"
}
AREA_LABELS_LQFB = {
    "mate":"Matemáticas","metodo":"Metodología","lab":"Laboratorios","quim":"Química","extra":"Extras",
    "fis":"Física", "med":"Medicina", "farma":"Farmacia"
}

AREA_LABELS_DEFAULT = AREA_LABELS_LIFI.copy()

def _order_by_id(courses: List[Dict[str, Any]]) -> Dict[str, int]:
    return {c["id"]: c.get("order") for c in courses}

def prereq_badges_html(course: Dict[str, Any], courses: List[Dict[str, Any]]) -> str:
    order_by_id = _order_by_id(courses)
    req_orders = [order_by_id.get(pid) for pid in course.get("prereqs", [])]
    req_orders = [o for o in req_orders if o is not None]
    return "".join(f'<span class="badge-pr">{o}</span>' for o in req_orders)

# --- spacer (solo modo normal) ---
def ghost_cell_html(rows: int = 1) -> str:
    return f'<div class="cell ghost" style="grid-row: span {int(rows)};"></div>'

def course_cell_html(
    c: Dict[str, Any],
    courses: List[Dict[str, Any]],
    area_class: Dict[str, str] | None = None,
) -> str:
    # ignoramos spacers del dataset: el padding lo hacemos nosotros
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
    <div class="cell{locked_class}" id="c-{c['id']}" data-prereqs="{prereqs_attr}" data-home-sem="{c.get('semester','')}">
      <label class="tick" for="{chk_id}">
        <input type="checkbox" id="{chk_id}"><span>Aprobado</span>
      </label>
      <div class="card {area_cls}">
        <div class="code-row">
          <span>{c.get('code','')}</span>
          <span class="num">{c.get('order','')}</span>
          <span class="sem-origin"> Sem {c.get('semester','')}</span> 
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
    area_class: Dict[str, str] | None = None,
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
            # en editable=True no renderizamos spacers del dataset
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
        "font-size: var(--legend-fs, 1rem);\">"
        + "".join(items) +
        "</div>"
    )

def render_html(
    courses: List[Dict[str, Any]],
    area_class: Dict[str, str],
    area_labels: Dict[str, str],
    *,
    editable: bool = False,
    zoom: float = 0.7,
    h1_fs: str = "1.8rem",
    p_fs: str = "1.05rem",
    legend_fs: str = "1rem",
    slots_per_semester: int = 9,
    max_semesters: int = 12,
) -> str:
    css = load_css()
    JS_EXPORT = load_js("app/files/grid_functions.js")
    JS_DND    = load_js("app/files/drag_and_drop.js") if editable else ""

    # --- agrupar por semestre ---
    data = courses
    by_sem: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
    for c in data:
        try:
            sem = int(str(c.get("semester", 0)).strip() or 0)
        except Exception:
            sem = 0
        if sem > 0:
            by_sem[sem].append(c)

    semesters = sorted(by_sem.keys()) or [1]
    n_cols = len(semesters)

    headers_row = "".join(
        f"<div class='sem-head'>{ROMAN[s] if s < len(ROMAN) else str(s)}</div>"
        for s in semesters
    )
    columns = "".join(
        semester_column_html(
            s, by_sem, data, area_class=area_class,
            editable=editable, slots_per_semester=slots_per_semester
        )
        for s in semesters
    )

    unlock_css = build_unlock_rules(data)

    data_json = json.dumps(data, ensure_ascii=False)
    plan_style = f"--h1-fs:{h1_fs}; --p-fs:{p_fs}; --legend-fs:{legend_fs};"
    zoom_wrap_style = f"--plan-zoom:{zoom};"
    table_style = f"grid-template-columns: repeat({n_cols}, minmax(180px, 1.15fr));"

    html = f"""
<style>{css}
{unlock_css}</style>

<div class="plan-zoom-wrap" style="{zoom_wrap_style}">
  <div class="plan plan-zoom" style="--legend-fs:1.75rem; --h1-fs:3rem; --p-fs:1.55rem">
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

    {""
      if not editable else
      f'''
      <div class="edit-toolbar" style="margin:8px 4px; display:flex;flex-wrap:wrap;gap:8px;position:relative;justify-content:center; text-align:center;">
        <label style="font-weight:600;font-size:1.2rem;line-height:1.1;">
          <input id="edit-toggle" type="checkbox"> Editar (drag & drop)
        </label>
        <button id="btn-add-sem"
                       style="padding:8px 10px;border-radius:8px;
                       border:1px solid #cbd5e1;background:#f8fafc;cursor:pointer;
                       font-size:1.2rem; line-height:1.2;">
            ➕ Agregar semestre
        </button>
        <button id="btn-rem-sem" 
                       style="padding:8px 10px;border-radius:8px;
                       border:1px solid #cbd5e1;background:#f8fafc;cursor:pointer;
                       font-size:1.2rem; line-height:1.2;">
            ➖ Quitar último
        </button>
        <button id="btn-download" 
                       style="padding:8px 10px;border-radius:8px;
                       border:1px solid #cbd5e1;background:#f8fafc;cursor:pointer;
                       font-size:1.2rem; line-height:1.2;">
            🖨️ Descargar malla
        </button>
      </div>
      '''
    }

    <div class="table" data-slots="{slots_per_semester}" data-maxsem="{max_semesters}"
         style="{table_style}">
      {headers_row}
      {columns}
    </div>

    {legend_html(area_class, area_labels)}

    <div style="display:flex;gap:8px;margin-top:10px;justify-content:center;">
        <button id="btn-copy"
                style="padding:8px 10px;border-radius:8px;
                       border:1px solid #cbd5e1;background:#f8fafc;cursor:pointer;
                       font-size:1.3rem; line-height:1.2;">
          📋 Copiar progreso
        </button>
    </div>
  </div>
</div>

<script id="__courses" type="application/json">{data_json}</script>
{JS_DND}
{JS_EXPORT}
"""
    return html

# --- HTMLs listos ---
# LIFI
HTML_LIFI_N: str = render_html(base_lifi_courses, AREA_CLASS_LIFI, AREA_LABELS_LIFI, editable=False)
HTML_LIFI_M: str = render_html(mod_lifi_courses,  AREA_CLASS_LIFI, AREA_LABELS_LIFI, editable=False)
HTML_LIFI_R: str = render_html(real_lifi_courses, AREA_CLASS_LIFI, AREA_LABELS_LIFI, editable=False)
HTML_LIFI_P: str = render_html(per_lifi_courses,  AREA_CLASS_LIFI, AREA_LABELS_LIFI, editable=True)

# LQFB
HTML_LQFB_N: str = render_html(base_lqfb_courses, AREA_CLASS_LQFB, AREA_LABELS_LQFB, editable=False)
HTML_LQFB_M: str = render_html(mod_lqfb_courses,  AREA_CLASS_LQFB, AREA_LABELS_LQFB, editable=False)
HTML_LQFB_P: str = render_html(per_lqfb_courses,  AREA_CLASS_LQFB, AREA_LABELS_LQFB, editable=True)

__all__ = [
    "HTML_LIFI_N","HTML_LIFI_M","HTML_LIFI_R","HTML_LIFI_P",
    "HTML_LQFB_N","HTML_LQFB_M","HTML_LQFB_P",
    "render_html","legend_html","build_unlock_rules",
    "semester_column_html","course_cell_html","prereq_badges_html"
]
