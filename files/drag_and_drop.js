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
    // si hay de más (no debería), borrar vacíos al final
    while (slots.length > N){
      const last = slots.pop();
      if (!last.querySelector('.cell')) last.remove();
    }
    // normaliza data-slot 1..N en orden DOM
    slots = [...col.querySelectorAll(':scope > .slot')];
    slots.forEach((s,i)=> s.dataset.slot = String(i+1));
    return slots;
  }

  // Asegura que cada slot tenga a lo sumo 1 .cell y normaliza el numerito
  function padSlots(col){
    const slots = ensureSlots(col);
    const N = slots.length;

    // 1) recoger celdas sueltas (no dentro de .slot) o duplicadas dentro del mismo .slot
    const stray = [];
    [...col.querySelectorAll(':scope > .cell')].forEach(c => stray.push(c));
    slots.forEach(s=>{
      const cs = s.querySelectorAll(':scope > .cell');
      if (cs.length > 1){
        for (let i = 1; i < cs.length; i++) stray.push(cs[i]);
      }
    });

    // 2) poner cada stray en el primer slot libre
    function firstEmpty(fromIdx=0){
      for (let i = fromIdx; i < N; i++){
        if (!slots[i].querySelector('.cell')) return i;
      }
      for (let i = 0; i < fromIdx; i++){
        if (!slots[i].querySelector('.cell')) return i;
      }
      return null;
    }
    stray.forEach(c=>{
      const idx = firstEmpty(0);
      if (idx != null) slots[idx].appendChild(c);
    });

    // 3) normalizar números visibles (solo fuera de edición)
    const editOn = document.body.classList.contains('edit-mode');
    slots.forEach((s,i)=>{
      const c = s.querySelector(':scope > .cell');
      const num = c?.querySelector('.num');
      if (num && !editOn) num.textContent = String(i+1);
    });
  }

  // Guarda semester/order desde el DOM y actualiza numeritos (fuera de edición)
  function recomputeOrders(){
    const data = window.COURSES_STATE || [];
    const idToIdx = new Map(data.map((c,i)=>[String(c.id), i]));
    const editOn = document.body.classList.contains('edit-mode');

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
          data[idx].order = i+1;
        }
        const num = cell.querySelector('.num');
        if (num && !editOn) num.textContent = String(i+1);
      });
    });
    updateNumSemUI();
  }

  // Muestra semestre original en edición, número fuera de edición
  function updateNumSemUI() {
    const editOn = document.body.classList.contains('edit-mode');
    document.querySelectorAll('.table .cell').forEach(cell => {
      const num = cell.querySelector('.num');
      const sem = cell.querySelector('.sem-origin');
      if (sem) {
        const hv = cell.dataset.homeSem || sem.textContent || '';
        sem.textContent = hv; // muestra el "semestre original" del HTML
      }
      if (num) num.style.display = editOn ? 'none'  : 'inline';
      if (sem) sem.style.display = editOn ? 'inline': 'none';
    });
  }

  // ---------- DnD: one-per-slot y swap solo al soltar ----------
  function bindColumn(col){
    ensureSlots(col);
    padSlots(col);

    let dragged = null;
    let originSlot = null;
    let committed = false;

    function clearHints(){
      col.querySelectorAll('.slot.drop-ok').forEach(s=> s.classList.remove('drop-ok'));
    }

    // Drag OVER: solo habilita drop y marca visual el slot destino
    col.addEventListener('dragover', (e)=>{
      if (!document.body.classList.contains('edit-mode')) return;
      const slot = e.target.closest('.slot');
      if (!slot || !col.contains(slot)) return;
      e.preventDefault(); // ← IMPORTANTÍSIMO para permitir drop
      clearHints();
      slot.classList.add('drop-ok');
    });

    col.addEventListener('dragleave', (e)=>{
      const slot = e.target.closest('.slot');
      slot?.classList.remove('drop-ok');
    });

    // DROP: mueve si vacío; si ocupado, intercambia con el de origen
    col.addEventListener('drop', (e)=>{
      if (!dragged) return;
      e.preventDefault();
      committed = true;

      const slot = e.target.closest('.slot');
      clearHints();
      if (!slot) return;

      const from = originSlot || dragged.closest('.slot');
      if (!from) return;

      if (!slot.querySelector(':scope > .cell')){
        // destino vacío → mover
        slot.appendChild(dragged);
      } else {
        // destino ocupado → swap con el de origen
        const other = slot.querySelector(':scope > .cell');
        if (other && from !== slot){
          from.appendChild(other);
          slot.appendChild(dragged);
        }
      }

      dragged.classList.remove('dragging');
      dragged = null; originSlot = null;
      recomputeOrders(); // guarda semester/order y ajusta numeritos
    });

    // Global: inicio/fin de drag
    document.addEventListener('dragstart', (e)=>{
      const cell = e.target.closest('.cell');
      if (!cell || !document.body.classList.contains('edit-mode')) return;
      dragged = cell;
      originSlot = cell.closest('.slot');
      committed = false;
      e.dataTransfer.setData('text/plain', cell.id);
      setTimeout(()=> cell.classList.add('dragging'), 0);
    });

    document.addEventListener('dragend', ()=>{
      const d = document.querySelector('.cell.dragging');
      if (d) d.classList.remove('dragging');
      if (!committed){
        // no hubo drop válido → nada cambia
      }
      dragged = null;
      originSlot = null;
      committed = false;
      padSlots(col);       // por si acaso, garantiza 1 por slot
      recomputeOrders();
    });
  }

  function enableEdit(on){
    document.body.classList.toggle('edit-mode', on);
    document.querySelectorAll('.cell').forEach(c=> c.setAttribute('draggable', on ? 'true' : 'false'));
    updateNumSemUI();
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

    const firstCol = t.querySelector('.sem-col');
    if (firstCol) t.insertBefore(head, firstCol); else t.appendChild(head);
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

  // --- export ---
  function downloadMalla(selector = '.plan') {
    const node = document.querySelector(selector);
    if (!node) return alert('No encontré la malla a exportar');

    const styles = [...document.querySelectorAll('style,link[rel="stylesheet"]')]
      .map(n => n.outerHTML).join('\n');

    const printCSS = `
      <style>
        @media print {
          body { margin: 0 !important; }
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
    setTimeout(()=>{ w.print(); w.close(); }, 50);
  }

  // ---------- init ----------
  document.addEventListener('DOMContentLoaded', ()=>{
    const t = tableEl(); if (!t) return;

    // Estado base desde JSON embebido
    const src = document.getElementById('__courses');
    if (src) window.COURSES_STATE = JSON.parse(src.textContent || '[]');
    else window.COURSES_STATE = [];

    // preparar columnas
    document.querySelectorAll('.table .sem-col').forEach(col=>{
      bindColumn(col);
    });
    updateGridColumns();
    updateNumSemUI();

    // UI
    document.getElementById('edit-toggle')?.addEventListener('change', (e)=> enableEdit(e.target.checked));
    document.getElementById('btn-add-sem')?.addEventListener('click', addSemester);
    document.getElementById('btn-rem-sem')?.addEventListener('click', removeLastSemester);
    document.getElementById('btn-download')?.addEventListener('click', () => downloadMalla('.plan'));
  });
})();
