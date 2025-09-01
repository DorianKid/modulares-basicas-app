(function(){
  const ROMAN = ["","I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"];

  // ---------- util ----------
  function tableEl(){ return document.querySelector('.table'); }
  function cols(){ return document.querySelectorAll('.table .sem-col'); }
  function updateGridColumns(){
    const t = tableEl(); if(!t) return;
    t.style.gridTemplateColumns = `repeat(${cols().length}, minmax(180px, 1.15fr))`;
  }

  // Crea/garantiza N slots como hijos directos de la columna (1..N)
  function ensureSlots(col){
    const N = parseInt(tableEl().dataset.slots || '9', 10);
    let slots = [...col.querySelectorAll(':scope > .slot')];

    // crear los que falten
    for (let i = slots.length + 1; i <= N; i++){
      const s = document.createElement('div');
      s.className = 'slot';
      s.dataset.slot = String(i);
      col.appendChild(s);
      slots.push(s);
    }
    // si hay de más (no deberìa), borramos vacíos al final
    while (slots.length > N){
      const last = slots.pop();
      if (!last.querySelector('.cell')) last.remove();
    }
    // normaliza data-slot 1..N en orden DOM
    slots = [...col.querySelectorAll(':scope > .slot')];
    slots.forEach((s,i)=> s.dataset.slot = String(i+1));
    return slots;
  }

  // Mueve todas las .cell “sueltas” o mal ubicadas dentro de su slot (por número .num)
  function padSlots(col){
    const slots = ensureSlots(col);
    const N = slots.length;

    // 1) tomar todas las .cell que estén directamente bajo la col o bajo un slot
    const strayCells = [];
    // cells sueltas
    [...col.querySelectorAll(':scope > .cell')].forEach(c => strayCells.push(c));
    // cells dentro de slots duplicadas
    slots.forEach(s=>{
      const cs = s.querySelectorAll(':scope > .cell');
      if (cs.length > 1){
        for (let i = 1; i < cs.length; i++) strayCells.push(cs[i]);
      }
    });

    // 2) colocar cada cell en su slot (por número visible .num, si no, por primer vacío)
    function findEmpty(from){
      for (let p = from; p <= N; p++){
        if (!slots[p-1].querySelector('.cell')) return p;
      }
      for (let p = 1; p < from; p++){
        if (!slots[p-1].querySelector('.cell')) return p;
      }
      return null;
    }

    // meter sueltas primero
    strayCells.forEach(c=>{
      let p = parseInt(c.querySelector('.num')?.textContent || '0', 10);
      if (!(p >= 1 && p <= N) || slots[p-1].querySelector('.cell')){
        p = findEmpty(1) || 1;
      }
      slots[p-1].appendChild(c);
    });

    // 3) normalizar números visibles conforme a su slot padre
    slots.forEach((s,i)=>{
      const c = s.querySelector(':scope > .cell');
      if (c){
        const num = c.querySelector('.num'); if (num) num.textContent = String(i+1);
      }
    });
  }

  // Escribir semester/order en COURSES_STATE (no reacomoda DOM)
  function recomputeOrders(){
    const data = window.COURSES_STATE || [];
    const idToIdx = new Map(data.map((c,i)=>[String(c.id), i]));
    document.querySelectorAll('.table .sem-col').forEach(col=>{
      const sem = parseInt(col.dataset.sem,10);
      const slots = ensureSlots(col);
      slots.forEach((s,i)=>{
        const cell = s.querySelector(':scope > .cell');
        if (!cell) return;
        const cid = cell.id.replace('c-','');
        const idx = idToIdx.get(cid);
        if (idx != null){
          data[idx].semester = sem;
          data[idx].order = i+1;            // slot real
        }
        const num = cell.querySelector('.num');
        if (num) num.textContent = String(i+1);
      });
    });
  }

  // ---------- DnD basado en slots contenedores ----------
  function bindColumn(col){
    ensureSlots(col);     // asegura N slots
    padSlots(col);        // mete las celdas en su slot por número
    let dragged = null;

    // habilitar drop SÓLO si el mouse está sobre un slot vacío
    col.addEventListener('dragover', (e)=>{
      if (!document.body.classList.contains('edit-mode')) return;
      const slot = e.target.closest('.slot');
      if (!slot || !col.contains(slot)) return;
      const empty = !slot.querySelector(':scope > .cell');
      if (!empty) return;          // no permitimos soltar sobre slot ocupado
      e.preventDefault();          // <- ¡habilita drop!
      slot.classList.add('drop-ok');
    });

    col.addEventListener('dragleave', (e)=>{
      const slot = e.target.closest('.slot');
      slot?.classList.remove('drop-ok');
    });

    col.addEventListener('drop', (e)=>{
      e.preventDefault();
      const slot = e.target.closest('.slot');
      if (!slot) return;
      slot.classList.remove('drop-ok');
      if (!dragged) return;
      // sólo si está vacío
      if (!slot.querySelector(':scope > .cell')){
        slot.appendChild(dragged);
        dragged.classList.remove('dragging');
        dragged = null;
        recomputeOrders();   // actualiza semester/order y numeritos
      }
    });

    // listeners globales para iniciar/terminar drag
    document.addEventListener('dragstart', (e)=>{
      const cell = e.target.closest('.cell');
      if (!cell || !document.body.classList.contains('edit-mode')) return;
      dragged = cell;
      e.dataTransfer.setData('text/plain', cell.id);
      setTimeout(()=> cell.classList.add('dragging'), 0);
    });

    document.addEventListener('dragend', ()=>{
      const d = document.querySelector('.cell.dragging');
      if (d) d.classList.remove('dragging');
      dragged = null;
      recomputeOrders();   // por si se soltó fuera, sólo sincroniza estado
    });
  }

  function enableEdit(on){
    document.body.classList.toggle('edit-mode', on);
    document.querySelectorAll('.cell').forEach(c=> c.setAttribute('draggable', on ? 'true' : 'false'));
  }

  // ---------- Semestres ----------
  function currentMaxSem(){
    const arr = [...cols()].map(c=>parseInt(c.dataset.sem,10));
    return arr.length ? Math.max(...arr) : 0;
  }

  function addSemester(){
    const t = tableEl(); if (!t) return;
    const maxSem = parseInt(t.dataset.maxsem || '12', 10);
    const next = currentMaxSem() + 1;
    if (next > maxSem){ alert(`Alcanzado el máximo de semestres (${maxSem}).`); return; }

    const head = document.createElement('div');
    head.className = 'sem-head';
    head.textContent = ROMAN[next] || String(next);

    const col = document.createElement('div');
    col.className = 'sem-col';
    col.dataset.sem = String(next);

    // header al principio (antes de la 1ª col)
    const firstCol = t.querySelector('.sem-col');
    if (firstCol) t.insertBefore(head, firstCol); else t.appendChild(head);
    // columna al final
    t.appendChild(col);

    bindColumn(col);
    updateGridColumns();
  }

  function removeLastSemester(){
    const t = tableEl(); if (!t) return;
    const columns = cols();
    if (!columns.length) return;
    const lastCol = columns[columns.length - 1];
    if (lastCol.querySelector('.cell')){
      alert("No se puede eliminar el último semestre porque no está vacío.");
      return;
    }
    const heads = t.querySelectorAll('.sem-head');
    heads[heads.length - 1]?.remove();
    lastCol.remove();
    updateGridColumns();
  }

// --- reemplaza esto ---
// function downloadPDF(){ window.print(); }

// --- por esto ---
function downloadMalla(selector = '.plan') {
  const node = document.querySelector(selector);
  if (!node) return alert('No encontré la malla a exportar');

  // toma todos los <style> y <link rel="stylesheet"> del documento
  const styles = [...document.querySelectorAll('style,link[rel="stylesheet"]')]
    .map(n => n.outerHTML).join('\n');

  // css de impresión para ocultar controles y márgenes
  const printCSS = `
    <style>
      @media print {
        body { margin: 0 !important; }
        /* oculta UI que no debe ir al PDF */
        .edit-toolbar, #view-only, .legend { display: none !important; }
        .plan { box-shadow: none !important; }
      }
    </style>`;

  const w = window.open('', '_blank');
  w.document.write(
    `<!doctype html><html><head>${styles}${printCSS}</head><body>${node.outerHTML}</body></html>`
  );
  w.document.close();
  w.focus();
  // importante: esperar un frame para layout
  setTimeout(()=>{ w.print(); w.close(); }, 50);
}

  // ---------- init ----------
  document.addEventListener('DOMContentLoaded', ()=>{
    const t = tableEl(); if (!t) return;

    // Estado base desde JSON embebido
    const src = document.getElementById('__courses');
    if (src) window.COURSES_STATE = JSON.parse(src.textContent || '[]');
    else window.COURSES_STATE = [];

    // preparar columnas → slots → acomodar celdas dentro de su slot
    document.querySelectorAll('.table .sem-col').forEach(col=>{
      bindColumn(col);
    });
    updateGridColumns();

    // UI
    document.getElementById('edit-toggle')?.addEventListener('change', (e)=> enableEdit(e.target.checked));
    document.getElementById('btn-add-sem')?.addEventListener('click', addSemester);
    document.getElementById('btn-rem-sem')?.addEventListener('click', removeLastSemester);
    document.getElementById('btn-download')?.addEventListener('click', () => downloadMalla('.plan'));
  });
})();

