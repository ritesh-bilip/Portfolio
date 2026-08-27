// ── ACTIVE NAV LINK ──
(function () {
  const page = location.pathname.replace(/\/+$/, "") || "/";
  const hash = location.hash || "#home";
  document.querySelectorAll(".nav-links a").forEach((a) => {
    const link = new URL(a.href, location.origin);
    const href = link.pathname.replace(/\/+$/, "") || "/";
    const sameHomeSection =
      page === "/" && href === "/" && (link.hash || "#home") === hash;
    const sameRoute = page !== "/" && href === page;
    if (sameHomeSection || sameRoute) {
      a.classList.add("active");
    }
  });
})();

// ── HAMBURGER ──
function toggleMenu() {
  const navLinks = document.getElementById("navLinks");
  const hamburger = document.querySelector(".hamburger");
  const isOpen = navLinks.classList.toggle("open");
  hamburger?.setAttribute("aria-expanded", String(isOpen));
}
document.addEventListener("click", (e) => {
  if (!e.target.closest("nav")) {
    document.getElementById("navLinks")?.classList.remove("open");
    document
      .querySelector(".hamburger")
      ?.setAttribute("aria-expanded", "false");
  }
});

// ── CUSTOM CURSOR ──
const _cur = document.getElementById("cursor");
const _ring = document.getElementById("cursorRing");
if (_cur && _ring) {
  document.addEventListener("mousemove", (e) => {
    _cur.style.left = e.clientX + "px";
    _cur.style.top = e.clientY + "px";
    setTimeout(() => {
      _ring.style.left = e.clientX + "px";
      _ring.style.top = e.clientY + "px";
    }, 60);
  });
  document
    .querySelectorAll(
      "a,button,.project-card,.service-card,.social-card,.skill-pill",
    )
    .forEach((el) => {
      el.addEventListener("mouseenter", () => {
        _cur.style.transform = "translate(-50%,-50%) scale(2.5)";
        _ring.style.transform = "translate(-50%,-50%) scale(1.5)";
        _ring.style.borderColor = "var(--gold)";
      });
      el.addEventListener("mouseleave", () => {
        _cur.style.transform = "translate(-50%,-50%) scale(1)";
        _ring.style.transform = "translate(-50%,-50%) scale(1)";
      });
    });
}

// Give the hero object a restrained depth response without a 3D dependency.
const tiltScene = document.querySelector("[data-tilt]");
if (
  tiltScene &&
  !window.matchMedia("(prefers-reduced-motion: reduce)").matches
) {
  tiltScene.addEventListener("pointermove", (event) => {
    const bounds = tiltScene.getBoundingClientRect();
    const x = (event.clientX - bounds.left) / bounds.width - 0.5;
    const y = (event.clientY - bounds.top) / bounds.height - 0.5;
    tiltScene.style.transform = `rotateX(${y * -8}deg) rotateY(${x * 10}deg)`;
  });
  tiltScene.addEventListener("pointerleave", () => {
    tiltScene.style.transform = "rotateX(0deg) rotateY(0deg)";
  });
}
