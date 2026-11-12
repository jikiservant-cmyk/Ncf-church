/* MUK CU clone — navigation, index scroll-spy, gallery lightbox, reveal-on-scroll. */
(function () {
  'use strict';

  /* ---------- Sticky header ---------- */
  var header = document.querySelector('.header');
  var banner = document.querySelector('.banner');
  function onScroll() {
    if (!header) return;
    var trigger = banner ? Math.max(banner.offsetHeight - 120, 200) : 120;
    header.classList.toggle('is-stuck', window.scrollY > trigger);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile navigation ---------- */
  var burger = document.querySelector('.burger');
  var scrim = document.querySelector('.scrim');
  var closeBtn = document.querySelector('.mobile-nav__close');
  function setNav(open) {
    document.body.classList.toggle('nav-open', open);
    if (burger) burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (burger) burger.addEventListener('click', function () { setNav(true); });
  if (scrim) scrim.addEventListener('click', function () { setNav(false); });
  if (closeBtn) closeBtn.addEventListener('click', function () { setNav(false); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { setNav(false); closeLightbox(); }
  });
  document.querySelectorAll('.mobile-nav__toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      btn.parentElement.classList.toggle('open');
    });
  });
  document.querySelectorAll('.mobile-nav a').forEach(function (a) {
    a.addEventListener('click', function () { setNav(false); });
  });

  /* ---------- Smooth anchor scrolling with sticky-nav offset ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (!id || id === '#') return;
      var target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      var nav = document.querySelector('.index-nav');
      var offset = nav ? nav.offsetHeight : 0;
      var y = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top: y, behavior: 'smooth' });
      history.replaceState(null, '', id);
    });
  });

  /* ---------- Index nav scroll-spy ---------- */
  var indexLinks = Array.prototype.slice.call(document.querySelectorAll('.index-nav a'));
  if (indexLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    indexLinks.forEach(function (a) {
      var sec = document.querySelector(a.getAttribute('href'));
      if (sec) map[sec.id] = a;
    });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          indexLinks.forEach(function (l) { l.classList.remove('is-active'); });
          if (map[en.target.id]) map[en.target.id].classList.add('is-active');
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) spy.observe(el);
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var revealables = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealables.length) {
    var ro = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); obs.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    revealables.forEach(function (el) { ro.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Gallery lightbox ---------- */
  var lb = document.querySelector('.lightbox');
  var lbImg = lb ? lb.querySelector('img') : null;
  var lbCap = lb ? lb.querySelector('.lightbox__cap') : null;
  var items = [];
  var idx = 0;

  document.querySelectorAll('.gallery').forEach(function (gal) {
    var figs = Array.prototype.slice.call(gal.querySelectorAll('figure'));
    figs.forEach(function (fig, i) {
      fig.addEventListener('click', function () {
        items = figs.map(function (f) {
          var im = f.querySelector('img');
          var cap = f.querySelector('figcaption');
          return { src: im.getAttribute('data-full') || im.src, cap: cap ? cap.textContent : '' };
        });
        idx = i;
        openLightbox();
      });
    });
  });

  function openLightbox() {
    if (!lb || !items.length) return;
    lbImg.src = items[idx].src;
    lbImg.alt = items[idx].cap || '';
    if (lbCap) lbCap.textContent = items[idx].cap || '';
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox() {
    if (!lb) return;
    lb.classList.remove('open');
    document.body.style.overflow = '';
  }
  function step(d) {
    if (!items.length) return;
    idx = (idx + d + items.length) % items.length;
    openLightbox();
  }
  if (lb) {
    lb.querySelector('.lightbox__close').addEventListener('click', closeLightbox);
    lb.querySelector('.lightbox__prev').addEventListener('click', function (e) { e.stopPropagation(); step(-1); });
    lb.querySelector('.lightbox__next').addEventListener('click', function (e) { e.stopPropagation(); step(1); });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target === lbImg) closeLightbox(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'ArrowLeft') step(-1);
      if (e.key === 'ArrowRight') step(1);
    });
  }

  /* ---------- Newsletter (client-side only; no backend wired) ---------- */
  document.querySelectorAll('.form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = form.parentElement.querySelector('.form__ok');
      if (ok) ok.classList.add('show');
      form.reset();
    });
  });

  /* ---------- Footer year ---------- */
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
