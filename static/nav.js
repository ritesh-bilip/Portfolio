// ── ACTIVE NAV LINK ──
(function(){
  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === page || (page === '' && href === 'index.html')) {
      a.classList.add('active');
    }
  });
})();

// ── HAMBURGER ──
function toggleMenu(){
  document.getElementById('navLinks').classList.toggle('open');
}
document.addEventListener('click', e => {
  if (!e.target.closest('nav')) {
    document.getElementById('navLinks')?.classList.remove('open');
  }
});

// ── CUSTOM CURSOR ──
const _cur  = document.getElementById('cursor');
const _ring = document.getElementById('cursorRing');
if(_cur && _ring){
  document.addEventListener('mousemove', e => {
    _cur.style.left  = e.clientX + 'px';
    _cur.style.top   = e.clientY + 'px';
    setTimeout(() => {
      _ring.style.left = e.clientX + 'px';
      _ring.style.top  = e.clientY + 'px';
    }, 60);
  });
  document.querySelectorAll('a,button,.project-card,.service-card,.social-card,.skill-pill').forEach(el => {
    el.addEventListener('mouseenter', () => {
      _cur.style.transform  = 'translate(-50%,-50%) scale(2.5)';
      _ring.style.transform = 'translate(-50%,-50%) scale(1.5)';
      _ring.style.borderColor = 'var(--gold)';
    });
    el.addEventListener('mouseleave', () => {
      _cur.style.transform  = 'translate(-50%,-50%) scale(1)';
      _ring.style.transform = 'translate(-50%,-50%) scale(1)';
    });
  });
}
