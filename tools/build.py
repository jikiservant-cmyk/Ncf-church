#!/usr/bin/env python3
"""Generate the static MUK CU clone. Run: python3 tools/build.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import head, header, footer, banner, gallery, quote, person, SITE
import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = {}


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def page(name, title, desc, body, active=None):
    PAGES[name] = head(title, desc, "/" + name) + header(active or "/" + name) + body + footer()


# ---------------------------------------------------------------- HOME
def build_home():
    b = []
    b.append(banner(
        "Makerere University Christian Union", "What We Do",
        "Training &amp; Equipping African Pastors To Study, Practice &amp; Teach God's Word Accurately",
        "img_8436.jpg", cue=True, anchor="what-we-do",
        actions='<a class="btn" href="/ways-to-donate.html">Partner With Us</a>'))

    b.append("""<nav class="index-nav" aria-label="Section navigation"><div class="index-nav__inner">
  <a href="#what-we-do">What We Do</a><a href="#richmond">Richmond's Story</a>
  <a href="#story">Story Highlights</a><a href="#brighter">Brighter</a>
  <a href="#strategic-partners">Strategic Partners</a><a href="#board-members">Board Members</a>
</div></nav>""")

    # About
    b.append(f"""<section class="section" id="what-we-do-content"><div class="wrapper">
  <p class="section-heading center">About MUK CU</p>
  <h1 class="center" style="max-width:860px;margin:0 auto 30px">MUK CU &mdash; Makerere University Christian Union &mdash; is a ministry that equips pastors and strengthens the African church.</h1>
  <p class="lead center" style="max-width:760px;margin:0 auto">{C.ABOUT_INTRO}</p>
  {quote('&ldquo;' + C.MISSION + '&rdquo;', 'Our Mission Statement')}
  <h2>Our Reality</h2>
  {ul(C.REALITY)}
  <p><strong>How is this reality affecting the spread of the Gospel and the African people?</strong></p>
  <p>We are seeing</p>
  {ul(C.REALITY_EFFECTS)}
  <p><strong>Specific identified causes of the above problem:</strong></p>
  {ul(C.REALITY_CAUSES)}
  {gallery([("preceptministries_2016.sas.jpg", "Inductive Bible study training"),
            ("baylor-6.jpg", "Baylor University partnership"),
            ("baylor-10.jpg", "Pastors equipped with resources")])}
  <h2>The Future</h2>
  <p>During the next three years, we will continue to build on this momentum and expand our reach and resources. Our goals are to:</p>
  {ul(C.FUTURE_GOALS)}
  <p>What&rsquo;s more, we plan to network and partner with other individuals and organizations whose programs complement or share a thread with our efforts. And we have already embarked on an exciting project to build a University &ndash; <a href="/cornerstone-university.html">Cornerstone University</a>.</p>
  <p>Ultimately, we aim to take pastoral training and education to new heights, to strengthen the church in Africa. By God&rsquo;s grace, and with all of our partners working together, this vision can become a reality.</p>
  {quote('&ldquo;' + C.VISION + '&rdquo;', 'Our Vision')}
  <h2>Progress</h2>
  <p>{C.PROGRESS_1}</p>
  <p>{C.PROGRESS_2}</p>
  <p>Our efforts are making a difference:</p>
  {ul(C.PROGRESS_RESULTS)}
  {quote('&ldquo;' + C.VALUES + '&rdquo;', 'Our Core Values')}
</div></section>""")

    # Richmond
    b.append(banner("Richmond's Story", "Our Founder, Richmond Wandera", "",
                    "photo-2023-03-01-11-32-29-7.jpg", short=True, anchor="richmond"))
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>Richmond's Story</h1>
  <h3>A Child among &ldquo;The Least of These&rdquo;</h3>
  {quote('<strong>Richmond Wandera was rescued from poverty in Jesus&rsquo; Name.</strong>', plain=True)}
  {''.join(f'<p>{p}</p>' for p in C.RICHMOND)}
</div></section>""")

    # Story highlights
    b.append(banner("Story", "Highlights", "", "pastorstraining.jpg", short=True, anchor="story"))
    stats = "".join(
        f'<div class="stat reveal"><span class="stat__num">{n}</span><span class="stat__label">{l}</span></div>'
        for n, l in C.HIGHLIGHTS)
    b.append(f"""<section class="section section--alt"><div class="wrapper">
  <h1 class="center">Highlights</h1>
  <div class="stats">{stats}</div>
</div></section>""")

    # Brighter
    b.append(banner("Brighter", "A Brighter Future For Women",
                    "MUK CU continues to touch the lives of pastor&rsquo;s wives &amp; women leaders &mdash; through Jesus Christ's transforming power &mdash; with training in discipleship, inductive Bible study methods, business &amp; life skills, and small scale enterprises.<br><br><em>The Word Of God &bull; Business Skills For Self-Reliance &bull; Bible Training &bull; Self Empowerment</em>",
                    "31230475_2076384292388854_3428454053439340544_o.jpg", anchor="brighter",
                    actions='<a class="btn" href="/impacting-women.html">Learn More</a>'))

    # Partners
    b.append(banner("Strategic Partners", "Strategic Partners", "", "lbc_cohort1_sas.jpg",
                    short=True, anchor="strategic-partners"))
    logos = [("cau-logo.png", "Church Answers University"), ("ctn-logo.jpg", "Church Transformation Network"),
             ("ignite-2023.png", "Ignite Mission Convention"), ("re-forma-logo.png", "Re-Forma")]
    logohtml = "".join(f'<img src="/assets/img/{f}" alt="{a}" loading="lazy">' for f, a in logos)
    plist = []
    for title, url, paras in C.PARTNERS:
        t = f'<a href="{url}" target="_blank" rel="noopener">{title}</a>' if url else title
        plist.append(f'<div class="card reveal"><h3>{t}</h3>' + "".join(f"<p>{p}</p>" for p in paras) + "</div>")
    b.append(f"""<section class="section"><div class="wrapper">
  <div class="logos">{logohtml}</div>
  <div class="cards">{''.join(plist)}</div>
</div></section>""")

    # Board
    b.append(banner("Board Members", "MUK CU USA Board Members", "", "img_3066.jpg",
                    short=True, anchor="board-members"))
    people = "".join(person(*p) for p in C.BOARD)
    b.append(f"""<section class="section section--alt"><div class="wrapper">
  <h1 class="center">MUK CU USA Board Members</h1>
  <div class="people">{people}</div>
</div></section>""")

    b.append("""<section class="section section--dark center"><div class="wrapper">
  <h1>Join us in deepening the African church</h1>
  <p class="lead" style="max-width:640px;margin:0 auto 34px">Your partnership equips pastors who will never attend Bible school &mdash; and strengthens the congregations they serve.</p>
  <a class="btn btn--solid" href="/ways-to-donate.html">Ways To Donate</a>
</div></section>""")

    page("index.html", SITE,
         "MUK CU trains and equips African pastors to study, practice and teach God's Word accurately.",
         "".join(b), active="/index.html")


# ------------------------------------------------------- PASTORAL TRAINING
def build_pastoral():
    b = [banner("Pastoral Training", "Pastoral Training", "", "img_8733.jpg", short=True)]
    comp = "".join(
        f'<div class="card reveal"><span class="card__num">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(C.COMPETENCIES, 1))
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>Addressing A Desperate Need For Bible Education</h1>
  <p>Over 85% of pastors in East Africa have not had access to theological training. Many pastors have expressed to us a desperate need for Bible education, while others do not feel they need training because they have made it thus far without it.</p>
  <p>MUK CU currently focuses on both sets of pastors;</p>
  <ul>
    <li>Those who feel stuck in their ministry. While they are passionate to divide God&rsquo;s Word accurately, they are not fully equipped to do so.</li>
    <li>Pastors who feel they don&rsquo;t need further training. This perspective has led to a dangerous attitude and mind-set and is destroying the church.</li>
  </ul>
  <h3>Our theological training comes in three convenient packages:</h3>
  <div class="cards">
    <div class="card reveal"><span class="card__num">01</span><h3>Seminary - Lite Courses</h3><p>12 weeks</p></div>
    <div class="card reveal"><span class="card__num">02</span><h3>Rooted In The Word Pastors Conferences</h3><p>3 days</p></div>
    <div class="card reveal"><span class="card__num">03</span><h3>Inductive Bible Study Classes</h3><p>Three levels</p></div>
  </div>
  <p style="margin-top:40px">These programs provide the pastors with both theology training and practical pastoral skills. Through programs like our &ldquo;Rooted in the Word&rdquo; conferences, church leaders are empowered to discover and apply Christ-centered principles. MUK CU is excited to witness the growth in church performance due to the correct handling and communication of God&rsquo;s Word.</p>
  <p>These programs also help pastors live a balanced and fruitful life leading to healthy families and congregations.</p>
  <p>Currently, over 4,800 pastors are benefiting from our training programs and we hope that in the next five years, we will be serving 30,000 churches across East Africa.</p>
  <h2>Key Competencies</h2>
  <div class="cards">{comp}</div>
  <p style="margin-top:40px">Video Testimonies of the impact on this Training on Pastors can be found on our <a href="https://www.youtube.com/channel/UC6y_XIXd-Dxb9zWGIh4CHrQ" target="_blank" rel="noopener">YouTube channel</a>.</p>
  {gallery([("richmond2.jpg", "Richmond Wandera teaching pastors"),
            ("teachingmaterial.jpg", "Teaching material distributed to pastors"),
            ("pastor-with-resources-2.jpg", "A pastor with new study resources"),
            ("pastor-with-resources.jpg", "Resourcing pastors across East Africa"),
            ("pastorstraining2.jpg", "Rooted in the Word conference"),
            ("pastor-with-book.jpg", "Equipped with God's Word"),
            ("business.training.jpg", "Business skills training for pastors"),
            ("img_9861.jpg", "Partner ministries"),
            ("whatsapp-image-2018-05-10-at-2.27.28-am.jpg", "Winchester Center training")], cols=3)}
</div></section>""")
    page("pastoral-training.html", "PASTORAL TRAINING",
         "Over 85% of pastors in East Africa have not had access to theological training. MUK CU addresses this desperate need.",
         "".join(b))


# ------------------------------------------------------------ YOUTH
def build_youth():
    b = [banner("Youth &amp; Emerging Leaders Training", "Youth Pastor Training",
                "Youth Pastors learn ministry techniques and activities to engage young people as well as ways to sustain themselves and their ministries.",
                "youthpastortraining4.jpg", short=True)]
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>About Youth Pastor Training</h1>
  <p>This program includes youth pastor training camps (3-4 days) where youth pastors are taught about theology, leadership, youth counselling, youth ministry, discipleship, and business skills while in a camp/natural setting. While many senior pastors have received no theological training, youth pastors are even worse off. Uganda is one of the youngest nations with over 80% of the population under the age of 30 and yet the ones put in place to lead these young people have not been led themselves. They learn ministry techniques and activities to engage young people as well as ways to sustain themselves and their ministries.</p>
  <p>There are also different youth pastor cohorts around the city of Kampala that meet monthly to discuss challenges and issues found in youth ministry. They are facilitated by MUK CU to go over different topics and ideas through these small discussion groups.</p>
  <hr class="divider">
  {gallery([("youthpastortraining5.jpg", "Youth pastor training camp"),
            ("youthpastortraining1.jpg", "Emerging leaders in training"),
            ("youthpastortraining2.jpg", "Youth ministry cohort"),
            ("youthpastortraining4.jpg", "Equipping the next generation")], cols=2)}
</div></section>""")
    page("youthpastorandemergingleaders.html", "YOUTH & EMERGING LEADERS TRAINING",
         "Youth pastor training camps equipping young leaders across Uganda in theology, leadership and discipleship.",
         "".join(b))


# ------------------------------------------------------ IMPACTING WOMEN
def build_women():
    b = [banner("Pastors' Spouses and Women of Influence Training", "Impacting Women", "",
                "31265215_2076383715722245_3300757120881786880_o.jpg", short=True)]
    b.append(f"""<section class="section"><div class="wrapper">
  <p class="lead"><strong>The women's ministry began in 2010</strong> after great need was seen in the pastor&rsquo;s household, highlighting the holistic needs the wives face. Today, the need continues as many pastors struggle in understanding their responsibility to their families: some have their priorities in the wrong place &ndash; with their ministry coming first at all times - while others completely ignore their financial obligations to their family. Often, pastors are not in a place where they can provide even the basic needs of their home. Therefore, most pastors&rsquo; wives benefit from business skills training in order to contribute to the financial needs of the household.</p>
  {quote('&ldquo;...many pastors&rsquo; wives lack biblical training and suffer from low self-worth&rdquo;')}
  <p>What is more, many pastors&rsquo; wives lack biblical training and suffer from low self-worth, and for these reasons feel they can not contribute as they should in the work of ministry. MUK CU&rsquo;s women&rsquo;s ministry was established in response to these needs and we continue to seek to touch the lives of pastor&rsquo;s wives and women leaders with the transforming power of Jesus Christ through trainings in discipleship, business and life skills.</p>
  <div class="split" style="margin-top:44px">
    <div>
      <h3 style="margin-top:0">Biblical &amp; Ministry Training</h3>
      <ul>
        <li>Foundational theology (NT and OT Survey)</li>
        <li>Women in Ministry</li>
        <li>Women in Leadership</li>
        <li>The Role of the Pastors Wife in Ministry Today</li>
        <li>Funding Your Mission</li>
      </ul>
    </div>
    <div>
      <h3 style="margin-top:0">Practical &amp; Business Skills</h3>
      <ul>
        <li>Inductive Bible study methods training: 15 women.</li>
        <li>Business Skills and Life Skills training: 100 women.</li>
        <li>Soap Making Training</li>
        <li>Snack making Training.</li>
        <li>Mushroom Growing and Marketing.</li>
        <li>Bakery skills using firewood.</li>
      </ul>
    </div>
  </div>
  <hr class="divider">
  <h1>Two Models Have Been Developed To Train Pastors&rsquo; Wives &amp; Women Leaders</h1>
  <h3>(1) IGA - Income Generating Activities Model</h3>
  <p>The focus of our IGA training for women is to equip pastor's wives and women leaders with basic business skills for self-reliance. The training educates women in how to best take advantage of resources at their disposal.</p>
  <p><strong>Key activities include: poultry rearing, mushroom growing, kitchen gardening, piggery, tailoring lessons, crafts making, as well as cooking/baking lessons.</strong></p>
  <h3>(2) BCS - Biblical, Cultural &amp; Self-view Model</h3>
  <p><strong>Biblical:</strong> The MUK CU Women Ministry trains pastor&rsquo;s wives and women leaders in <em>Discipleship</em> and <em>Inductive Bible Study method</em> with the objective of supporting the women to know Christ and minister effectively to others within their churches and communities.</p>
  <div class="split" style="margin:40px 0">
    <div class="split__media"><img src="/assets/img/18055952_1649009261793028_6108037501281470649_o.jpg" alt="Women's training" loading="lazy"></div>
    <div>
      <p><strong>Cultural:</strong> <em>Cultural view correction</em> program tackles what African culture teaches about women. Some of these beliefs create a self-defeating image for women. Many times cultural beliefs and practices hinder women from participating in church thus limiting the extent to which the woman can serve or offer their skills. The MUK CU trainings focus on boosting the self-worth of women by how they view themselves in the light of the Word of God and their identity in Christ.</p>
      <p><strong>Self-view:</strong> The Self-view training enables women to function confidently and completely without looking down on themselves and other people. Low self-esteem can lead to many self-degrading patterns, such as disregarding personal rights, depression, failure to reach full potential, or tolerating abusive situations and relationships. MUK CU seeks to address all these needs through biblically-based training.</p>
    </div>
  </div>
  {gallery([("whatsapp-image-2023-04-11-at-12.11.50-pm.jpg", "Women's empowerment training"),
            ("whatsapp-image-2023-04-11-at-12.11.12-pm_1_.jpg", "Business skills for self-reliance"),
            ("whatsapp-image-2023-04-11-at-12.11.12-pm.jpg", "Pastors' wives in discipleship training")])}
</div></section>""")
    page("impacting-women.html", "Impacting Women",
         "MUK CU trains pastors' spouses and women of influence in discipleship, business and life skills.",
         "".join(b))


# ------------------------------------------------------------- IPM
def build_ipm():
    b = [banner("Interim Pastoral Ministry", "Interim Pastoral Ministry",
                "Temporary pastors who strengthen churches during pastoral transition for greater effectiveness.",
                "whatsapp-image-2023-04-11-at-11.48.51-am.jpg", short=True)]
    stages = [("Stage 1", "Come to terms with the church&rsquo;s history."),
              ("Stage 2", "Assess church health."),
              ("Stage 3", "Facilitate Action."),
              ("Stage 4", "Lead strategic planning"),
              ("Stage 5", "Coach pastoral search team")]
    st = "".join(f'<div class="card reveal"><span class="card__num">{n}</span><p>{d}</p></div>' for n, d in stages)
    b.append(f"""<section class="section"><div class="wrapper">
  <p class="lead">Makerere University Christian Union&rsquo;s Interim Pastor Ministries provides temporary pastors to strengthen churches during pastoral transition for greater effectiveness.</p>
  <p>MUK CU&rsquo;s IPM pastors are trained to build up churches in crisis to guarantee their continuity and prepare them for their new pastor and their next season of ministry. Our training process of our interim pastors is intentional, designed to produce interim pastors that affirm the strengths of the churches they are placed in while identifying what&rsquo;s necessary to move forward so that they are prepared for optimal kingdom effectiveness.</p>
  <h2>Our IPM roadmap is comprised of 5 stages</h2>
  <div class="cards">{st}</div>
  <p style="margin-top:40px">This process involves forming a Transition Team, typically comprised of existing leadership as well as other emerging leaders and key workers. This process will help improve your church&rsquo;s health, effectiveness, and ability to secure a pastor who will have a long and effective ministry with you.</p>
  <p>IPM helps churches identify where they&rsquo;ve been and help them make choices to move them towards where they want to go. Their primary goal is to help move a church to a point where it&rsquo;s now ready to receive a new pastor. And sometimes that means helping churches heal trouble spots that they&rsquo;ve struggled with. They create space and opportunity for that healing to happen.</p>
  <p>Their pastors are well trained, and they understand that leading a church through a transition and into the future is a unique process. With IPM you&rsquo;re going to get somebody that is called and enthusiastic about the uniqueness of interim ministry. They&rsquo;re a healing agent.</p>
  {quote('Interim Pastor Ministries was a breath of fresh air. We were without a pastor for a total of two years. The first year, we had a different person speak every Sunday. The second year, we decided that our church needed consistency. Our interim pastor was extremely helpful with guiding the leadership team, as well as providing the stability we so needed.')}
  <p>By the grace of God and with the diligent training offered by Pr. Rick and Lucy Foster of CO, USA, MUK CU interim pastors have been found to be:</p>
  <div class="cards">
    <div class="card reveal"><span class="card__num">01</span><h3>Competent</h3><p>Trained &amp; Experienced</p></div>
    <div class="card reveal"><span class="card__num">02</span><h3>Caring</h3><p>Skilled at Pastoral Care &amp; Listening</p></div>
    <div class="card reveal"><span class="card__num">03</span><h3>Intentional</h3><p>Consultative in How they Guide Churches</p></div>
  </div>
  {gallery([("whatsapp-image-2023-04-11-at-11.48.51-am_1_.jpg", "Interim pastors in training"),
            ("whatsapp-image-2023-04-11-at-11.48.51-am.jpg", "IPM cohort"),
            ("whatsapp-image-2023-04-11-at-11.50.16-am.jpg", "Interim pastoral ministry")])}
</div></section>""")
    page("interim-pastoral-ministry.html", "INTERIM PASTORAL MINISTRY",
         "MUK CU's Interim Pastor Ministries provides temporary pastors to strengthen churches in transition.",
         "".join(b))


# --------------------------------------------------- ACCREDITED DEGREES
def build_degrees():
    b = [banner("Accredited Degree Program Partnerships", "Accredited Degree Program Partnerships", "",
                "whatsapp-image-2023-04-11-at-12.04.30-pm_1_.jpg", short=True)]
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>Lancaster Seminary and Bible College</h1>
  <p>The Master of Arts in Contextualized Pastoral Ministry Degree is a fully accredited M.A. degree through Lancaster Bible College|Capital Seminary &amp; Graduate School in the USA, in partnership with the Makerere University Christian Union (MUK CU) in Kampala, Uganda.</p>
  <p><strong>The Program&rsquo;s Mission:</strong> This program seeks to prepare African church pastors and leaders to utilize their unique gifts both personally and professionally for holistic ministry in a variety of African contexts through academic rigor (head), spiritual formation (heart), and professional ministry experience (hands).</p>
  <p>This program is a rigorous degree that demands each student&rsquo;s commitment and sacrifice for 2 years. Only students who can make the weekly commitment for 2 years can enter the program. The program expects the student to spend 21-22 hours of academic engagement per week during classes.</p>
  <p>This is an online program, utilizing the latest in 21st century educational technology. This makes the program flexible and mobile, allowing the students to do their work remotely from their home, office, church, or while traveling.</p>
  <ul>
    <li>Computer literacy required to start the program (the program does not teach computer literacy)</li>
    <li>This is a 2-year program, comprising 14 classes and 40 credits.</li>
    <li>Each class is 7 weeks long with a 1 or 2 week break in-between classes.</li>
    <li>A new cohort of 44 students starts in May of each year.</li>
  </ul>
  <hr class="divider">
  <h1>Church Answers University</h1>
  <p>Church Answers University is equipping church leaders by providing affordable, attainable, practical ministry training and education for ministry in today's world.</p>
  <p>Through the partnership with MUK CU, Church Answers University endeavors to equip African pastors with a certified diploma education that they can in turn, impact other leaders and communities as well by spreading the gospel from their communities and around the continent.</p>
  <p>Currently MUK CU through Church Answers University offers 25 scholarships in a Diploma in Christian Ministry or a Diploma in Discipleship for Women. The program is a year long. The application and interview process starts in November to December. Classes run from January to December.</p>
  {gallery([("whatsapp-image-2023-04-11-at-12.04.30-pm_1_.jpg", "Degree program cohort"),
            ("whatsapp-image-2023-04-11-at-12.04.30-pm.jpg", "Lancaster Bible College partnership"),
            ("whatsapp-image-2023-04-11-at-11.50.45-am.jpg", "Accredited training"),
            ("whatsapp-image-2023-04-11-at-2.54.05-pm.jpg", "Graduating pastors")], cols=2)}
</div></section>""")
    page("accredited-degree-program-partnerships.html", "ACCREDITED DEGREE PROGRAM PARTNERSHIPS",
         "Fully accredited ministry degrees through Lancaster Bible College and Church Answers University.",
         "".join(b))


# --------------------------------------------------- CORNERSTONE
def build_cornerstone():
    b = [banner("Cornerstone University", "Cornerstone University", "",
                "whatsapp-image-2023-04-11-at-9.19.10-am.jpg", short=True)]
    programs = ["Bachelor in Theology", "Diploma in Theology", "Bachelor of Christian Ministry",
                "Diploma in Christian Ministry", "Bachelor of Business Administration",
                "Diploma in Business Administration", "Bachelor of Information Technology",
                "Diploma of Information Technology"]
    prog = "".join(f'<div class="card reveal"><h3 style="margin:0">{p}</h3></div>' for p in programs)
    b.append(f"""<section class="section"><div class="wrapper">
  <figure style="margin:0 0 44px"><img src="/assets/img/whatsapp-image-2023-04-11-at-9.19.11-am.jpg" alt="Cornerstone University master plan" loading="lazy"></figure>
  <h3>Mission:</h3>
  <p class="lead">Cornerstone University exists to equip critical and creative servant leaders who will employ a Christian worldview for community transformation in all facets of life.</p>
  <h3>Ownership:</h3>
  <p>Proposed Cornerstone Christian University is owned by Makerere University Christian Union (MUK CU) Ltd.</p>
  <h3>Our Why:</h3>
  <p>There is a scholarly crisis in the African church and society today. Most African pastors are untrained, and the effects of their teaching and misuse of power are being felt in people&rsquo;s lives. Moreover, many in other professions are also untrained and so the need for higher quality education for Africa has never been more dire. Africa needs a new and improved type of higher education that produces truly transformed and qualified workers.</p>
  <p>It is the goal of Cornerstone University to train and equip the highest caliber of Pastors and leaders in various facets of society, to maximize the redemptive and restorative assignment of the church.</p>
  <p>This way, Cornerstone University exists for the public good, the advancement of the Kingdom.</p>
  <h2>Programs</h2>
  <p>Cornerstone University will offer programs not only in theology and biblical studies, but in traditional fields like art, science, business, and education. Businessmen and women, pastors, educators, and theologians will soon be making their way into the workforce trained and equipped by experts with a Christian background.</p>
  <div class="cards">{prog}</div>
  <p style="margin-top:40px">We believe this vision will inspire a new standard for design, architecture, and learning for universities in Africa. We see this vision as a mark of progress for the church in Africa and a gateway to better community formation throughout the continent. We also see many African universities being inspired, and making changes to better their students&rsquo; experience.</p>
  {gallery([("whatsapp-image-2023-04-11-at-9.19.09-am.jpg", "Cornerstone University campus design"),
            ("whatsapp-image-2023-04-11-at-9.19.10-am-_1_.jpg", "Proposed academic buildings"),
            ("whatsapp-image-2023-04-11-at-9.19.10-am.jpg", "Campus master plan"),
            ("whatsapp-image-2023-04-11-at-9.19.11-am.jpg", "Cornerstone University rendering")], cols=2)}
</div></section>""")
    page("cornerstone-university.html", "CORNERSTONE UNIVERSITY",
         "Cornerstone University equips critical and creative servant leaders for community transformation in Africa.",
         "".join(b))


# ------------------------------------------------------- POSITIVE IMPACT
def build_positive():
    b = [banner("Positive Impact", "Positive Impact", "", "positive.jpg", short=True)]
    b.append("""<section class="section"><div class="wrapper">
  <div class="stats">
    <div class="stat reveal"><span class="stat__num">400,000</span><span class="stat__label">Ugandan believers studying under trained pastors</span></div>
    <div class="stat reveal"><span class="stat__num">$140,000</span><span class="stat__label">In rental income from Daraja</span></div>
    <div class="stat reveal"><span class="stat__num">Live</span><span class="stat__label">Streaming for conferences</span></div>
  </div>
  <p class="center" style="margin-top:44px"><a class="btn btn--dark" href="/lives-impacted.html">Read Lives Impacted</a></p>
</div></section>""")
    page("pos-impact.html", "POSITIVE IMPACT",
         "400,000 Ugandan believers studying under trained pastors and measurable community impact.",
         "".join(b))


# --------------------------------------------------------- LIVES IMPACTED
def build_lives():
    b = [banner("Lives Impacted", "Interview With Pastor David Ebenezer Mikiga", "",
                "pastor-with-book.jpg", short=True)]
    b.append(f"""<section class="section"><div class="wrapper" style="max-width:800px">
  <img src="/assets/img/lives.impacted.jpg" alt="Pastor David Ebenezer Mikiga" style="float:right;margin:0 0 20px 28px;width:161px" loading="lazy">
  <h1>Interview With Pastor David Ebenezer Mikiga</h1>
  <p>Through a pastor named Richmond, I was clothed, provided food, and given the hope of Jesus Christ. Even in those moments, God was building and preparing me for the ministry,... as I saw the transformation only He could make in my life,&rdquo; Makiga said.</p>
  <p>Years later, Makiga found himself looking for work in Mbale, in eastern Uganda. He began attending a church that his aunt also attended, which needed people for ministry outreach. Because of his service at his church in Kampala, he was asked to help. &ldquo;All I really had, I felt was John 3:16; I told people &lsquo;Jesus loves you, and His love is eternal.&rsquo;&rdquo; Congregation members began looking to Makiga for leadership as a pastor, and eventually &ndash; the pastor forced him to leave and in anger, invited church members to go with him. Makiga did leave, and many of the church members left too &ndash; creating a tremendous source of conflict.</p>
  {quote('&ldquo;In a rage of envy, the other pastor and some of the remaining church members raided this new church, literally tearing iron sheets off the outer walls of the building.&rdquo;')}
  <p>After some time passed, Makiga found a place for this new fellowship to meet for worship and was called to lead this group. His authority as pastor was affirmed by the local chairman in Mbale. In a rage of envy, the other pastor and some of the remaining church members raided this new church, literally tearing iron sheets off the outer walls of the building. Mikiga was able to reconnect with Pastor Richmond, as MUK CU led a regional training for pastors in Mbale. &ldquo;After we shared with Pastor Richmond what had transpired, he encouraged us that God was in full control. Again, he told me to forgive, to love, and to pray. As part of the conference, MUK CU fed us, provided accommodations for us at night and we left refreshed and renewed to face another day&ndash;even with challenging circumstances awaiting,&rdquo; Makiga said.</p>
  <p>MUK CU stood with Pastor David, providing a portion of the resources needed to repair their church. &ldquo;MUK CU has done a great work for me and for my church,&rdquo; Makiga said. &ldquo;In earlier days, I found it hard to preach because I had no training as a pastor. I know that many of my peers also fell into ministry without really knowing how to minister and without an understanding of God&rsquo;s word. Pastor Richmond taught us about expository preaching, and he has helped build me up as a leader in my church.&rdquo;</p>
  {quote('&ldquo;Before I connected with MUK CU I had a Bible with many pages torn away; MUK CU gave me a new study Bible, which helps me prepare my sermons &ndash; in addition to the many things I learned in our formal trainings.&rdquo;')}
  <p>&ldquo;Before I connected with MUK CU,&rdquo; he continues, &ldquo;I had a Bible with many pages torn away; MUK CU gave me a new study Bible, which helps me prepare my sermons&ndash;in addition to the many things I learned in our formal trainings. I want to give thanks to those who support MUK CU, because they have not forgotten us and the people we serve. There are times we lack in knowledge, in resources &ndash; in food and clothing, and MUK CU is there to care for us. I cannot thank God enough for allowing MUK CU to touch our lives, as if He touched us himself.&rdquo;</p>
  <p style="margin-top:44px"><a class="btn btn--dark" href="/mentorship-profiles.html">Mentorship Profiles</a></p>
</div></section>""")
    page("lives-impacted.html", "LIVES IMPACTED",
         "The story of Pastor David Ebenezer Mikiga and how MUK CU training transformed his ministry.",
         "".join(b))


# --------------------------------------------------------- MENTORSHIP
def build_mentorship():
    b = [banner("Mentorship Profiles", "Mentorship Profiles", "", "laughing.jpg", short=True)]
    cards = []
    for img, name, role, mission, body in C.MENTEES:
        cards.append(f"""<article class="card reveal" style="display:flex;gap:24px;align-items:flex-start">
      <img src="/assets/img/{img}" alt="{name}" style="width:110px;flex-shrink:0;object-fit:cover" loading="lazy">
      <div><h3 style="margin-top:0">{name}</h3>
      <p><strong>{role}</strong></p>
      <p><strong>Mission:</strong> {mission}</p>
      <p>{body}</p></div>
    </article>""")
    b.append(f"""<section class="section"><div class="wrapper">
  <p class="lead"><strong>One of MUK CU&rsquo;s main objectives</strong> is to establish and foster mentoring relationships between pastors in the West and in Africa. In this program, trained pastors in the West are connected to a pastor in Africa. Both pastors commit to follow MUK CU&rsquo;s one year syllabus, after which the African pastor is commissioned to mentor a fellow African pastor who has no ability to communicate with a mentor in the West.</p>
  <hr class="divider">
  <div style="display:grid;gap:24px">{''.join(cards)}</div>
  <p style="margin-top:44px"><a class="btn btn--dark" href="/lives-impacted.html">Back To Lives Impacted</a></p>
</div></section>""")
    page("mentorship-profiles.html", "MENTORSHIP PROFILES",
         "MUK CU connects trained pastors in the West with African pastors for one-year mentoring relationships.",
         "".join(b))


# --------------------------------------------------------- RUN ACROSS UG
def build_run():
    b = [banner("Run Across Uganda", "Run Across Uganda", "",
                "1492704_10153578205042067_8995650145922231659_o.jpg", short=True)]
    b.append("""<section class="section"><div class="wrapper center" style="max-width:760px">
  <img src="/assets/img/run_logo_fb.jpg" alt="Run Across Uganda" style="max-width:300px;margin:0 auto 40px" loading="lazy">
  <p class="lead">Thank you for your support of Manley&rsquo;s RUN ACROSS UGANDA. He was able to complete 300km and raise over $27,000 to benefit pastors and poor communities in Uganda.</p>
  <div class="stats" style="margin-top:44px">
    <div class="stat"><span class="stat__num">300km</span><span class="stat__label">Completed across Uganda</span></div>
    <div class="stat"><span class="stat__num">$27,000+</span><span class="stat__label">Raised for pastors and poor communities</span></div>
  </div>
</div></section>""")
    page("run-across-uganda.html", "RUN ACROSS UGANDA",
         "Manley's Run Across Uganda completed 300km and raised over $27,000 for pastors and communities.",
         "".join(b))


# --------------------------------------------------------- DONATE
def build_donate():
    b = [banner("One Time Gifts", "Donations &amp; Designated Gifts",
                "Please consider making a one time or recurring donation to MUK CU &amp; our projects in Africa. We are deeply grateful for your support, whether modest or ample. We partner with tithe.ly for our online donation processing.",
                "one.time.jpg",
                actions='<a class="btn btn--solid" href="https://www.pdnafrica.org/ways-to-donate" target="_blank" rel="noopener">Donate Now</a>')]
    b.append(banner("Other Ways To Give", "Other Ways To Give", "", "equipping.jpg", short=True))
    b.append(f"""<section class="section"><div class="wrapper">
  <h1>Other Ways To Give</h1>
  <div class="cards">
    <div class="card reveal"><h3>Mail A Check</h3><p>Makerere University Christian Union<br>C/O Eden Bridge Foundation<br>909 Eden Rd, Lancaster, PA 17601</p></div>
    <div class="card reveal"><h3>PayPal Giving Fund</h3><p>100% of your credit card donation is distributed to MUK CU on the 25th of the month, no fees withheld.</p></div>
    <div class="card reveal"><h3>Giving Assistant</h3><p>Simply sign up, select our cause, and shop at over 3,000+ online stores.</p></div>
    <div class="card reveal"><h3>Non-Cash Donations</h3><p>We also accept non-cash donations such as stock &amp; real estate.</p></div>
  </div>
  <p style="margin-top:40px">Please contact us for more information regarding these options: <a href="mailto:info@pdnafrica.org">info@PDNAFRICA.ORG</a></p>
  <hr class="divider">
  <div class="center">
    <img src="/assets/img/guidestarseal_2017_bronze_sm.png" alt="GuideStar Bronze Seal of Transparency" style="margin:0 auto 26px;width:100px" loading="lazy">
    <h2 style="margin-top:0">Thank You For Your Compassion And Generosity</h2>
    <p style="max-width:720px;margin:0 auto"><strong>Makerere University Christian Union</strong> is a 501(c)(3) public charity. Tax ID 27-2014552. Your contributions are tax deductible under section 170 of the 501(c)(3) Internal Revenue Code.</p>
  </div>
</div></section>""")
    page("ways-to-donate.html", "WAYS TO DONATE",
         "Support MUK CU through one-time or recurring gifts, PayPal Giving Fund, checks and non-cash donations.",
         "".join(b))


# --------------------------------------------------------- CONTACT
def build_contact():
    b = [banner("Contact", "Contact", '<a href="mailto:info@pdnafrica.org" style="color:#fff">info@pdnafrica.org</a>',
                "pdn-regional-coordinators.jpg", short=True)]
    b.append("""<section class="section"><div class="wrapper">
  <div class="contact-grid">
    <div class="contact-block">
      <h2 style="margin-top:0">Makerere University Christian Union, USA</h2>
      <p><strong>MUK CU USA:</strong> C/O Eden Bridge Foundation<br>909 Eden Rd, Lancaster, PA 17601</p>
      <p><strong>Email:</strong> <a href="mailto:info@pdnafrica.org">INFO@PDNAFRICA.ORG</a></p>
      <p><strong>Phone:</strong> <a href="tel:+17175608270">(717) 560-8270</a></p>
    </div>
    <div class="contact-block">
      <h2 style="margin-top:0">MUK CU Uganda Ltd</h2>
      <p><strong>Uganda Office:</strong> Plot 2312 and 67 Bweyogerere, Kazinga, Kira, Wakiso District, Uganda</p>
      <p><strong>Mailing Address:</strong> PO Box 40361 Nakawa, Kampala, Uganda</p>
      <p><strong>Managing Director:</strong> Ben Mutegeki</p>
      <p><strong>Email:</strong> <a href="mailto:pdnafricamarketing@gmail.com">pdnafricamarketing@gmail.com</a></p>
    </div>
  </div>
  <hr class="divider">
  <div style="max-width:620px">
    <h2 style="margin-top:0">Subscribe To Our Newsletter</h2>
    <p>Sign up with your email address to receive news &amp; updates.</p>
    <form class="form" novalidate>
      <input type="email" placeholder="Email Address" aria-label="Email Address" required>
      <button class="btn btn--solid" type="submit">Sign Up</button>
    </form>
    <p class="form__note">We respect your privacy.</p>
    <p class="form__ok">Thank you!</p>
  </div>
</div></section>""")
    page("contact.html", "Contact",
         "Contact MUK CU USA in Lancaster, PA and MUK CU Uganda Ltd in Kampala, Wakiso District.",
         "".join(b))


# --------------------------------------------------------- BLOG
def build_blog():
    b = [banner("Blog", "Blog", "", "hhj.jpg", short=True)]
    posts = [
        ("Change is Here", None, [
            "<em>&ldquo;Before this intervention, we did not have a clear mission and vision statement for the church, but now when he came in, we learnt to come up with the mission and vision statements and we have managed to put up systems that can sustain the church even in the absence of the pastor. Right now, many ministers we have in church know what to do. They are self-driven, and they can do what is expected from them&rdquo;, says Pr. Dickson.</em>",
            "MUK CU&rsquo;s Interim Pastors are adequately equipped in ministry competencies to ensure effective ministry support to the church they serve.",
            "<em>&ldquo;It&rsquo;s now a healthy church. They are growing spiritually and physically. Everyone is enjoying what he/she is doing because they know what they are doing. They are served. There is life in the church now. The numbers have increased. More people are coming in now. There are now systems which allow people to come in and stay, which was not there before&rdquo;, Pr. Dickson happily tells us.</em>",
            "Some of the competencies brought into the deployment are; Vision and mission development, Theology (introductory), Inductive bible study, Biblical communication, Discipleship, Servant Leadership, Resource mobilization, Conflict resolution, Counseling skills, and Children and youth ministry.",
            "<em>&ldquo;As a Pastor, it has relieved me of the burden I had. I was carrying the church alone. I no longer carry that burden on my own. I have free time now. I have time to do other things and yet the church is running. It is no longer depending on one person. I now even get time to rest. I get more time to attend to my family. Now things are balancing. I can now balance ministry and family&rdquo;, says a relieved Pr. Dickson.</em>",
            "A successful Interim Pastoral deployment helps the church become stronger during the transition. The Lead Pastor or Leaders can regroup, be renewed spiritually, clarify its values, and refocus its vision. Consequently, they are then in the best position to grow a healthy church, which in turn builds a health community and healthy nation.",
            "<em>&ldquo;Even now that the deployment ended, MUK CU is still helping us. And I participate in everything that they invite me to. I am now also in the IPM program and can be deployed. I am also participating in the establishment of discipleship hubs and training in these hubs&rdquo;, says Pr. Dickson enthusiastically.</em>",
        ]),
        ("A Light at The End of the Tunnel", None, [
            "<em>&ldquo;I was introduced to MUK CU (Makerere University Christian Union) when I joined the Luteete Discipleship hub. I was introduced to several programs MUK CU has included Interim Pastoral Ministry&rdquo;, Pr. Dickson says.</em>",
            "The MUK CU Discipleship hub model brings together Senior Pastors in different communities every week to support, and exhort each other, as well as keep each other accountable. It is in one of these sessions that MUK CU&rsquo;s Interim Pastoral Ministry (IPM) was introduced to Pr. Dickson.",
            "The MUK CU IPM Program seeks to offer individualised support to a church experiencing gaps in its leadership. Sometimes a pastor is not able to give the much-needed leadership in a church because he/she is sick and cannot offer pastoral leadership, or death, or there is a need to travel for different reasons like study, a sabbatical, on leave, or a mission trip. A gap can also be brought about when a pastor has fallen morally and a break from leadership is needed. Sometimes it may be a lack of some specific competencies and the need for support in a specific area. MUK CU&rsquo;s IPM Program comes to bridge the leadership gap by deploying an Interim Pastor who serves within a church&rsquo;s existing structures to provide continuity of spiritual leadership which gives the church stability and the opportunity to grow its roots and spread its branches.",
            "<em>&ldquo;MUK CU intervened through the deployment of a Pastor at my church who helped provide us with capacity building of the church ministers. The IPM Pastor helped us through training the ministers in capacity building. Some of the things we learnt were leadership skills. We learnt how to put up systems in the church. I was also invited to several conferences and trainings at MUK CU&rdquo;, says Pr. Dickson.</em>",
            "MUK CU run a needs assessment analysis to determine the specific needs of the church, the nature of engagement and period of deployment. After the assessment MUK CU deployed a well-trained, trustworthy, seasoned Pastor to support Pr. Dickson and his team for 6 months. The receiving church leadership and IPM run an orientation meeting to familiarize themselves with IPM, purposes for smooth transfer of responsibility, and expectations on each side.",
        ]),
        ("When all seems Lost", "hhj.jpg", [
            "Like many churches in Uganda, Everlasting Sanctuary of God Church in Uganda was burdened and strained by a Pastor who was over strained and in charge of everything in the church.",
            "Pr. Magembe Gideon Dickson is the Lead Pastor of Everlasting Sanctuary of God Church in Gayaza Wakiso Dictrict. His every waking moment everyday was spent at his Church. He had no rest days and did everything by himself. He was burnout and wanted to give up.",
            "<em>&ldquo;I was being overworked. I was on top of everything because we lacked systems in the church. No one knew what to do&rdquo;, he says. &ldquo;I was carrying the church alone. I was doing everything alone. It was too much and too heavy on me. I was over-stressed with everything and everyone depending on me alone.&rdquo;</em>",
            "Everlasting Sanctuary of God was one among many Pentecostal churches afraid to seek for help when the Lead Pastor is feeling overwhelmed, and the church is suffering. Many Pastors are very distrustful of churches and Pastors coming in to offer help. They are afraid that this &ldquo;help&rdquo; only comes to &ldquo;steal&rdquo; their flock. Personal Insecurities and the lack of Church governance systems are other factors that contribute to Churches not seeking for help. Some Church leaders have a ministry system that ties the church to them, making the church unable to operate in the Pastor&rsquo;s absence, which was the case of Everlasting Sanctuary of God Church.",
        ]),
    ]
    html = []
    for title, img, paras in posts:
        figure = ""
        if img:
            figure = (f'<figure class="post__img"><img src="/assets/img/{img}" alt="{title}" loading="lazy">'
                      '<figcaption class="post__caption">MUK CU Interim Pastors pray with Pr. Dickson during a home visit</figcaption></figure>')
        html.append(f"""<article class="post reveal">
      <p class="post__date">April 10, 2023</p>
      <h2 class="post__title">{title}</h2>
      {figure}
      {''.join(f'<p>{p}</p>' for p in paras)}
    </article>""")
    b.append(f'<section class="section"><div class="wrapper" style="max-width:820px">{"".join(html)}</div></section>')
    page("blog.html", "BLOG",
         "Stories from the field: how MUK CU's Interim Pastoral Ministry is strengthening churches in Uganda.",
         "".join(b))


def build_404():
    b = [banner("Page Not Found", "404",
                "The page you were looking for has moved or no longer exists.",
                "img_8436.jpg", short=True,
                actions='<a class="btn" href="/index.html">Return Home</a>')]
    b.append("""<section class="section"><div class="wrapper center">
  <h1>Let's get you back on track</h1>
  <div class="cards" style="text-align:left">
    <div class="card"><h3>About MUK CU</h3><p>Our mission, reality, vision and board.</p><p><a href="/index.html">Read more &rarr;</a></p></div>
    <div class="card"><h3>Our Programs</h3><p>Pastoral training, women's empowerment and degrees.</p><p><a href="/pastoral-training.html">Read more &rarr;</a></p></div>
    <div class="card"><h3>Ways To Donate</h3><p>Partner with us to deepen the African church.</p><p><a href="/ways-to-donate.html">Read more &rarr;</a></p></div>
  </div>
</div></section>""")
    page("404.html", "Page Not Found", "The page you were looking for could not be found.",
         "".join(b), active="/404.html")


# ------------------------------------------------------------ SEO FILES
def write_seo_files():
    from layout import SITE_URL
    base = SITE_URL  # empty until you deploy with SITE_URL set
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

    robots = ("User-agent: *\n"
              "Allow: /\n"
              "Disallow: /404.html\n"
              "Disallow: /tools/\n")
    if base:
        robots += f"\nSitemap: {base}/sitemap.xml\n"
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(robots)
    print(f"  {'sitemap.xml':46s} {len(urls):>7} urls")
    print(f"  {'robots.txt':46s}")


def main():
    for fn in (build_home, build_pastoral, build_youth, build_women, build_ipm,
               build_degrees, build_cornerstone, build_positive, build_lives,
               build_mentorship, build_run, build_donate, build_contact, build_blog,
               build_404):
        fn()
    for name, html in PAGES.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"  {name:46s} {len(html):>7,} bytes")
    write_seo_files()
    print(f"\nBuilt {len(PAGES)} pages + SEO files.")


if __name__ == "__main__":
    main()
