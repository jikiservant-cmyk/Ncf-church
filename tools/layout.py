"""Shared chrome (head, header, nav, footer) for the MUK CU clone."""
import os

SITE = "Makerere University Christian Union"

# Absolute base for canonical tags / sitemap. Set SITE_URL when you deploy, e.g.
#   SITE_URL=https://ncf.church python3 tools/build.py
# Left empty by default so the clone never declares somebody else's domain as
# canonical (which would de-index your copy).
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")

# Navigation mirrors the source site's folder structure.
NAV = [
    ("About", "/index.html", [
        ("What We Do", "/index.html#what-we-do"),
        ("Richmond's Story", "/index.html#richmond"),
        ("Story Highlights", "/index.html#story"),
        ("Brighter", "/index.html#brighter"),
        ("Strategic Partners", "/index.html#strategic-partners"),
        ("Board Members", "/index.html#board-members"),
        ("Positive Impact", "/pos-impact.html"),
        ("Lives Impacted", "/lives-impacted.html"),
        ("Mentorship Profiles", "/mentorship-profiles.html"),
        ("Run Across Uganda", "/run-across-uganda.html"),
    ]),
    ("MUK CU Program", "/pastoral-training.html", [
        ("Pastoral Training", "/pastoral-training.html"),
        ("Youth & Emerging Leaders", "/youthpastorandemergingleaders.html"),
        ("Impacting Women", "/impacting-women.html"),
        ("Interim Pastoral Ministry", "/interim-pastoral-ministry.html"),
        ("Accredited Degrees", "/accredited-degree-program-partnerships.html"),
        ("Cornerstone University", "/cornerstone-university.html"),
    ]),
    ("Ways To Donate", "/ways-to-donate.html", []),
    ("Blog", "/blog.html", []),
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
<meta property="og:image" content="/assets/img/img_8436.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#20242a">
{canonical}<link rel="icon" type="image/png" href="/assets/img/pdn-logo.png">
<link rel="apple-touch-icon" href="/assets/img/pdn-logo.png">
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
    desktop.append('<div class="nav__item"><a class="nav__link nav__cta" href="/ways-to-donate.html">Donate</a></div>')

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
    mobile.append('<li><a href="/ways-to-donate.html">Ways To Donate</a></li>')

    return f"""<div class="announcement">
  Training &amp; equipping African pastors to study, practice &amp; teach God's Word accurately.
  <a href="/ways-to-donate.html">Support the work</a>
</div>

<header class="header">
  <div class="header__inner">
    <a class="brand" href="/index.html">
      <img class="brand__mark" src="/assets/img/pdn-logo-white.png" alt="MUK CU logo" width="44" height="53">
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
    return """<footer class="footer">
  <div class="wrapper">
    <div class="footer__grid">
      <div>
        <div class="footer__brand">
          <img src="/assets/img/pdn-logo-white.png" alt="MUK CU logo" width="40" height="48">
          <span>Pastors<br>Discipleship Network</span>
        </div>
        <p>Training &amp; equipping African pastors to study, practice &amp; teach God's Word accurately.</p>
        <div class="socials">
          <a href="https://www.facebook.com/PDNAfrica/" aria-label="Facebook" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
          </a>
          <a href="https://instagram.com/pdnafrica" aria-label="Instagram" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.2A6.6 6.6 0 1 0 18.6 12 6.6 6.6 0 0 0 12 5.4zm0 10.9A4.3 4.3 0 1 1 16.3 12 4.3 4.3 0 0 1 12 16.3zm6.9-11.2a1.5 1.5 0 1 1-1.5-1.5 1.5 1.5 0 0 1 1.5 1.5z"/></svg>
          </a>
          <a href="https://www.youtube.com/channel/UC6y_XIXd-Dxb9zWGIh4CHrQ" aria-label="YouTube" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.8-1.8C19.3 5 12 5 12 5s-7.3 0-8.8.5a2.5 2.5 0 0 0-1.8 1.8C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.8 1.8C4.7 19 12 19 12 19s7.3 0 8.8-.5a2.5 2.5 0 0 0 1.8-1.8C23 15.2 23 12 23 12zM9.8 15.3V8.7l6 3.3-6 3.3z"/></svg>
          </a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/index.html">About MUK CU</a></li>
          <li><a href="/pastoral-training.html">Pastoral Training</a></li>
          <li><a href="/impacting-women.html">Impacting Women</a></li>
          <li><a href="/cornerstone-university.html">Cornerstone University</a></li>
          <li><a href="/blog.html">Blog</a></li>
          <li><a href="/ways-to-donate.html">Ways To Donate</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <p><strong>MUK CU USA</strong><br>C/O Eden Bridge Foundation<br>909 Eden Rd, Lancaster, PA 17601<br>
        <a href="tel:+17175608270">(717) 560-8270</a></p>
        <p><strong>MUK CU Uganda Ltd</strong><br>Plot 2312 &amp; 67 Bweyogerere, Kazinga<br>Kira, Wakiso District, Uganda</p>
        <p><a href="mailto:info@pdnafrica.org">info@pdnafrica.org</a></p>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> Makerere University Christian Union. A 501(c)(3) public charity &middot; Tax ID 27-2014552.</span>
      <span>Integrity &middot; Christ-centeredness &middot; Institutional Excellence &middot; Service</span>
    </div>
  </div>
</footer>

<div class="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="lightbox__close" type="button" aria-label="Close">&times;</button>
  <button class="lightbox__nav lightbox__prev" type="button" aria-label="Previous">&#8249;</button>
  <img src="" alt="">
  <button class="lightbox__nav lightbox__next" type="button" aria-label="Next">&#8250;</button>
  <div class="lightbox__cap"></div>
</div>

<script src="/assets/js/site.js"></script>
</body>
</html>
"""
