/* ==========================================================================
   MUCU — St Francis Chapel Makerere Design Clone
   Interactions: mobile nav, contact form, active nav link
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  initMobileNav();
  initActiveLink();
  initContactForm();
  setCurrentYear();
});

/* ---------- Mobile nav toggle ---------- */
function initMobileNav() {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav-links");
  if (!toggle || !nav) return;

  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open);
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
}

/* ---------- Highlight active nav link ---------- */
function initActiveLink() {
  const links = document.querySelectorAll(".nav-links a[href^='#']");
  const sections = Array.from(links)
    .map((a) => document.querySelector(a.getAttribute("href")))
    .filter(Boolean);
  if (!links.length || !sections.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          links.forEach((a) => a.classList.remove("active"));
          const active = document.querySelector(`.nav-links a[href="#${entry.target.id}"]`);
          if (active) active.classList.add("active");
        }
      });
    },
    { threshold: 0.25, rootMargin: "-80px 0% -60% 0%" }
  );
  sections.forEach((sec) => observer.observe(sec));
}

/* ---------- Contact form ---------- */
function initContactForm() {
  const form = document.getElementById("contactForm");
  if (!form) return;
  const msg = document.getElementById("formMessage");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const btn = form.querySelector(".form-btn");
    const originalText = btn.textContent;
    btn.textContent = "Sending…";
    btn.disabled = true;

    setTimeout(() => {
      btn.textContent = originalText;
      btn.disabled = false;
      form.reset();
      msg.textContent = "Thank you! Your message has been sent. We'll get back to you soon.";
      msg.className = "form-message success";
      setTimeout(() => { msg.style.display = "none"; }, 7000);
    }, 1200);
  });
}

/* ---------- Footer year ---------- */
function setCurrentYear() {
  const el = document.getElementById("year");
  if (el) el.textContent = new Date().getFullYear();
}
