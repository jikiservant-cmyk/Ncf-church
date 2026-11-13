#!/usr/bin/env python3
"""Build the Makerere University Christian Union site.

Design/layout is unchanged from the approved template; only content differs.
Run:  python3 tools/build.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import (head, header, footer, banner, band, hero_slideshow, gallery,
                    quote, person, table, meta, SITE)
import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = {}


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def page(name, title, desc, body, active=None):
    PAGES[name] = head(title, desc, "/" + name) + header(active or "/" + name) + body + footer()


def cards(items):
    """items: (heading, body-html)"""
    return '<div class="cards">' + "".join(
        f'<div class="card reveal"><h3>{h}</h3>{b}</div>' for h, b in items) + "</div>"


def paras(items):
    return "".join(f"<p>{p}</p>" for p in items)


# ---------------------------------------------------------------- HOME
def build_home():
    b = [hero_slideshow(C.SLIDES)]

    b.append("""<nav class="index-nav" aria-label="Section navigation"><div class="index-nav__inner">
  <a href="#what-we-do">Who We Are</a><a href="#story">Our Story</a>
  <a href="#fellowships">Fellowships</a><a href="#gather">Gather With Us</a>
  <a href="#affiliations">Affiliations</a>
</div></nav>""")

    # Who we are
    b.append(f"""<section class="section" id="what-we-do-content"><div class="wrapper">
  <p class="section-heading center">Who We Are</p>
  <h1 class="center" style="max-width:900px;margin:0 auto 30px">An interdenominational fellowship of Christian students at Makerere University.</h1>
  <p class="lead center" style="max-width:780px;margin:0 auto">{C.ABOUT_INTRO}</p>
  {quote('&ldquo;' + C.THEME + '&rdquo;', 'This Year&rsquo;s Theme &middot; ' + C.THEME_SCRIPTURE)}
  {quote('&ldquo;' + C.MISSION + '&rdquo;', 'Our Mission')}
  {paras(C.ABOUT_MORE)}
  {gallery([("cu-full-hall.jpg", "A full hall for the ministry of the word"),
            ("cu-choir.jpg", "The choir"),
            ("cu-chapel-family.jpg", "The fellowship gathered in the chapel")])}
  {quote('&ldquo;' + C.VISION + '&rdquo;', 'Our Vision')}
  {quote('&ldquo;' + C.BELIEF + '&rdquo;', 'What We Believe')}
</div></section>""")

    # Pinned image — content scrolls past it
    b.append(band("One family on the hill", "Gathered in the chapel as brothers and sisters in Christ.",
                  "cu-chapel-family.jpg"))

    # Story
    b.append(banner("Our Story", "On the hill since 1962", "", "muk-freedom-square.jpg",
                    short=True, anchor="story"))
    stats = "".join(
        f'<div class="stat reveal"><span class="stat__num">{n}</span>'
        f'<span class="stat__label">{l}</span></div>' for n, l in C.MILESTONES)
    b.append(f"""<section class="section section--alt" id="story-content"><div class="wrapper">
  <h1 class="center">Six decades on the hill</h1>
  {paras(C.HISTORY)}
  <div class="stats">{stats}</div>
  <p class="center" style="margin-top:34px"><a class="btn btn--dark" href="/history.html">Read the full story</a></p>
</div></section>""")

    # Fellowships
    b.append(banner("Fellowships", "Hall &bull; College &bull; Hostel", C.FELLOWSHIP_INTRO,
                    "muk-chapel-group.jpg", anchor="fellowships",
                    actions='<a class="btn" href="/fellowships.html">Find Your Fellowship</a>'))
    fc = [(h, paras(ps)) for h, ps in C.FELLOWSHIP_TYPES]
    struct_counts = meta([
        (len(C.HALL_FELLOWSHIPS), "Hall Fellowships"),
        (len(C.COLLEGE_FELLOWSHIPS), "College Fellowships"),
        (len(C.HOSTEL_FELLOWSHIPS), "Hostel Fellowships"),
        (len(C.MISSION_FELLOWSHIPS), "Mission Teams"),
    ])
    b.append(f"""<section class="section"><div class="wrapper">
  {struct_counts}
  {cards(fc)}
  <p class="center" style="margin:0 0 40px"><a class="btn btn--dark" href="/structure.html">See The Full CU Structure</a></p>
  {gallery([("cu-sisters.jpg", "Sisters of the fellowship"),
            ("cu-chapel-celebration.jpg", "Celebrating together"),
            ("cu-full-hall.jpg", "The hall filled")])}
</div></section>""")

    b.append(band("Known by name", "In the fellowship a student is prayed for by name.",
                  "cu-sisters.jpg"))

    # Gather
    b.append(banner("Gather With Us", "Through the week", "", "muk-benediction.jpg",
                    short=True, anchor="gather"))
    rows = "".join(
        f'<div class="card reveal"><h3>{n}</h3>'
        f'<p><strong>{d}</strong> &middot; {t}</p><p>{desc}</p></div>'
        for n, d, t, desc in C.WEEKLY)
    b.append(f"""<section class="section section--alt" id="gather-content"><div class="wrapper">
  <h1 class="center">Our weekly rhythm</h1>
  <div class="cards">{rows}</div>
  {gallery([("cu-full-hall.jpg", "A full hall"),
            ("cu-chapel-family.jpg", "Gathered in the chapel"),
            ("cu-celebration.jpg", "Marking the occasion together")])}
  <p class="center" style="margin-top:34px"><a class="btn btn--dark" href="/contact.html">Plan a visit</a></p>
</div></section>""")

    # Night of redemption highlight
    b.append(banner("Night of Redemption", "The whole campus, one night",
                    "The Union&rsquo;s great open gathering at the University Sports Ground &mdash; worship, preaching and an open door for every student.",
                    "cu-openair.jpg", anchor="night",
                    actions='<a class="btn" href="/night-of-redemption.html">Learn More</a>'))

    # Affiliations
    b.append(banner("Affiliations", "We do not walk alone", "", "muk-remarks.jpg",
                    short=True, anchor="affiliations"))
    af = []
    for title, url, ps in C.AFFILIATIONS:
        t = f'<a href="{url}" target="_blank" rel="noopener">{title}</a>' if url else title
        af.append((t, paras(ps)))
    b.append(f"""<section class="section" id="affiliations-content"><div class="wrapper">
  {cards(af)}
  {gallery([("cu-handover.jpg", "Handing over to the next leaders"),
            ("cu-awards.jpg", "Recognising those who have served"),
            ("cu-portrait.jpg", "Serving the fellowship")], cols=3)}
</div></section>""")

    b.append(band("Beyond the hill", "Carrying the gospel to communities outside Kampala.",
                  "cu-mission-outreach.jpg"))

    b.append(f"""<section class="section section--dark center"><div class="wrapper">
  <h1>There is a place for you here</h1>
  <p class="lead" style="max-width:660px;margin:0 auto 34px">Whether you are a fresher finding your feet or a student who has never walked into a fellowship &mdash; come as you are.</p>
  <a class="btn btn--solid" href="/contact.html">Get In Touch</a>
</div></section>""")

    page("index.html", SITE,
         "Makerere University Christian Union — an interdenominational student fellowship preaching Christ and ministering God's love on campus and beyond. On the hill since 1962.",
         "".join(b), active="/index.html")


# ---------------------------------------------------------------- ABOUT
def build_about():
    b = [banner("Who We Are", "About MUK CU", C.TAGLINE, "muk-chapel-group.jpg", short=True)]
    vals = "".join(f"<li>{v}</li>" for v in C.VALUES)
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>About the Union</h1>
  <p class="lead">{C.ABOUT_INTRO}</p>
  {paras(C.ABOUT_MORE)}
  {quote('&ldquo;' + C.THEME + '&rdquo;', 'This Year&rsquo;s Theme &middot; ' + C.THEME_SCRIPTURE)}
  {quote('&ldquo;' + C.THEME + '&rdquo;', 'Theme &middot; ' + C.THEME_SCRIPTURE + ' &middot; ' + C.THEME_BY)}
  {quote('&ldquo;' + C.MISSION + '&rdquo;', 'Our Mission')}
  <h2>Our Vision</h2>
  <p>{C.VISION}</p>
  {quote('&ldquo;' + C.BELIEF + '&rdquo;', 'What We Believe')}
  <h2>Core Values</h2>
  <ul>{vals}</ul>
  <h2>Interdenominational</h2>
  <p>The Union brings together students from many churches and denominations. We do not ask members to leave their congregations; we ask them to walk with fellow believers while they are on the hill.</p>
  {gallery([("cu-chapel-family.jpg", "The fellowship gathered"),
            ("cu-full-hall.jpg", "Under the word"),
            ("cu-choir.jpg", "Leading worship")])}
</div></section>""")
    b.append(band("Come as you are", "There is a place for you in this family.",
                  "cu-chapel-celebration.jpg"))
    page("about.html", "Who We Are",
         "MUK CU is an interdenominational fellowship of Christian students at Makerere University, affiliated to FOCUS-Uganda.", "".join(b))


# ---------------------------------------------------------------- HISTORY
def build_history():
    b = [banner("Our History", "On the hill since 1962", "", "muk-freedom-square.jpg", short=True)]
    stats = "".join(
        f'<div class="stat reveal"><span class="stat__num">{n}</span>'
        f'<span class="stat__label">{l}</span></div>' for n, l in C.MILESTONES)
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>How the Union began</h1>
  {paras(C.HISTORY)}
  {quote('<strong>What began on the Makerere hill sparked the Christian Union movement in Uganda.</strong>', plain=True)}
  <div class="stats">{stats}</div>
  <h2>The founders</h2>
  <p>The Union was started by students including <strong>Daniel Kyanda</strong> and <strong>Michael Ssenyimba</strong>, who later became Bishop Ssenyimba and Vice-Chancellor of Ndejje University.</p>
  <h2>Jubilee</h2>
  <p>In November 2012 the Union gathered alumni and students at Freedom Square on the main campus to celebrate fifty years &mdash; a day of fellowship, testimony and re-union, giving thanks for the countless lives changed through the CU. Sixty years were marked in November 2022.</p>
  {gallery([("muk-freedom-square.jpg", "Freedom Square, main campus"),
            ("muk-chapel-crest.jpg", "St Francis Chapel"),
            ("muk-freshers.jpg", "A new academic year begins")])}
</div></section>""")
    page("history.html", "Our History",
         "Founded in 1962, Makerere University Christian Union sparked the CU movement in Uganda, leading to FOCUS-Uganda in 1972.", "".join(b))


# ---------------------------------------------------------------- FELLOWSHIPS
def build_fellowships():
    b = [banner("Fellowships", "Hall &bull; College &bull; Hostel", C.FELLOWSHIP_INTRO,
                "muk-chapel-group.jpg", short=True)]
    ids = ["halls", "colleges", "hostels", "missions"]
    body = []
    for (h, ps), aid in zip(C.FELLOWSHIP_TYPES, ids):
        body.append(f'<div id="{aid}"><h2>{h}</h2>{ul(ps)}</div>')
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>Where every member belongs</h1>
  <p class="lead">{C.FELLOWSHIP_INTRO}</p>
  {''.join(body)}
  {quote('&ldquo;' + C.VISION + '&rdquo;', 'Our Vision')}
  <p class="center" style="margin:34px 0"><a class="btn btn--dark" href="/structure.html">Full CU Structure &amp; Membership</a></p>
  {gallery([("cu-chapel-family.jpg", "A fellowship gathered"),
            ("cu-sisters.jpg", "Sisters of the fellowship"),
            ("cu-full-hall.jpg", "The wider Union gathered")])}
</div></section>""")
    b.append("""<section class="section section--dark center"><div class="wrapper">
  <h1>Not sure which fellowship fits?</h1>
  <p class="lead" style="max-width:640px;margin:0 auto 34px">Tell us your hall, college or hostel and we will connect you to the gathering nearest you.</p>
  <a class="btn btn--solid" href="/contact.html">Find My Fellowship</a>
</div></section>""")
    page("fellowships.html", "Fellowships",
         "Hall, College and Hostel Fellowships bring together all believers at Makerere University.", "".join(b))


# ---------------------------------------------------------------- MINISTRY PAGES
def ministry_page(slug, title, sub, img, heading, blocks, extra="", gal=None):
    b = [banner(title, sub, "", img, short=True)]
    body = "".join(f"<p>{p}</p>" for p in blocks)
    g = gallery(gal) if gal else ""
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>{heading}</h1>
  {body}
  {extra}
  {g}
</div></section>""")
    return b


def build_discipleship():
    b = ministry_page("discipleship", "Discipleship", "Growing beyond the first decision",
                      "muk-listening.jpg", "Following Jesus for life",
                      C.DISCIPLESHIP,
                      extra=quote('&ldquo;' + C.BELIEF + '&rdquo;', 'What We Believe'),
                      gal=[("cu-full-hall.jpg", "Under the word"),
                           ("cu-chapel-family.jpg", "The fellowship"),
                           ("cu-chapel-celebration.jpg", "Growing together")])
    page("discipleship.html", "Discipleship",
         "Bible study, follow-up of new believers and personal mentoring in the fellowships of MUK CU.", "".join(b))


def build_evangelism():
    b = ministry_page("evangelism", "Evangelism &amp; Missions", "To every soul on campus",
                      "muk-freshers.jpg", "Reaching the campus and beyond",
                      C.EVANGELISM,
                      gal=[("cu-openair.jpg", "Open-air outreach"),
                           ("cu-mission-outreach.jpg", "Sharing the gospel with the children"),
                           ("cu-mission-children.jpg", "With the children on mission")])
    b.append(band("To every soul", "Missions carry the work beyond the hill.",
                  "cu-mission-village.jpg", tall=True))
    b.append(f"""<section class="section"><div class="wrapper">
  <h2>The mission field</h2>
  <p>During recess and vacation terms students travel out in teams &mdash; preaching, serving and visiting homes. These are moments from those trips.</p>
  {gallery([("cu-mission-village.jpg", "Visiting homes in the village"),
            ("cu-mission-joy.jpg", "Joy on the mission road"),
            ("cu-mission-children.jpg", "With the children")])}
</div></section>""")
    page("evangelism.html", "Evangelism & Missions",
         "Personal witness, campus outreach and recess mission teams beyond Kampala.",
         "".join(b))


def build_worship():
    b = ministry_page("worship", "Praise &amp; Worship", "The sound of the Union",
                      "muk-choir.jpg", "Worship at the centre",
                      C.WORSHIP,
                      gal=[("cu-choir.jpg", "The choir"),
                           ("cu-full-hall.jpg", "The Union in worship"),
                           ("cu-sisters.jpg", "Sisters serving")])
    page("worship.html", "Praise & Worship",
         "The choir, praise team and creative ministries of Makerere University Christian Union.",
         "".join(b))


def build_prayer():
    b = ministry_page("prayer", "Prayer Altar", "Where we get our strength",
                      "muk-benediction.jpg", "Intercession for the University",
                      C.PRAYER)
    rows = "".join(
        f'<div class="card reveal"><h3>{n}</h3><p><strong>{d}</strong> &middot; {t}</p><p>{desc}</p></div>'
        for n, d, t, desc in C.WEEKLY if "Prayer" in n)
    b.append(f"""<section class="section section--alt"><div class="wrapper">
  <h2 class="center">When we gather</h2>
  <div class="cards">{rows}</div>
</div></section>""")
    page("prayer.html", "Prayer Altar",
         "Evening intercession for the University, the nation and the lost on campus — Thursdays at 6:00 PM at St Francis Chapel.", "".join(b))


# ---------------------------------------------------------------- GATHERINGS
def build_lunch_hour():
    b = [banner("Lunch Hour", "Tuesdays &amp; Fridays", "The Union gathers in the middle of the day for worship, testimonies and the teaching of the word.",
                "muk-congregation.jpg", short=True)]
    rows = "".join(
        f'<div class="card reveal"><h3>{n}</h3><p><strong>{d}</strong> &middot; {t}</p><p>{desc}</p></div>'
        for n, d, t, desc in C.WEEKLY)
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>Midday on the hill</h1>
  <p class="lead">Lunch Hour is the Union&rsquo;s gathering in the middle of the academic day &mdash; worship, testimonies from members, and the ministry of the word. Visitors are welcomed at every meeting.</p>
  <p>The Main CU Fellowship meets at <strong>St Francis Chapel</strong> at <strong>12:45 PM</strong> on Tuesdays and Fridays, with around 125 students gathering. Guest ministers join the Union through the year. Recordings of past meetings are published on the Union&rsquo;s YouTube channel.</p>
  <div class="cards">{rows}</div>
  {gallery([("cu-full-hall.jpg", "The hall filled"),
            ("cu-chapel-family.jpg", "Gathered in the chapel"),
            ("cu-choir.jpg", "The choir leading")])}
  <p class="center" style="margin-top:34px">
    <a class="btn btn--dark" href="{C.YOUTUBE}" target="_blank" rel="noopener">Watch Past Meetings</a></p>
</div></section>""")
    page("lunch-hour.html", "Lunch Hour",
         "MUK CU Main Fellowship — Tuesdays and Fridays at 12:45 PM at St Francis Chapel. Worship, testimonies and teaching, open to every student.", "".join(b))


def build_night():
    b = [banner("Night of Redemption", "The whole campus, one night", "",
                "muk-congregation.jpg", short=True)]
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>The Union&rsquo;s great open gathering</h1>
  {paras(C.NIGHT_OF_REDEMPTION)}
  {quote('<strong>An open door onto campus for the gospel.</strong>', plain=True)}
  {gallery([("cu-openair.jpg", "Open-air gathering"),
            ("cu-full-hall.jpg", "A full house"),
            ("cu-choir.jpg", "Leading worship")])}
</div></section>""")
    page("night-of-redemption.html", "Night of Redemption",
         "The Makerere Night of Redemption — MUK CU's flagship open-air gathering at the University Sports Ground.", "".join(b))


def build_events():
    b = [banner("Events", "Through the academic year", "", "muk-freshers.jpg", short=True)]
    ev = [(f"{n}<br><small>{when}</small>", f"<p>{d}</p>") for n, when, d in C.EVENTS]
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>What marks the year</h1>
  {cards(ev)}
  <h2>Weekly gatherings</h2>
  <p>The Main CU Fellowship meets Tuesdays and Fridays at 12:45 PM at St Francis Chapel; the prayer altar gathers on Thursdays at 6:00 PM. Fellowship meetings run through the week in the halls, colleges, hostels and mission teams.</p>
  {gallery([("cu-celebration.jpg", "Marking the occasion together"),
            ("cu-chapel-celebration.jpg", "Celebrating in the chapel"),
            ("cu-awards.jpg", "Recognising service"),
            ("cu-evening.jpg", "An evening with the fellowship")], cols=4)}
  <p class="center" style="margin-top:34px"><a class="btn btn--dark" href="/contact.html">Ask About An Event</a></p>
</div></section>""")
    b.append(band("Moments that mark the year", "Fellowship, thanksgiving and celebration.",
                  "cu-celebration.jpg"))
    page("events.html", "Events",
         "Night of Redemption, freshers' outreach, missions teams and alumni gatherings at Makerere University Christian Union.", "".join(b))


# ---------------------------------------------------------------- LEADERSHIP
def build_leadership():
    b = [banner("Leadership", "Serving the fellowship", "", "muk-remarks.jpg", short=True)]
    dk = [(h, f"<p>{d}</p>") for h, d in C.DOCKETS]
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>How the Union is led</h1>
  <p class="lead">{C.LEADERSHIP_INTRO}</p>
  {cards(dk)}
  <h2>Chaplaincy</h2>
  <p>{C.CHAPLAINCY}</p>
  {quote('<strong>Office bearers serve the fellowship; they do not sit above it.</strong>', plain=True)}
  {gallery([("cu-handover.jpg", "Handing over to the next leaders"),
            ("cu-awards.jpg", "Recognising those who have served"),
            ("cu-portrait.jpg", "Serving the fellowship")])}
</div></section>""")
    b.append(band("Servant leadership", "Each generation hands the work to the next.",
                  "cu-handover.jpg"))
    page("leadership.html", "Leadership",
         "The elected student executive, fellowship coordinators and dockets serving Makerere University Christian Union.", "".join(b))


# ---------------------------------------------------------------- AFFILIATIONS
def build_affiliations():
    b = [banner("Affiliations", "We do not walk alone", "", "muk-remarks.jpg", short=True)]
    af = []
    for title, url, ps in C.AFFILIATIONS:
        t = f'<a href="{url}" target="_blank" rel="noopener">{title}</a>' if url else title
        af.append((t, paras(ps)))
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>Partners and family</h1>
  {cards(af)}
  {gallery([("cu-chapel-family.jpg", "Gathered in the chapel"),
            ("cu-awards.jpg", "Serving together"),
            ("cu-handover.jpg", "Continuity of leadership")])}
</div></section>""")
    page("affiliations.html", "Affiliations",
         "MUK CU is affiliated to FOCUS-Uganda and works alongside the Makerere University chaplaincy.", "".join(b))


# ---------------------------------------------------------------- GIVE
def build_give():
    b = [banner("Give", "Partner with the work", C.GIVING_INTRO, "muk-chapel-group.jpg",
                short=True)]
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>Supporting the Union</h1>
  <p class="lead">{C.GIVING_INTRO}</p>
  <h2>What your giving carries</h2>
  {ul(C.GIVING_USES)}
  {quote('<strong>The work is carried by the freewill giving of members, alumni and friends.</strong>', plain=True)}
  <h2>How to give</h2>
  <p>To give towards the work of the Union, please get in touch with the executive through the contact page or speak to a fellowship leader. Giving is received and reported through the Union treasury.</p>
  <p><strong>Alumni</strong> &mdash; if you passed through the CU and would like to support the current generation, we would be glad to hear from you.</p>
  <p class="center" style="margin-top:34px"><a class="btn btn--dark" href="/contact.html">Contact The Union</a></p>
</div></section>""")
    page("give.html", "Give",
         "Support the fellowships, discipleship materials, missions teams and campus gatherings of MUK CU.", "".join(b))


# ---------------------------------------------------------------- NEWS
def build_news():
    b = [banner("News", "From the hill", "", "muk-choir.jpg", short=True)]
    posts = []
    for i, (title, date, img, ps) in enumerate(C.POSTS):
        posts.append(f"""<article class="post reveal" id="post-{i+1}">
  <img class="post__img" src="/assets/img/{img}" alt="{title}" loading="lazy">
  <p class="post__date">{date}</p>
  <h2 class="post__title">{title}</h2>
  {paras(ps)}
</article>""")
    b.append(f"""<section class="section"><div class="wrapper">
  {''.join(posts)}
</div></section>""")
    page("news.html", "News",
         "News and reflections from Makerere University Christian Union — campus events, anniversaries and life in the fellowships.", "".join(b))


# ---------------------------------------------------------------- CONTACT
def build_contact():
    b = [banner("Contact", "Come and see", C.CONTACT_INTRO, "cu-chapel-family.jpg",
                short=True)]
    b.append(f"""<section class="section"><div class="wrapper">
  <div class="contact-grid">
    <div>
      <h1>Get in touch</h1>
      <p class="lead">{C.CONTACT_INTRO}</p>
      <p><strong>Postal address:</strong><br>{C.POSTAL}</p>
      <p><strong>Email:</strong><br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
      <p><strong>Where we meet:</strong><br>St Francis Chapel, Makerere University</p>
      <p><strong>Facebook:</strong><br><a href="{C.FACEBOOK}" target="_blank" rel="noopener">{C.FACEBOOK_NAME}</a></p>
      <p><strong>Twitter / X:</strong><br>{C.TWITTER_HANDLE}</p>
      <p><strong>YouTube:</strong><br><a href="{C.YOUTUBE}" target="_blank" rel="noopener">Watch past meetings</a></p>
    </div>
    <div>
      <h2>Visiting</h2>
      {ul(C.VISIT)}
      <h2>Gather with us</h2>
      {table(["Program", "Time", "Venue"], [(n, t, v) for n, t, v, _ in C.MAIN_PROGRAMS])}
      <p><a href="/structure.html">See all fellowships &rarr;</a></p>
    </div>
  </div>
</div></section>""")
    b.append(f"""<section class="section section--alt center"><div class="wrapper">
  <h1>Stay in touch</h1>
  <p class="lead" style="max-width:620px;margin:0 auto 30px">Get news of gatherings, missions and events on the hill.</p>
  <div style="max-width:520px;margin:0 auto">
    <form class="form" novalidate>
      <input type="email" placeholder="Email Address" aria-label="Email Address" required>
      <button class="btn btn--solid" type="submit">Sign Up</button>
    </form>
    <p class="form__note">We respect your privacy.</p>
    <p class="form__ok">Thank you!</p>
  </div>
</div></section>""")
    page("contact.html", "Contact",
         "Find MUK CU at St Francis Chapel, Makerere University, Kampala. Fellowship Tuesdays and Fridays at 12:45 PM; prayer altar Thursdays at 6:00 PM.", "".join(b))


# ---------------------------------------------------------------- 404
def build_404():
    b = [banner("Page Not Found", "404",
                "The page you were looking for has moved or no longer exists.",
                "muk-freedom-square.jpg", short=True,
                actions='<a class="btn" href="/index.html">Return Home</a>')]
    b.append("""<section class="section"><div class="wrapper center">
  <h1>Let's get you back on track</h1>
  <div class="cards" style="text-align:left">
    <div class="card"><h3>Who We Are</h3><p>The Union, its mission and its story.</p><p><a href="/about.html">Read more &rarr;</a></p></div>
    <div class="card"><h3>Fellowships</h3><p>Find the gathering nearest your hall, college or hostel.</p><p><a href="/fellowships.html">Read more &rarr;</a></p></div>
    <div class="card"><h3>Contact</h3><p>Plan a visit or ask a question.</p><p><a href="/contact.html">Read more &rarr;</a></p></div>
  </div>
</div></section>""")
    page("404.html", "Page Not Found", "The page you were looking for could not be found.",
         "".join(b), active="/404.html")



# ---------------------------------------------------------------- CU STRUCTURE
def build_structure():
    b = [banner("CU Structure", "Fellowships of the Union", C.STRUCTURE_NOTE,
                "cu-full-hall.jpg", short=True)]

    counts = meta([
        (len(C.HALL_FELLOWSHIPS), "Hall Fellowships"),
        (len(C.COLLEGE_FELLOWSHIPS), "College Fellowships"),
        (len(C.HOSTEL_FELLOWSHIPS), "Hostel Fellowships"),
        (len(C.MISSION_FELLOWSHIPS), "Mission Teams"),
        (C.CHURCH_BASED_COUNT, "Church-Based"),
        (C.SUMMARY_TOTAL, "Total In Structure"),
    ])

    b.append(f"""<section class="section"><div class="wrapper">
  <h1>The structure of the Union</h1>
  <p class="lead">The Christian Union brings together believers across the University through its hall, college, hostel and mission team fellowships.</p>
  {counts}
  <h2>Main CU Programs</h2>
  {table(["Program", "Meeting Time", "Venue", "Students"], C.MAIN_PROGRAMS, num_cols=(3,))}
</div></section>""")

    b.append(band("Hall Fellowships", "Five fellowships in the halls of residence.",
                  "cu-chapel-family.jpg"))
    b.append(f"""<section class="section"><div class="wrapper">
  <h2>Hall Fellowships</h2>
  {meta([(len(C.HALL_FELLOWSHIPS), "Fellowships"), (C.HALL_AVG, "Average Students"),
         (sum(n for _, n in C.HALL_FELLOWSHIPS), "Students Total")])}
  {table(["Fellowship Name", "Students"], C.HALL_FELLOWSHIPS, num_cols=(1,), index=True)}
</div></section>""")

    b.append(f"""<section class="section section--alt"><div class="wrapper">
  <h2>College Fellowships</h2>
  {meta([(len(C.COLLEGE_FELLOWSHIPS), "Fellowships"), (C.COLLEGE_AVG, "Average Students"),
         (sum(n for _, n in C.COLLEGE_FELLOWSHIPS), "Students Total")])}
  {table(["Fellowship Name", "Students"], C.COLLEGE_FELLOWSHIPS, num_cols=(1,), index=True)}
</div></section>""")

    b.append(band("Hostel Fellowships", "Taking the Union to students off campus.",
                  "cu-sisters.jpg"))
    b.append(f"""<section class="section"><div class="wrapper">
  <h2>Hostel Fellowships</h2>
  {meta([(len(C.HOSTEL_FELLOWSHIPS), "Fellowships"), (C.HOSTEL_AVG, "Average Students"),
         (sum(n for _, n in C.HOSTEL_FELLOWSHIPS), "Students Total")])}
  {table(["Fellowship Name", "Students"], C.HOSTEL_FELLOWSHIPS, num_cols=(1,), index=True)}
</div></section>""")

    b.append(f"""<section class="section section--alt"><div class="wrapper">
  <h2>Mission Team Fellowships</h2>
  {meta([(len(C.MISSION_FELLOWSHIPS), "Teams"), (C.MISSION_AVG, "Average Students"),
         (sum(n for _, n in C.MISSION_FELLOWSHIPS), "Students Total")])}
  {table(["Fellowship / Team Name", "Students"], C.MISSION_FELLOWSHIPS, num_cols=(1,), index=True)}
</div></section>""")

    b.append(band("Beyond the hill", "Mission teams carry the gospel across Uganda.",
                  "cu-mission-joy.jpg"))
    b.append(f"""<section class="section"><div class="wrapper">
  <h2>Church-Based Fellowships</h2>
  {meta([(C.CHURCH_BASED_COUNT, "Fellowships"), (C.CHURCH_BASED_AVG, "Average Students")])}
  <p class="table-note">{C.CHURCH_BASED_NOTE}</p>

  <h2>Independent Fellowships</h2>
  <p>Not affiliated with the CU &mdash; shown for reference only.</p>
  {meta([(len(C.INDEPENDENT_FELLOWSHIPS), "Fellowships"), (C.INDEPENDENT_AVG, "Average Students")])}
  {table(["Fellowship Name", "Students"], C.INDEPENDENT_FELLOWSHIPS, num_cols=(1,), index=True)}
  <p class="table-note">{C.INDEPENDENT_NOTE}</p>
</div></section>""")

    b.append(f"""<section class="section section--alt"><div class="wrapper">
  <h2>Summary</h2>
  {table(["Category", "Number of Fellowships"], C.SUMMARY, num_cols=(1,),
         foot=["Total", C.SUMMARY_TOTAL])}
  <p class="table-note">{C.SUMMARY_NOTE}</p>
  {quote('&ldquo;' + C.THEME + '&rdquo;', C.THEME_SCRIPTURE)}
</div></section>""")

    b.append("""<section class="section section--dark center"><div class="wrapper">
  <h1>Find your fellowship</h1>
  <p class="lead" style="max-width:640px;margin:0 auto 34px">Tell us your hall, college or hostel and we will connect you to the gathering nearest you.</p>
  <a class="btn btn--solid" href="/contact.html">Get In Touch</a>
</div></section>""")
    page("structure.html", "CU Structure",
         "The fellowships of Makerere University Christian Union — 5 hall, 11 college, "
         "6 hostel and 10 mission team fellowships, with meeting times and venues.",
         "".join(b))


# ---------------------------------------------------------------- SEO
def write_seo_files():
    from layout import SITE_URL
    base = SITE_URL
    urls = []
    for name in PAGES:
        if name == "404.html":
            continue
        loc = "/" if name == "index.html" else "/" + name[:-5]
        priority = "1.0" if name == "index.html" else "0.7"
        urls.append(f"  <url><loc>{base}{loc}</loc>"
                    f"<changefreq>monthly</changefreq><priority>{priority}</priority></url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(sitemap)
    robots = ("User-agent: *\nAllow: /\nDisallow: /404.html\nDisallow: /tools/\n")
    if base:
        robots += f"\nSitemap: {base}/sitemap.xml\n"
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(robots)
    print(f"  {'sitemap.xml':46s} {len(urls):>7} urls")


def main():
    for fn in (build_home, build_about, build_history, build_fellowships,
               build_discipleship, build_evangelism, build_worship, build_prayer,
               build_lunch_hour, build_night, build_events, build_leadership,
               build_affiliations, build_give, build_news, build_contact, build_structure,
               build_404):
        fn()
    for name, html in PAGES.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"  {name:46s} {len(html):>7,} bytes")
    write_seo_files()
    print(f"\nBuilt {len(PAGES)} pages.")


if __name__ == "__main__":
    main()
