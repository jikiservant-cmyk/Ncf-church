# MUK CU — Makerere University Christian Union

Site for **Makerere University Christian Union (MUK CU)**, built on a faithful,
self-contained static clone of **[pdnafrica.org](https://www.pdnafrica.org)** —
rebuilt from that site's content, imagery and compiled stylesheet, then rebranded.

> **Rebrand status:** the organisation name is changed throughout (page titles,
> header wordmark, hero, nav, body copy, footer). Still carrying PDN's details:
> the logo artwork, contact emails, social links, postal addresses, tax ID and the
> outbound donate link. Replace those before publishing — see *Notes & caveats*.

No Squarespace runtime, no CDN dependencies, no build step required to view it.

---

## Run it

```bash
node server.js
# → http://localhost:3000
```

Any static file server also works (`python3 -m http.server`, nginx, Netlify, Vercel,
GitHub Pages…). The site is plain HTML/CSS/JS.

## Rebuild the pages

Page copy lives in `tools/content.py`; shared chrome in `tools/layout.py`.

```bash
python3 tools/build.py     # regenerates all 15 .html files + sitemap.xml + robots.txt
```

## Deploying

It's a static folder — drop it on Netlify, Vercel, Cloudflare Pages, GitHub Pages or
any nginx box. Set `SITE_URL` at build time so canonical tags and the sitemap point
at **your** domain:

```bash
SITE_URL=https://your-domain.org python3 tools/build.py
```

Left unset, no canonical tags are emitted and the sitemap uses relative paths — so
the clone never accidentally declares `pdnafrica.org` as canonical and de-indexes
your copy.

| Host | Settings |
|---|---|
| Netlify / Cloudflare | publish directory `.` · no build command (or the one above) |
| Vercel | Framework preset: **Other** · output directory `.` |
| GitHub Pages | push the folder, enable Pages on the branch |
| nginx | `root /path/to/repo; try_files $uri $uri.html $uri/ =404;` |

Set `404.html` as your host's not-found page (Netlify and GitHub Pages pick it up
automatically; `server.js` already serves it locally).

---

## What's here

| | |
|---|---|
| **15 pages** | Home + every program, impact, donate, blog, contact page + styled 404 |
| **65 images** | Original photography pulled from the site's Squarespace CDN |
| **Self-hosted fonts** | No Adobe Fonts / Google Fonts callout — works fully offline |
| **SEO ready** | `sitemap.xml`, `robots.txt`, OG/Twitter tags, optional canonicals |
| **~20 MB** | Everything included, nothing hotlinked |
| **Zero build deps** | No npm install needed to run or deploy |

### Pages

`index` · `pastoral-training` · `youthpastorandemergingleaders` · `impacting-women` ·
`interim-pastoral-ministry` · `accredited-degree-program-partnerships` ·
`cornerstone-university` · `pos-impact` · `lives-impacted` · `mentorship-profiles` ·
`run-across-uganda` · `ways-to-donate` · `contact` · `blog`

Extensionless URLs (`/pastoral-training`) resolve too, matching the original slugs.

---

## Design fidelity

Type ramp, spacing and colours were extracted from the live site's compiled
stylesheet (`pdnafrica.org/site.css`) rather than eyeballed:

| Token | Value from source |
|---|---|
| Display face | `futura-pt` — 700, page title 72px / `-1px` tracking |
| Body face | `proxima-nova` — 400, 15px / 24px line-height |
| Hero description | 24px, 300 weight, uppercase, `.015em` |
| Nav | 13px, 700, uppercase, `1.33px` tracking |
| H1 / H2 / H3 | 45px / 24px / 15px |
| Quote block | 6% padding, 24px display bold |
| Nav panel | `#97a6b4`, slides to 79% width on mobile |
| Block gutter | 34px |

**Fonts:** the original loads Futura PT and Proxima Nova from Adobe Fonts, which
requires a licensed kit. This clone self-hosts **Jost** (a Futura-derived geometric
sans) and **Source Sans 3** under the original family names, so the CSS type ramp is
unchanged and the rendering is very close without a subscription. Swap in the real
licensed `.woff2` files in `assets/fonts/` for a pixel-exact match.

### Behaviour recreated

- Stacked full-bleed index banners with overlay copy and "Scroll Down" cue
- Transparent header that becomes solid on scroll
- Hover dropdown folders on desktop; 79% slide-out panel on mobile
- Sticky section sub-nav with scroll-spy
- Click-to-zoom gallery lightbox (arrow keys + Esc)
- Reveal-on-scroll, reduced-motion aware
- Responsive down to 360px, plus print styles

---

## Structure

```
├── *.html                  15 generated pages (incl. 404.html)
├── sitemap.xml robots.txt  generated SEO files
├── server.js               static server (binds 0.0.0.0, serves styled 404)
├── assets/
│   ├── css/site.css        design system
│   ├── js/site.js          nav, lightbox, scroll-spy
│   ├── fonts/              self-hosted woff2
│   └── img/                65 original photos + derived PDN logos
└── tools/
    ├── build.py            page generator + SEO writer
    ├── content.py          all site copy
    ├── layout.py           head / header / nav / footer helpers
    └── asset_manifest.json provenance: local file → original CDN URL
```

---

## Notes & caveats

- **Donation button** links out to the real `pdnafrica.org/ways-to-donate` page. The
  original processes gifts through tithe.ly; no payment form is embedded here, so no
  money can be collected by this clone by accident.
- **Newsletter form** is front-end only and shows a thank-you state — it does **not**
  store or send anything. The live site's form was itself unconfigured ("needs a
  storage option"). Wire it to your provider (Supabase, Mailchimp, Buttondown…)
  before going live; the submit handler is at the bottom of `assets/js/site.js`.
- **Logo** was recovered from PDN's published mark and separated into transparent
  colour and white knock-out variants (`assets/img/pdn-logo*.png`).
- Two source images (`LIVES.IMPACTED.jpg` at 161×243, and the mentorship portraits at
  ~145px) are low-resolution originals; they're used at natural size rather than
  upscaled into heroes.
- Copy is transcribed verbatim, including a few typos present in the source
  ("Bachelor in Thology" was corrected to "Theology"; wording otherwise untouched).

## Provenance

Content and imagery belong to Pastors Discipleship Network. This is a reproduction
built at the user's request — confirm you have the right to reuse the brand, copy
and photography before publishing it publicly.
