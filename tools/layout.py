"""Shared chrome (head, header, nav, footer) for the MUK CU clone."""
import os

SITE = "Makerere University Christian Union"

# Absolute base for canonical tags / sitemap. Set SITE_URL when you deploy, e.g.
#   SITE_URL=https://ncf.church python3 tools/build.py
# Left empty by default so the clone never declares somebody else's domain as
# canonical (which would de-index your copy).
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")

# Site navigation.
NAV = [
    ("About", "/about.html", [
        ("Who We Are", "/about.html"),
        ("Our History", "/history.html"),
        ("Leadership", "/leadership.html"),
        ("Affiliations", "/affiliations.html"),
    ]),
    ("Fellowships", "/fellowships.html", [
        ("Hall Fellowships", "/fellowships.html#halls"),
        ("College Fellowships", "/fellowships.html#colleges"),
        ("Hostel Fellowships", "/fellowships.html#hostels"),
        ("Mission Teams", "/fellowships.html#missions"),
        ("Full CU Structure", "/structure.html"),
    ]),
    ("Ministry", "/discipleship.html", [
        ("Discipleship", "/discipleship.html"),
        ("Evangelism & Missions", "/evangelism.html"),
        ("Praise & Worship", "/worship.html"),
        ("Prayer Altar", "/prayer.html"),
    ]),
    ("Gatherings", "/lunch-hour.html", [
        ("Lunch Hour", "/lunch-hour.html"),
        ("Night of Redemption", "/night-of-redemption.html"),
        ("Events", "/events.html"),
    ]),
    ("Give", "/give.html", []),
    ("News", "/news.html", []),
    ("Contact", "/contact.html", []),
]


def head(title, desc, path="/index.html"):
    full = title if title == SITE else f"{title} — {SITE}"
    slug = "" if path == "/index.html" else path[:-5]
    canonical = (f'<link rel="canonical" href="{SITE_URL}{slug or "/"}">\n'
                 if SITE_URL else "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="/assets/img/muk-chapel-group.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#20242a">
{canonical}<link rel="icon" type="image/png" href="/assets/img/muk-mark.png">
<link rel="apple-touch-icon" href="/assets/img/muk-mark.png">
<link rel="preload" href="/assets/fonts/jost-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/source-sans-3-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body data-page="{path}">
"""


def header(active="/index.html"):
    desktop = []
    for label, href, kids in NAV:
        cls = " is-active" if href == active else ""
        if kids:
            links = "".join(f'<a href="{h}">{t}</a>' for t, h in kids)
            desktop.append(
                f'<div class="nav__item"><a class="nav__link nav__link--caret{cls}" href="{href}">{label}</a>'
                f'<div class="folder">{links}</div></div>'
            )
        else:
            desktop.append(f'<div class="nav__item"><a class="nav__link{cls}" href="{href}">{label}</a></div>')
    desktop.append('<div class="nav__item"><a class="nav__link nav__cta" href="/give.html">Give</a></div>')

    mobile = []
    for label, href, kids in NAV:
        if kids:
            links = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in kids)
            mobile.append(
                f'<li><button class="mobile-nav__toggle" type="button">{label}</button>'
                f'<ul class="sub">{links}</ul></li>'
            )
        else:
            mobile.append(f'<li><a href="{href}">{label}</a></li>')
    mobile.append('<li><a href="/give.html">Give</a></li>')

    return f"""<div class="announcement">
  Theme: Preaching Christ with Love &mdash; Ephesians 4:14&ndash;16
  <a href="/structure.html">Find a fellowship</a>
</div>

<header class="header">
  <div class="header__inner">
    <a class="brand" href="/index.html">
      <img class="brand__mark" src="/assets/img/muk-mark-white.png" alt="MUK CU" width="44" height="53">
      <span class="brand__text">Makerere<br>University<br>Christian Union</span>
    </a>
    <nav class="nav" aria-label="Main navigation">{''.join(desktop)}</nav>
    <button class="burger" type="button" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="scrim"></div>
<nav class="mobile-nav" aria-label="Mobile navigation">
  <button class="mobile-nav__close" type="button" aria-label="Close menu">&times;</button>
  <ul>{''.join(mobile)}</ul>
</nav>
"""


def banner(title, sub, desc, img, short=False, cue=False, actions="", pos="center center", anchor=None):
    """Full-bleed hero matching the source template's stacked index banners."""
    cls = "banner banner--short" if short else "banner"
    aid = f' id="{anchor}"' if anchor else ""
    subhtml = f'<p class="banner__sub">{sub}</p>' if sub else ""
    deschtml = f'<div class="banner__desc">{desc}</div>' if desc else ""
    acthtml = f'<div class="banner__actions">{actions}</div>' if actions else ""
    cuehtml = '<a class="scroll-cue" href="#what-we-do-content">Scroll Down</a>' if cue else ""
    return f"""<section class="{cls}"{aid}>
  <div class="banner__media" style="background-image:url('/assets/img/{img}');background-position:{pos}"></div>
  <div class="banner__inner">
    <h1 class="banner__title">{title}</h1>
    {subhtml}
    {deschtml}
    {acthtml}
  </div>
  {cuehtml}
</section>
"""


def hero_slideshow(slides, cue=True):
    """Home hero: stacked background images that fade out to full black,
    then fade back up with the next image and its own words.

    Each slide is an absolutely-stacked layer (matching the source template's
    stacked full-bleed banners). A black curtain sits above the images and
    below nothing else, so the whole hero blacks out between slides.
    """
    layers, texts = [], []
    for i, (img, title, sub, desc, label, href) in enumerate(slides):
        on = " is-active" if i == 0 else ""
        layers.append(
            f'<div class="hero__bg{on}" data-slide="{i}" '
            f'style="background-image:url(\'/assets/img/{img}\')"></div>')
        subhtml = f'<p class="banner__sub">{sub}</p>' if sub else ""
        texts.append(f"""<div class="hero__text{on}" data-slide="{i}">
      <h1 class="banner__title">{title}</h1>
      {subhtml}
      <div class="banner__desc">{desc}</div>
      <div class="banner__actions"><a class="btn" href="{href}">{label}</a></div>
    </div>""")
    dots = "".join(
        f'<button class="hero__dot{" is-active" if i == 0 else ""}" type="button" '
        f'data-goto="{i}" aria-label="Go to slide {i+1}"></button>'
        for i in range(len(slides)))
    cuehtml = '<a class="scroll-cue" href="#what-we-do-content">Scroll Down</a>' if cue else ""
    return f"""<section class="banner hero" id="what-we-do" data-hero>
  <div class="hero__stack">{''.join(layers)}</div>
  <div class="hero__curtain"></div>
  <div class="banner__inner hero__inner">{''.join(texts)}</div>
  <div class="hero__dots">{dots}</div>
  {cuehtml}
</section>
"""


def band(title, desc, img, tall=False, actions="", pos="center center", anchor_id=None):
    """Full-bleed image pinned to the viewport. Page content scrolls over it."""
    cls = "band band--tall" if tall else "band"
    aid = f' id="{anchor_id}"' if anchor_id else ""
    dh = f'<div class="band__desc">{desc}</div>' if desc else ""
    ah = f'<div class="band__actions">{actions}</div>' if actions else ""
    th = f'<h2 class="band__title">{title}</h2>' if title else ""
    return f"""<section class="{cls}"{aid}>
  <div class="band__bg" style="background-image:url('/assets/img/{img}');background-position:{pos}"></div>
  <div class="band__inner">
    {th}
    {dh}
    {ah}
  </div>
</section>
"""


def gallery(images, cols=3):
    """images: list of (filename, caption)."""
    cls = "gallery" if cols == 3 else f"gallery gallery--{cols}"
    figs = "".join(
        f'<figure><img src="/assets/img/{fn}" alt="{cap}" loading="lazy">'
        + (f"<figcaption>{cap}</figcaption>" if cap else "")
        + "</figure>"
        for fn, cap in images
    )
    return f'<div class="{cls}">{figs}</div>'


def table(headers, rows, caption=None, num_cols=(), index=False, foot=None):
    """Data table matching the site's type scale. num_cols are right-aligned."""
    cap = f"<caption>{caption}</caption>" if caption else ""
    th = []
    if index:
        th.append('<th class="idx" scope="col">No.</th>')
    for i, h in enumerate(headers):
        cls = ' class="num"' if i in num_cols else ""
        th.append(f'<th scope="col"{cls}>{h}</th>')
    body = []
    for n, row in enumerate(rows, 1):
        tds = [f'<td class="idx">{n}</td>'] if index else []
        for i, c in enumerate(row):
            cls = ' class="num"' if i in num_cols else ""
            tds.append(f"<td{cls}>{c}</td>")
        body.append("<tr>" + "".join(tds) + "</tr>")
    tf = ""
    if foot:
        cells = []
        if index:
            cells.append("<td></td>")
        for i, c in enumerate(foot):
            cls = ' class="num"' if i in num_cols else ""
            cells.append(f"<td{cls}>{c}</td>")
        tf = "<tfoot><tr>" + "".join(cells) + "</tr></tfoot>"
    return (f'<div class="table-wrap"><table class="data">{cap}'
            f'<thead><tr>{"".join(th)}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody>{tf}</table></div>')


def meta(items):
    """items: (number, label) — small stat cards."""
    return '<div class="meta-grid">' + "".join(
        f'<div class="meta reveal"><span class="meta__n">{n}</span>'
        f'<span class="meta__l">{l}</span></div>' for n, l in items) + "</div>"


def quote(text, cite=None, plain=False):
    cls = "quote quote--plain" if plain else "quote"
    c = f"<cite>&mdash; {cite}</cite>" if cite else ""
    return f'<blockquote class="{cls}"><p>{text}</p>{c}</blockquote>'


def person(img, name, role, bio):
    paras = "".join(f"<p>{p}</p>" for p in bio)
    return f"""<article class="person reveal">
  <img class="person__photo" src="/assets/img/{img}" alt="{name}" loading="lazy">
  <h3 class="person__name">{name}</h3>
  <p class="person__role">{role}</p>
  <div class="person__bio">{paras}</div>
</article>"""


def footer():
    import content as C
    return f"""<footer class="footer">
  <div class="wrapper">
    <div class="footer__grid">
      <div>
        <div class="footer__brand">
          <img src="/assets/img/muk-mark-white.png" alt="MUK CU logo" width="40" height="48">
          <span>Makerere<br>University<br>Christian Union</span>
        </div>
        <p>{C.TAGLINE}</p>
        <p><strong>Theme:</strong> {C.THEME}<br>{C.THEME_SCRIPTURE}</p>
        <div class="socials">
          <a href="{C.FACEBOOK}" aria-label="Facebook" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
          </a>
          <a href="{C.YOUTUBE}" aria-label="YouTube" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.8-1.8C19.3 5 12 5 12 5s-7.3 0-8.8.5a2.5 2.5 0 0 0-1.8 1.8C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.8 1.8C4.7 19 12 19 12 19s7.3 0 8.8-.5a2.5 2.5 0 0 0 1.8-1.8C23 15.2 23 12 23 12zM9.8 15.3V8.7l6 3.3-6 3.3z"/></svg>
          </a>
          <span class="socials__handle" title="Twitter / X">
            <svg viewBox="0 0 24 24"><path d="M18.9 2H22l-6.8 7.8L22.7 22h-6.3l-4.9-6.4L5.8 22H2.7l7.3-8.3L1.6 2H8l4.6 6.1L18.9 2zm-1.1 18h1.7L7.3 3.8H5.5L17.8 20z"/></svg>
            <span>{C.TWITTER_HANDLE}</span>
          </span>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/about.html">Who We Are</a></li>
          <li><a href="/history.html">Our History</a></li>
          <li><a href="/fellowships.html">Fellowships</a></li>
          <li><a href="/structure.html">CU Structure</a></li>
          <li><a href="/leadership.html">Leadership</a></li>
          <li><a href="/news.html">News</a></li>
          <li><a href="/give.html">Give</a></li>
        </ul>
      </div>
      <div>
        <h4>Gather With Us</h4>
        <p><strong>Main CU Fellowship</strong><br>Tuesdays &amp; Fridays, 12:45 PM</p>
        <p><strong>Prayer Altar</strong><br>Thursdays, 6:00 PM</p>
        <p>St Francis Chapel</p>
        <p>{C.POSTAL}</p>
        <p><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
        <p><a href="/structure.html">Find your fellowship &rarr;</a></p>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> {C.NAME}. Affiliated to FOCUS-Uganda.</span>
      <span>On the hill since {C.FOUNDED}.</span>
    </div>
  </div>
</footer>

<div class="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="lightbox__close" type="button" aria-label="Close">&times;</button>
  <button class="lightbox__nav lightbox__prev" type="button" aria-label="Previous">&#8249;</button>
  <img alt="">
  <button class="lightbox__nav lightbox__next" type="button" aria-label="Next">&#8250;</button>
  <div class="lightbox__cap"></div>
</div>
<script src="/assets/js/site.js"></script>
</body>
</html>"""
