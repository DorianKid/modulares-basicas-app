// app/files/grid_functions.js
(function(){
  function collectApproved(){
    const ids = [];
    document.querySelectorAll('.cell input[type="checkbox"]').forEach(chk=>{
      if (chk.checked) ids.push(chk.id.replace('done-',''));
    });
    return { approved: ids };
  }

  function copyJSON(){
    const data = JSON.stringify(collectApproved());
    navigator.clipboard.writeText(data).then(()=>{
      alert("Progreso copiado al portapapeles ✅\n\n" + data);
    });
  }

  function isApproved(id){
    const el = document.getElementById('done-' + id);
    return !!(el && el.checked);
  }

  function hasAllPrereqs(cell){
    const list = (cell.dataset.prereqs || '').split(',').filter(Boolean);
    if (!list.length) return true;
    return list.every(isApproved);
  }

  function enforceLocks(){
    document.querySelectorAll('.cell[data-prereqs]').forEach(cell => {
      const chk = cell.querySelector('input[type="checkbox"]');
      if (chk && !hasAllPrereqs(cell)) chk.checked = false;
    });
  }

  function toggleViewOnly(ev){
    const on = ev.target.checked;
    document.body.classList.toggle('view-only', on);
  }

  document.addEventListener('DOMContentLoaded', ()=>{
    const btn = document.getElementById('btn-copy');
    if (btn) btn.addEventListener('click', copyJSON);

    const solo = document.getElementById('view-only');
    if (solo) solo.addEventListener('change', toggleViewOnly);

    enforceLocks();
    document.addEventListener('change', (ev)=>{
      if (ev.target.matches('.cell input[type="checkbox"]')) enforceLocks();
    });
  });
})();
