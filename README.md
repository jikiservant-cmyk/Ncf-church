# MUK CU — Makerere University Christian Union

Website for **Makerere University Christian Union (MUK CU)** — an interdenominational
fellowship of Christian students at Makerere University, Kampala. On the hill since 1962.

The visual design is carried over unchanged from the approved template; the content,
imagery and navigation are MUK CU's own.

---

## Run it

```bash
node server.js          # → http://localhost:3000
```

Any static host works (Netlify, Vercel, Cloudflare Pages, GitHub Pages, nginx).
No npm install and no build step are needed just to view it.

## Rebuild

```bash
python3 tools/build.py                      # 17 pages + sitemap.xml + robots.txt
SITE_URL=https://your-domain.org python3 tools/build.py   # with canonical URLs
```

Copy lives in `tools/content.py`; shared chrome in `tools/layout.py`.

---

## Pages

`index` · `about` · `history` · `fellowships` · `discipleship` · `evangelism` ·
`worship` · `prayer` · `lunch-hour` · `night-of-redemption` · `events` ·
`leadership` · `affiliations` · `give` · `news` · `contact` · `404`

Extensionless URLs (`/fellowships`) resolve, matching the original routing behaviour.

---

## Home hero slideshow

The homepage hero cycles four slides. Between each one the **whole hero fades to
solid black**, the next image and its own words are swapped underneath, then the
black fades back up — the transition requested, rather than a plain cross-fade.

```
readable 5.2s  →  fade to black 0.85s  →  swap  →  fade up 0.85s  →  repeat
```

- Images are **stacked as absolute background layers**, matching the source
  template's stacked full-bleed banners.
- A `.hero__curtain` sits above the imagery and below the copy.
- Each slide carries its **own title, description and button**.
- Dot navigation, pause on hover/focus, pause when the tab is hidden.
- Images are preloaded so the next slide never appears half-loaded.
- `prefers-reduced-motion` disables the animation entirely.

## Pinned background images

Images are **tied to the viewport** — the page content scrolls across them rather
than carrying them along. This applies to every interior banner and to the
full-bleed `band()` sections placed between content blocks.

- `background-attachment: fixed` does the work in browsers that support it, at
  **all screen widths**.
- iOS Safari ignores that property, so `site.js` detects iOS and counter-scrolls
  the layer with a `translate3d` on `requestAnimationFrame` — same pinned result.
- `prefers-reduced-motion` and print stylesheets release the pin.

The home hero slideshow is separate and was left unchanged.

## Photography

The gallery and band images are the Union's **own photographs**, supplied directly:
chapel gatherings, the choir, a full hall, leadership handover and awards,
celebrations, and mission trips (open-air outreach, village visits, children).
15 photos, kept at their native resolution — no upscaling. Per-file provenance in
`tools/cu_image_sources.json`.

Campus/chapel context shots on the hero and history pages come from Makerere
University News and Uganda Jubilee Network (`tools/muk_image_sources.json`).

Captions are descriptive only — no names or roles have been invented for anyone
pictured.

---

## Design

Type ramp, spacing and colours are unchanged from the approved design system:

| Token | Value |
|---|---|
| Display face | Futura PT → **Jost** (self-hosted) |
| Body face | Proxima Nova → **Source Sans 3** (self-hosted) |
| Hero title | 700 / 72px / `-1px` tracking |
| Body | 400 / 15px / 24px line-height |
| Accent | `#7ba05b` |
| Nav panel | `#97a6b4` |

Fonts are self-hosted, so the site works fully offline. Drop licensed `.woff2`
files into `assets/fonts/` for a pixel-exact match to the original faces.

---

## Content sources

All factual claims about the Union come from public records:

| Claim | Source |
|---|---|
| Founded 1962 by Daniel Kyanda and Michael Ssenyimba; sparked Uganda's CU movement; FOCUS-Uganda formed 1972; Golden Jubilee at Freedom Square, Nov 2012 | [Uganda Jubilee Network](https://www.ugandajubilee.org/makerere-university-christian-union-celebrates-jubilee/) |
| 60 years celebrated Nov 2022; "a fellowship under FOCUS" | [FOCUS-Uganda events](https://focusuganda.org/) |
| Vision: brings together all believers through Hall, College and Hostel Fellowships | MUK CU's own [YouTube channel](https://www.youtube.com/@MAKEREREUNIVERSITYCHRISTIANUNI) description |
| Mission: "Preaching Christ, ministering God's love on campus"; location St Francis; phone | [Public directory listing](https://yellow.place/en/makerere-university-christian-union-mukcu-kampala-uganda) |
| Lunch Hour Tue/Fri; prayer altar Tue/Thu 6–8 PM | Announced by the MC at [MUK CU Lunch Hour, 29 Oct 2024](https://www.youtube.com/watch?v=7qfjjkquCYM) |
| Night of Redemption at the Sports Ground; Pr. Robert Kayanja chief celebrant, March 2025 | [Makerere University News](https://news.mak.ac.ug/2025/03/courtesy-visit-by-pr-kayanja/) |
| Chaplaincy at St Francis Chapel; Rev. Canon Onesimus Asiimwe | [Makerere University News](https://news.mak.ac.ug/2020/01/1st-joint-christian-fellowship-outlines-theme-for-2020/) |

Photography is from Makerere University News and the Uganda Jubilee Network —
real campus, chapel and fellowship photographs. Per-file provenance is recorded in
`tools/muk_image_sources.json`.

---

## Before you publish

- [ ] **Logo** — `assets/img/muk-mark*.png` is a simple typographic placeholder
      (cross + open book), not the Union's official mark. Replace with the real logo.
- [ ] **Verify the details** — meeting days/times, phone number and the docket list
      are drawn from public sources and may be out of date. Confirm with the
      current executive.
- [ ] **Executive names** — the leadership page lists dockets, not office holders,
      because current names aren't published. Add them if you want them shown.
- [ ] **Giving** — no payment details are published; the page directs givers to
      contact the executive. Add official mobile-money/bank details if desired.
- [ ] **Newsletter** — front-end only; it shows a thank-you but stores nothing.
      The handler is at the bottom of `assets/js/site.js`.
- [ ] **Photo rights** — the Union's own photos were supplied directly. The hero and
      history pages still use press photographs from Makerere University News and
      Uganda Jubilee Network; confirm permission for those before public launch.
- [ ] **Names/captions** — photos are captioned descriptively. Send names and dockets
      if you want people identified (e.g. the leadership portrait and handover shots).

## Structure

```
├── *.html                  17 generated pages
├── sitemap.xml robots.txt  generated SEO files
├── server.js               static server (0.0.0.0, styled 404)
├── assets/
│   ├── css/site.css        design system + hero slideshow
│   ├── js/site.js          nav, hero cycle, lightbox, scroll-spy
│   ├── fonts/              self-hosted woff2
│   └── img/                26 files — the Union's photos, campus shots, wordmark
└── tools/
    ├── build.py            page generator
    ├── content.py          all MUK CU copy
    ├── layout.py           head / header / hero / footer
    ├── muk_image_sources.json   press photo provenance
    └── cu_image_sources.json    supplied photo provenance
```
