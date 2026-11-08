# Makerere University Christian Union (MUCU) Website

A fully working, responsive static website for **Makerere University Christian Union (MUCU / MukCU)** — a student-led Christian fellowship at Makerere University, Kampala, Uganda.

## Design
Rebuilt using the **studio** design aesthetic (jikiservant-cmyk/studio Next.js church template):
- Dark hero `#2D2B44`, header `#3E3E4E`, magenta accent `#D12E8B`
- Kinetic typography, magnetic buttons, ink-flow text, blur-focus images
- Sticky nav, floating chat button, quick-link cards, dark footer
- Tailwind CSS (via CDN) + vanilla JavaScript — no build step required

## What's included
- `index.html` — Home (hero, intro, vision, quick links)
- `about.html` — Our story, vision, mission, values
- `events.html` — Weekly rhythm + featured events
- `sermons.html` — Ministries (Bible study, prayer, evangelism, worship, leadership)
- `donate.html` — Online giving + bank details
- `contact.html` — Contact details + working contact form
- `css/style.css` — Custom animations & component styles
- `js/main.js` — Mobile nav, magnetic buttons, scroll reveals
- `assets/images/` — Logo + research/studio photos

## Research sources (info used in the site)
- Makerere University Christian Union (MukCU) — Facebook: facebook.com/people/Makerere-University-Christian-UnionMukCU/100064865400507/
- Website: www.mukchristianunion.org
- Phone: +256 777 345125
- Location: Makerere University, Makerere Hill / St Francis, Kampala, Uganda
- Email: info@mukchristianunion.org
- Mission: "Preaching Christ, ministering God's love on campus"
- Founded 1962 by Daniel Kyanda and Bishop Micheal Ssenyimba; part of FOCUS-Uganda

## Run locally
```bash
# from the repo root
python3 -m http.server 8000
# then open http://localhost:8000
```
