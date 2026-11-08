/* ==========================================================================
   MUCU — Studio Design Interactions
   Mobile nav, magnetic buttons, scroll reveals, kinetic typography
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  initMobileNav();
  initMagneticButtons();
  initScrollReveal();
  initKineticHeadlines();
  initBlurFocus();
  setCurrentYear();
});

/* ---------- Mobile nav toggle ---------- */
function initMobileNav() {
  const toggle = document.querySelector(".menu-toggle");
  const menu = document.querySelector(".mobile-menu");
  if (!toggle || !menu) return;

  toggle.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open);
  });

  menu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      menu.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
}

/* ---------- Magnetic buttons ---------- */
function initMagneticButtons() {
  document.querySelectorAll(".magnetic-wrap").forEach((wrap) => {
    const btn = wrap.querySelector(".magnetic-btn");
    if (!btn) return;

    let x = 0, y = 0;
    wrap.addEventListener("mousemove", (e) => {
      const rect = wrap.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dx = (e.clientX - cx) / (rect.width / 20);
      const dy = (e.clientY - cy) / (rect.height / 20);
      x = dx; y = dy;
      wrap.style.transform = `translate3d(${dx}px, ${dy}px, 0)`;
    });
    wrap.addEventListener("mouseleave", () => {
      x = 0; y = 0;
      wrap.style.transform = `translate3d(0, 0, 0)`;
    });
  });
}

/* ---------- Scroll reveal ---------- */
function initScrollReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
}

/* ---------- Kinetic headlines (reveal on scroll) ---------- */
function initKineticHeadlines() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.querySelectorAll(".kinetic-line").forEach((line, i) => {
            line.style.animationDelay = `${i * 0.15}s`;
            line.classList.add("kinetic-visible");
          });
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );
  document.querySelectorAll(".kinetic-wrap").forEach((el) => observer.observe(el));
}

/* ---------- Blur-focus images ---------- */
function initBlurFocus() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("focused");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );
  document.querySelectorAll(".vision-img").forEach((img) => observer.observe(img));
}

/* ---------- Active nav link on scroll ---------- */
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-links a, .mobile-menu a");
if (sections.length && navLinks.length) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((a) => {
            a.classList.remove("active");
            if (a.getAttribute("href") === `#${entry.target.id}`) {
              a.classList.add("active");
            }
          });
        }
      });
    },
    { threshold: 0.25, rootMargin: "-100px 0% -60% 0%" }
  );
  sections.forEach((s) => observer.observe(s));
}

/* ---------- Footer year ---------- */
function setCurrentYear() {
  const el = document.getElementById("year");
  if (el) el.textContent = new Date().getFullYear();
}
