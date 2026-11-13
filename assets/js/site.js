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


  /* ---------- Home hero: fade to black, swap, fade back up ---------- */
  var hero = document.querySelector('[data-hero]');
  if (hero) {
    var bgs    = [].slice.call(hero.querySelectorAll('.hero__bg'));
    var texts  = [].slice.call(hero.querySelectorAll('.hero__text'));
    var dots   = [].slice.call(hero.querySelectorAll('.hero__dot'));
    var count  = bgs.length;
    var idx    = 0;
    var busy   = false;
    var timer  = null;
    var HOLD   = 5200;   // time a slide is readable
    var BLACK  = 850;    // must match .hero__curtain transition
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Warm the cache so the next image never flashes in half-loaded.
    bgs.forEach(function (el) {
      var m = /url\(['"]?([^'")]+)['"]?\)/.exec(el.style.backgroundImage);
      if (m) { var im = new Image(); im.src = m[1]; }
    });

    function paint(n) {
      bgs.forEach(function (el, i)   { el.classList.toggle('is-active', i === n); });
      texts.forEach(function (el, i) { el.classList.toggle('is-active', i === n); });
      dots.forEach(function (el, i)  { el.classList.toggle('is-active', i === n); });
    }

    function go(n) {
      if (busy || n === idx || !count) return;
      busy = true;
      clearTimeout(timer);
      // 1. curtain rises to full black
      hero.classList.add('is-blacked');
      // 2. once opaque, swap image + words underneath
      setTimeout(function () {
        idx = n;
        paint(idx);
        // 3. curtain falls, revealing the new slide
        setTimeout(function () {
          hero.classList.remove('is-blacked');
          setTimeout(function () { busy = false; }, reduce ? 0 : BLACK);
          schedule();
        }, 60);
      }, reduce ? 0 : BLACK);
    }

    function next() { go((idx + 1) % count); }

    function schedule() {
      clearTimeout(timer);
      if (reduce || count < 2) return;
      timer = setTimeout(next, HOLD);
    }

    dots.forEach(function (d) {
      d.addEventListener('click', function () {
        go(parseInt(d.getAttribute('data-goto'), 10));
      });
    });

    // Pause while the tab is hidden so it doesn't burn cycles in background.
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) clearTimeout(timer); else schedule();
    });

    // Pause on hover / focus so a slide can be read or its button clicked.
    hero.addEventListener('mouseenter', function () { clearTimeout(timer); });
    hero.addEventListener('mouseleave', schedule);
    hero.addEventListener('focusin',  function () { clearTimeout(timer); });
    hero.addEventListener('focusout', schedule);

    paint(0);
    schedule();
  }


  /* ---------- Pinned backgrounds ----------
     Desktop browsers honour background-attachment:fixed, so the image is
     tied to the viewport and content scrolls past it. iOS Safari ignores
     that property, so we detect it and drive the layer with a transform
     on scroll instead — same visual result. */
  (function pinnedBackgrounds() {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) return;

    var iOS = /iP(hone|ad|od)/.test(navigator.userAgent) ||
              (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    if (!iOS) return;   // native fixed attachment already works

    document.documentElement.classList.add('no-bg-fixed');
    var layers = [].slice.call(document.querySelectorAll('.band__bg, .banner__media'));
    if (!layers.length) return;

    var ticking = false;
    function update() {
      ticking = false;
      var vh = window.innerHeight;
      layers.forEach(function (el) {
        var host = el.parentElement;
        var r = host.getBoundingClientRect();
        if (r.bottom < -vh || r.top > vh * 2) return;   // off-screen, skip
        // Counter-scroll the layer so it appears nailed to the viewport.
        el.style.transform = 'translate3d(0,' + (-r.top) + 'px,0)';
        el.style.height = vh + 'px';
      });
    }
    function onScroll() {
      if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  })();

  /* ---------- Footer year ---------- */
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
