(function(){
  const ROMAN = ["","I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"];
  const SWAP_EDGE = 0.10; // 10% superior/inferior del slot para activar swap preview

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

  // Mueve .cell “sueltas” o mal ubicadas dentro de su slot (por número .num)
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

    strayCells.forEach(c=>{
      let p = parseInt(c.querySelector('.num')?.textContent || '0', 10);
      if (!(p >= 1 && p <= N) || slots[p-1].querySelector('.cell')){
        p = findEmpty(1) || 1;
      }
      slots[p-1].appendChild(c);
    });

    // 3) normalizar números visibles (no tocar si estás en edición)
    const editOn = document.body.classList.contains('edit-mode');
    slots.forEach((s,i)=>{
      const c = s.querySelector(':scope > .cell');
      if (c){
        const num = c.querySelector('.num');
        if (num && !editOn) num.textContent = String(i+1);
      }
    });
  }

  // Escribir semester/order en COURSES_STATE y actualizar numeritos (fuera de edición)
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
          data[idx].semester = sem;  // slot real (se guarda)
          data[idx].order = i+1;     // slot real (se guarda)
        }
        // numerito solo fuera de edición
        const num = cell.querySelector('.num');
        if (num && !editOn) num.textContent = String(i+1);
      });
    });
    updateNumSemUI(); // asegura visual correcto tras cualquier cambio
  }

  // ----- UI: alterna .num vs .sem-origin durante edición -----
  function updateNumSemUI() {
    const editOn = document.body.classList.contains('edit-mode');
    document.querySelectorAll('.table .cell').forEach(cell => {
      const num = cell.querySelector('.num');
      const sem = cell.querySelector('.sem-origin');
      if (sem) {
        // usa el dato del HTML si existe
        const hv = cell.dataset.homeSem || sem.textContent || '';
        sem.textContent = hv;
      }
      if (num) num.style.display = editOn ? 'none'  : 'inline';
      if (sem) sem.style.display = editOn ? 'inline': 'none';
    });
  }

  // ---------- DnD con slots y swap preview ----------
  function bindColumn(col){
    ensureSlots(col);
    padSlots(col);

    let dragged = null;
    let originSlot = null;          // slot inicial del dragged
    let swapState = null;           // {withCell, withSlot, origOtherSlot}
    let committed = false;          // se soltó con drop válido

    // helpers swap
    function doSwapPreview(targetSlot){
      if (!dragged || !targetSlot) return;
      const other = targetSlot.querySelector(':scope > .cell');
      if (!other || other === dragged) return;

      const fromSlot = dragged.closest('.slot');
      if (!fromSlot || fromSlot === targetSlot) return;

      // guarda estado para posible revert
      swapState = {
        withCell: other,
        withSlot: targetSlot,
        origDraggedSlot: originSlot || fromSlot,
        origOtherSlot: other.closest('.slot')
      };

      // intercambio visual
      fromSlot.appendChild(other);
      targetSlot.appendChild(dragged);
      updateNumSemUI(); // mantiene UI coherente
    }

    function revertSwapPreview(){
      if (!swapState) return;
      const { withCell, origDraggedSlot, origOtherSlot } = swapState;
      if (withCell && origOtherSlot) origOtherSlot.appendChild(withCell);
      if (dragged && origDraggedSlot) origDraggedSlot.appendChild(dragged);
      swapState = null;
    }

    // dragover: permitir drop; si el slot está ocupado, activar swap preview
    col.addEventListener('dragover', (e)=>{
      if (!document.body.classList.contains('edit-mode')) return;

      const slot = e.target.closest('.slot');
      if (!slot || !col.contains(slot)) return;

      e.preventDefault(); // habilita drop en cualquier caso

      const occupied = !!slot.querySelector(':scope > .cell');
      if (!occupied){
        slot.classList.add('drop-ok');
        return;
      }
      // si está ocupado, detectar si puntero entra a borde superior/inferior
      const r = slot.getBoundingClientRect();
      const y = e.clientY - r.top;
      const h = r.height;
      const nearTop = y <= h * SWAP_EDGE;
      const nearBottom = y >= h * (1 - SWAP_EDGE);

      if (nearTop || nearBottom){
        if (!dragged) return;
        doSwapPreview(slot); // intercambia temporalmente
      }
    });

    col.addEventListener('dragleave', (e)=>{
      const slot = e.target.closest('.slot');
      slot?.classList.remove('drop-ok');
    });

    // drop: consolidar donde se suelte
    col.addEventListener('drop', (e)=>{
      e.preventDefault();
      committed = true;

      const slot = e.target.closest('.slot');
      if (!slot) return;

      slot.classList.remove('drop-ok');

      // si no hay cell (slot vacío), simplemente colócalo
      if (!slot.querySelector(':scope > .cell')){
        if (dragged) slot.appendChild(dragged);
      } else {
        // si está ocupado y no hicimos preview, colócalo aquí desplazando el otro hacia el origen
        if (dragged && !swapState){
          const other = slot.querySelector(':scope > .cell');
          const from = dragged.closest('.slot');
          if (other && from){
            from.appendChild(other);
            slot.appendChild(dragged);
          }
        }
        // si había preview, ya quedó intercambiado; limpiamos estado
      }
      if (dragged) dragged.classList.remove('dragging');
      dragged = null;
      swapState = null;
      recomputeOrders(); // actualiza semester/order y numeritos
    });

    // listeners globales para iniciar/terminar drag
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

      // si NO se consolidó con drop, revierte el preview
      if (!committed) revertSwapPreview();

      dragged = null;
      originSlot = null;
      committed = false;
      recomputeOrders();   // sincroniza estado real/visual
    });
  }

  function enableEdit(on){
    document.body.classList.toggle('edit-mode', on);
    document.querySelectorAll('.cell').forEach(c=> c.setAttribute('draggable', on ? 'true' : 'false'));
    updateNumSemUI(); // <-- alterna num/semestre original
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
    if (src) window.COURSES_STATE = JSON.parse(src.textContent || '[]);
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
