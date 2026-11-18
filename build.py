#!/usr/bin/env python3
"""Bouwt de statische Scarlatti-site: gedeelde header/footer + per pagina de inhoud.
Gebruik: python3 build.py   → schrijft *.html naast dit script."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
SITE = "https://scarlatti-leiden.nl"
TEL, TEL_HREF = "071 512 21 14", "tel:+31715122114"
MAIL = "info@scarlatti-leiden.nl"

NAV = [("menukaarten.html", "Menukaarten"), ("highs.html", "Highs"), ("groepen.html", "Groepen"),
       ("vacatures.html", "Vacatures"), ("contact.html", "Contact")]

BOOK = '<a class="btn {cls}" href="contact.html#reserveren" data-book>{label}</a>'


def img(src, alt, label, light=False, eager=False):
    """Foto met placeholder eronder: zolang assets/ leeg is, blijft de site toonbaar."""
    ph = f'<div class="ph{" ph--light" if light else ""}" aria-hidden="true"><span>{escape(label)}</span></div>'
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'{ph}<img src="assets/{src}" alt="{escape(alt)}" {load} decoding="async" '
            f'onerror="this.hidden=true">')


def head(title, desc, slug):
    full = "Restaurant Scarlatti Leiden" if slug == "index" else f"{title} · Restaurant Scarlatti Leiden"
    canon = SITE + "/" + ("" if slug == "index" else slug + "/")
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{escape(full)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta name="theme-color" content="#861533">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Naar de inhoud</a>
'''


def header(slug):
    cur = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{h}"{cur if h.startswith(slug + ".") else ""}>{t}</a></li>'
        for h, t in NAV)
    return f'''<header class="header">
  <div class="wrap header__bar">
    <a class="logo" href="index.html" aria-label="Restaurant Scarlatti, naar home">
      <img src="assets/logo-wit.png" alt="Restaurant Scarlatti" width="162" height="58">
    </a>
    <span class="status" data-open-status role="status">Open dagelijks</span>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav"><span class="nav-toggle__icon" aria-hidden="true"></span>Menu</button>
    <nav class="nav" id="nav" aria-label="Hoofdmenu">
      <ul>{items}</ul>
      {BOOK.format(cls="btn--light", label="Reserveren")}
    </nav>
  </div>
</header>
'''


FOOTER = f'''<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="logo" href="index.html" aria-label="Restaurant Scarlatti, naar home"><img src="assets/logo-wit.png" alt="Restaurant Scarlatti" width="162" height="58" loading="lazy"></a>
        <p>Sinds de jaren ’80 een begrip in Leiden. Lunch, diner, borrel, highs en de Heerenkamer voor groepen tot 70 personen.</p>
      </div>
      <div>
        <h2>Bezoek</h2>
        <ul>
          <li>Stille Mare 4</li>
          <li>2312 DH Leiden</li>
          <li><a href="https://www.google.com/maps/dir/?api=1&amp;destination=Restaurant+Scarlatti+Stille+Mare+4+Leiden" rel="noopener">Routebeschrijving</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="{TEL_HREF}">{TEL}</a></li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li><a href="https://www.instagram.com/restaurantscarlatti/" rel="noopener">Instagram</a> · <a href="https://www.facebook.com/ScarlattiLeiden" rel="noopener">Facebook</a></li>
        </ul>
      </div>
      <div>
        <h2>Pagina’s</h2>
        <ul>
          <li><a href="menukaarten.html">Menukaarten</a></li>
          <li><a href="highs.html">High tea &amp; high wine</a></li>
          <li><a href="groepen.html">Groepen &amp; Heerenkamer</a></li>
          <li><a href="vacatures.html">Vacatures</a></li>
          <li><a href="contact.html">Contact &amp; reserveren</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 Restaurant Scarlatti · Leiden</span>
      <span>Stille Mare 4 · 2312 DH Leiden</span>
    </div>
  </div>
</footer>

<div class="book-bar" role="region" aria-label="Snel reserveren">
  {BOOK.format(cls="btn--wine", label="Tafel reserveren")}
  <a class="btn btn--line" href="{TEL_HREF}" aria-label="Bel Scarlatti, {TEL}">Bel</a>
</div>

<!-- Guestplan-reserveringswidget (zelfde embed als de huidige site) -->
<script>
(function(g,s,t,p,l,n){{g["_gstpln"]={{}};(l=s.createElement(t)),(n=s.getElementsByTagName(t)[0]);l.async=1;l.src=p;n.parentNode.insertBefore(l,n);}})(window,document,"script","https://cdn.guestplan.com/widget.js");
_gstpln.accessKey="7c2392649f8fa83f25bfa3c863830cfff7a9980a";_gstpln.open=false;_gstpln.locale="nl";_gstpln.useNewsletterSubscription=false;
</script>
<script src="js/main.js" defer></script>
</body>
</html>
'''


def cta(title, text, extra=""):
    return f'''<section class="section section--wine on-wine">
  <div class="wrap cta">
    <div><h2>{title}</h2><p class="lead" style="margin-top:.8rem">{text}</p></div>
    <div class="btn-row" style="margin-top:0">{BOOK.format(cls="btn--light", label="Tafel reserveren")}{extra}</div>
  </div>
</section>
'''


HOURS_TABLE = '''<table class="hours">
  <caption class="visually-hidden">Openingstijden per dag</caption>
  <tbody>
    <tr data-days="1"><th scope="row">Maandag</th><td>11:30 – 21:30</td></tr>
    <tr data-days="2,3,4,5,6,0"><th scope="row">Dinsdag t/m zondag</th><td>10:30 – 21:30</td></tr>
  </tbody>
</table>'''


def dish(name, price, desc="", tag=""):
    t = f'<span class="tag">{tag}</span>' if tag else ""
    d = f'<span class="dish__desc">{desc}</span>' if desc else ""
    p = f"<span class=\"visually-hidden\">€</span>{price}" if price[0].isdigit() else price
    return f'<li class="dish"><span class="dish__name">{name}{t}</span><span class="dish__price">{p}</span>{d}</li>'


def group(title, dishes):
    return f'<div class="menu-group"><h3>{title}</h3><ul class="menu-list">{"".join(dish(*d) for d in dishes)}</ul></div>'


# ---------------------------------------------------------------- HOME
HOME = f'''<main id="main">
<section class="hero">
  <div class="hero__media">{img("gevel.jpg", "Het uithangbord van Scarlatti aan de gevel, met de Stille Mare op de achtergrond", "Gevel · Stille Mare", eager=True)}</div>
  <div class="hero__panel on-wine">
    <span class="eyebrow">Lunch · Diner · Borrel · Highs</span>
    <h1>Welkom bij Scarlatti</h1>
    <p class="lead">Reserveer een tafel of loop gewoon binnen. Sinds de jaren ’80 een begrip in Leiden, aan de Stille Mare tegenover de Stadsgehoorzaal.</p>
    <div class="btn-row">{BOOK.format(cls="btn--light", label="Tafel reserveren")}<a class="btn btn--line" href="menukaarten.html">Menukaarten</a></div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap">
    <h2 class="visually-hidden">Waarvoor kom je?</h2>
    <div class="quick reveal">
      <a href="menukaarten.html#lunch"><strong>Lunch &amp; diner</strong><span>De hele dag terecht, van uitsmijter tot ribeye.</span></a>
      <a href="highs.html"><strong>High tea &amp; high wine</strong><span>Voor groepen vanaf 10 personen. Vanaf € 24,50 p.p.</span></a>
      <a href="groepen.html"><strong>Heerenkamer</strong><span>Eigen ruimte met open haard voor 10 tot 70 personen.</span></a>
      <a href="menukaarten.html#fondue"><strong>Kaasfondue</strong><span>Van september tot april, vanaf 2 personen.</span></a>
    </div>
  </div>
</section>

<section class="split">
  <div class="split__media">{img("lunch.jpg", "Lunchgerechten op tafel bij Scarlatti", "Lunch")}</div>
  <div class="split__panel reveal"><span class="eyebrow">2 tot 30 personen</span><h2>Lunch &amp; diner</h2><span class="ornament"></span>
    <p>Klassiekers als Oma Bob’s kroketten en de uitsmijter Scarlatti, ’s avonds zeewolf uit de oven of onze ribeye. Om bij te kletsen of om iets te vieren.</p>
    <div class="btn-row"><a class="btn btn--line" href="menukaarten.html">Bekijk de menukaart</a></div></div>
</section>
<section class="split split--rev split--cream">
  <div class="split__media">{img("hightea.jpg", "High tea met etagère en theepot", "High tea", light=True)}</div>
  <div class="split__panel reveal"><span class="eyebrow">10 tot 30 personen</span><h2>High tea &amp; high wine</h2><span class="ornament"></span>
    <p>Onbeperkt thee met een etagère vol hartig en zoet, of drie glazen wijn in drie rondes met huisgemaakte gerechten.</p>
    <div class="btn-row"><a class="btn btn--line" href="highs.html">Onze highs</a></div></div>
</section>
<section class="split">
  <div class="split__media">{img("heerenkamer.jpg", "De Heerenkamer met gedekte tafel en wijnkast", "Heerenkamer")}</div>
  <div class="split__panel reveal"><span class="eyebrow">Tot 70 personen</span><h2>De Heerenkamer</h2><span class="ornament"></span>
    <p>Op de eerste etage, met open haard en eikenhouten vloer. Voor borrels, diners en highs met je eigen gezelschap.</p>
    <div class="btn-row"><a class="btn btn--wine" href="groepen.html#aanvraag">Groep aanvragen</a><a class="btn btn--line" href="groepen.html">Meer over groepen</a></div></div>
</section>
<section class="split split--rev split--cream">
  <div class="split__media">{img("fondue.jpg", "Kaasfondue met brood en charcuterie", "Kaasfondue", light=True)}</div>
  <div class="split__panel reveal"><span class="eyebrow">September t/m april</span><h2>Kaasfondue</h2><span class="ornament"></span>
    <p>Je kunt de klok erop gelijkzetten: elk jaar van september tot april staat onze kaasfondue weer op tafel. Vanaf 2 personen, € 23,50 p.p.</p>
    <div class="btn-row"><a class="btn btn--line" href="menukaarten.html#fondue">Bekijk de kaart</a></div></div>
</section>
<section class="split">
  <div class="split__media">{img("borrel.jpg", "Borrelplank met bitterballen, olijven en een glas rosé", "Borrel")}</div>
  <div class="split__panel reveal"><span class="eyebrow">De hele dag</span><h2>Borrel</h2><span class="ornament"></span>
    <p>Borrelplanken, bittergarnituur, truffelfrites en calamares. Op het terras aan het water of binnen aan de bar.</p>
    <div class="btn-row"><a class="btn btn--line" href="menukaarten.html#borrel">Borrelkaart</a></div></div>
</section>

<section class="band">
  {img("openhaard.jpg", "", "Open haard")}
  <div class="wrap reveal"><span class="eyebrow">Over ons</span><blockquote>Wat begon als theehuis, groeide uit tot een volwaardig restaurant.</blockquote></div>
</section>

<section class="section">
  <div class="wrap grid-2">
    <div class="reveal">
      <span class="eyebrow">Restaurant Scarlatti</span>
      <h2>Vernoemd naar een componist</h2>
      <p class="lead" style="margin-top:1.2rem">De eerste eigenaar was een groot liefhebber van de Italiaanse componist Domenico Scarlatti en vernoemde zijn theehuis naar zijn muzikale favoriet. Die naam houden we met trots: om onze geschiedenis, en omdat hij voor veel vaste gasten iets betekent.</p>
    </div>
    <div class="frame reveal">{img("uithangbord.jpg", "Het uithangbord van Scarlatti", "Uithangbord", light=True)}</div>
  </div>
</section>

<section class="section--rose section">
  <div class="wrap info">
    <div><h2>Openingstijden</h2>{HOURS_TABLE}</div>
    <div><h2>Reserveren</h2><p><a href="{TEL_HREF}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p><p class="muted" style="margin-top:.8rem">Of loop gezellig even binnen.</p>
      <div class="btn-row">{BOOK.format(cls="btn--wine", label="Online reserveren")}</div></div>
    <div><h2>Vinden</h2><p>Stille Mare 4, 2312 DH Leiden. In hartje Leiden, tegenover de Stadsgehoorzaal.</p><p style="margin-top:.8rem"><a href="contact.html#vinden">Route</a></p></div>
  </div>
</section>
</main>
'''

# ---------------------------------------------------------------- MENUKAARTEN
LUNCH = [
    ("Klassiekers", [
        ("Trio van vis", "14,50", "Gerookte zalm, tonijnsalade, 2 gambakroketjes, frisse dressing, sla"),
        ("Carpaccio", "14,50", "Italiaanse kaas, balsamico, rucola, pijnboompitten"),
        ("Oma Bob’s kroketten", "11,75", "2 rundvlees- of bospaddenstoelenkroketten", "vega mogelijk"),
        ("Uitsmijter", "11,50", "3 gebakken eieren met ham, kaas, tomaat of spek (+1), of alles (+1)"),
        ("Uitsmijter Scarlatti", "14,50", "3 gebakken eieren, gerookte runderribeye, gesmolten Rotterdamse oude kaas, truffelmayonaise"),
        ("Croque monsieur", "9,75", "Kaas, ham, bechamelsaus, gruyère (spiegelei +1,50)"),
        ("Tosti", "7,75", "Ham, kaas, tomaat of spek (+1), of alles (+1)"),
    ]),
    ("Specialiteiten", [
        ("Broodje pulled chicken", "12,75", "Langzaam gegaarde kip, bao bun, zoetzure groenten, barbecuesaus"),
        ("Tuna melt", "12,75", "Briochebol, tonijnsalade, kaas, tomaat, rucola, uit de oven"),
        ("Avocado toast", "12,75", "Landbrood, verse avocado, avocadospread, gekookt ei, pijnboompitten, zongedroogde tomaat", "vega"),
        ("Soep van geroosterde paprika en tomaat", "8,75", "Met brood", "vega"),
        ("Soep van het moment", "8,75", "Met brood"),
    ]),
    ("Hoofdgerechten", [
        ("Ribeye Scarlatti", "27,50", "190 gram, gepofte knoflookcrème, seizoensgroenten, zeezoutboter"),
        ("Caesar salade", "19,50", "Romeinse sla, kip of vegan kipstukjes, Parmezaanse kaas, ansjovis, ei, brood"),
        ("Burger Scarlatti", "19,75", "Runder- of vegaburger, briochebol, bacon, cheddar, truffelmayonaise, tomatensalsa, frites"),
    ]),
]
DINER = [
    ("Voorgerechten", [
        ("Brood uit de oven", "8,75", "Extra vergine olijfolie, zeezoutboter", "vega"),
        ("Carpaccio", "13,75", "Italiaanse kaas, balsamico, pijnboompitten, rucola"),
        ("Tonijn tataki", "14,50", "Licht geschroeide saku tonijn, soja-uitjes, pittige mayonaise, furikake"),
        ("Gebakken boerenbrie", "13,75", "Briochebrood, honing, walnoot, rode-uienchutney", "vega"),
        ("Soep van geroosterde paprika en tomaat", "8,75", "Met brood", "vega"),
        ("Soep van het moment", "8,75", "Met brood"),
    ]),
    ("Hoofdgerechten", [
        ("Zeewolf uit de oven", "25,50", "Venkel, rode biet, groene kruidenolie"),
        ("Pasta puttanesca", "19,50", "Tomatensaus, ansjovis, kappertjes, olijven, chilivlokken"),
        ("Ribeye Scarlatti", "27,50", "190 gram, gepofte knoflookcrème, seizoensgroenten, zeezoutboter"),
        ("Halve kip", "19,50", "Sous vide gegaard, knapperige huid, gepofte trostomaatjes, citroen"),
        ("Burger Scarlatti", "19,75", "Runder- of vegaburger, briochebol, bacon, cheddar, truffelmayonaise, tomatensalsa, frites"),
        ("Caesar salade", "19,50", "Romeinse sla, kip of vegan kipstukjes, Parmezaanse kaas, ansjovis, ei, brood"),
    ]),
    ("Bijgerechten", [
        ("Verse frites", "5,75", "Met mayonaise"),
        ("Gemengde salade", "5,75"),
        ("Extra saus", "0,50", "Mayonaise, ketchup of truffelmayonaise"),
    ]),
    ("Desserts", [
        ("Crème brûlée", "9,75", "Huisgemaakt, vanille-ijs"),
        ("Aardbeien Romanoff", "10,75", "Gemarineerde aardbeien, sinaasappel, lichte Romanoffroom"),
        ("Sgroppino", "9,50", "Citroensorbetijs, prosecco, wodka"),
        ("Speciale koffie", "10,50", "Likeur naar keuze, slagroom"),
    ]),
]
FONDUE = [("Kaasfondue · vanaf 2 personen", [
    ("Kaasfondue", "23,50 p.p.", "Met brood en groenten"),
    ("Scarlatti borrelplank", "+ 7,50", "Picos, krieltjes, albondigas (vega mogelijk)"),
    ("Charcuterie", "+ 9,00", "3 soorten gesneden vleeswaren"),
    ("Extra smaak", "+ 3,00 p.p.", "Blauwe kaas of truffel"),
    ("Extra portie kaas", "+ 10,00"),
])]
BORREL = [
    ("Borrelhapjes", [
        ("Brood uit de oven", "8,75", "Zeezoutboter, extra vergine olijfolie"),
        ("Nacho’s", "10,25", "Gesmolten kaas, crème fraîche, guacamole, tomatensalsa"),
        ("Truffelfrites", "9,75", "Truffelmayonaise, Grana Padano"),
        ("Calamares", "9,25", "Gefrituurde inktvis, aioli"),
        ("Fuet", "8,75", "Uit Catalonië, licht gepeperd"),
        ("Rotterdamse oude kaas", "7,75", "Mosterd"),
        ("Fuet &amp; oude kaas", "14,50", "Mosterd"),
        ("Olijven", "5,50", "Gemarineerd met knoflook en paprika"),
    ]),
    ("Planken &amp; bittergarnituur", [
        ("Scarlatti borrelplank", "21,50", "Brood, olijven, fuet, truffelfrites, rundvleesbitterballen, kaassticks"),
        ("Vegetarische borrelplank", "21,50", "Brood, olijven, nacho’s, truffelfrites, mini groenteloempia’s, kaassticks", "vega"),
        ("Rundvleesbitterballen (4)", "5,50", "Mosterd"),
        ("Mini groenteloempia’s (4)", "5,50", "Chilisaus"),
        ("Kaassticks (4)", "5,50", "Chilisaus"),
        ("Gambakroketjes (4)", "7,00", "Aioli"),
        ("Bittergarnituur 8 stuks", "12,50"),
        ("Bittergarnituur 12 stuks", "17,50"),
    ]),
]


def menu_section(id_, title, intro, groups, image=None):
    cols = "".join(group(t, d) for t, d in groups)
    media = f'<div class="frame" style="margin-top:0">{image}</div>' if image else ""
    return f'''<section class="section menu-section" id="{id_}" aria-labelledby="{id_}-t">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{intro}</span><h2 id="{id_}-t">{title}</h2></div>
    <div class="menu-cols">{cols}{media}</div>
  </div>
</section>'''


MENU = f'''<main id="main">
<section class="page-hero">
  {img("lunch.jpg", "", "Lunch", eager=True)}
  <div class="wrap"><span class="eyebrow">Lunch · diner · fondue · borrel</span><h1>Menukaarten</h1></div>
</section>
<nav class="subnav" aria-label="Onderdelen menukaart">
  <div class="wrap"><ul>
    <li><a href="#lunch">Lunch</a></li><li><a href="#diner">Diner</a></li>
    <li><a href="#fondue">Kaasfondue</a></li><li><a href="#borrel">Borrel</a></li>
  </ul></div>
</nav>
{menu_section("lunch", "Lunch", "Op wit of bruin landbrood", LUNCH)}
{menu_section("diner", "Diner", "Voor- en hoofdgerechten, desserts", DINER)}
{menu_section("fondue", "Kaasfondue", "September t/m april", FONDUE, img("fondue.jpg", "Kaasfondue met brood en charcuterie", "Kaasfondue", light=True))}
{menu_section("borrel", "Borrel", "De hele dag", BORREL)}
<section class="section--tight"><div class="wrap"><p class="note"><strong>Allergieën of dieetwensen?</strong> Vraag het ons team, we denken graag mee. Prijzen in euro’s, inclusief btw.</p></div></section>
{cta("Reserveer een tafel", "Of loop gezellig even binnen. Met een groep? De Heerenkamer biedt plek aan tot 70 personen.", '<a class="btn btn--line" href="groepen.html">Groepen</a>')}
</main>
'''

# ---------------------------------------------------------------- HIGHS
HIGHS = f'''<main id="main">
<section class="page-hero">
  {img("hightea.jpg", "", "High tea", eager=True)}
  <div class="wrap"><span class="eyebrow">Voor groepen van 10 tot 30 personen</span><h1>High tea &amp; high wine</h1></div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="lead">Huisgemaakt, uitgebreid en gezellig: ideaal voor een verjaardag, vrijgezellenfeest of uitje met collega’s. Beide highs zijn ook vegetarisch te krijgen.</p></div>
    <div class="cards">
      <article class="card reveal">
        <div class="frame">{img("hightea-etagere.jpg", "Etagère met scones, macarons en hartige hapjes", "High tea", light=True)}</div>
        <div class="card__body">
          <span class="card__meta">10 t/m 30 personen</span>
          <h2 style="font-size:1.6rem">High tea</h2>
          <p>Onbeperkt thee en een etagère met hartige en zoete hapjes.</p>
          <p class="card__price">€ 24,50 <small style="font-size:.9rem">p.p.</small></p>
          <ul class="checks">
            <li>Paprika-tomatensoepje</li><li>Toast met gerookte zalm en crème fraîche</li>
            <li>Sandwich met jonge kaas, mosterd en mesclun</li><li>Wrap met guacamole, ribeye en zongedroogde tomaat</li>
            <li>Scones met aardbeienjam</li><li>Brownie, cheesecake, macaron en petit four</li>
          </ul>
          <a class="btn btn--wine" href="groepen.html?type=high-tea#aanvraag">High tea aanvragen</a>
        </div>
      </article>
      <article class="card reveal">
        <div class="frame">{img("wijn.jpg", "Twee gasten proosten met een glas rosé en witte wijn", "High wine", light=True)}</div>
        <div class="card__body">
          <span class="card__meta">10 t/m 30 personen</span>
          <h2 style="font-size:1.6rem">High wine</h2>
          <p>Drie glazen wijn, geserveerd in drie rondes met huisgemaakte gerechten.</p>
          <p class="card__price">€ 32,50 <small style="font-size:.9rem">p.p.</small></p>
          <ul class="checks">
            <li>Brood uit de oven, Italiaanse ham, oude kaas, gerookte zalmrolletjes</li>
            <li>Gebakken biefstukpuntjes met champignon, salade, paprika-tomatensoepje, nacho’s</li>
            <li>Grand dessert met huisgemaakte zoetigheden</li>
          </ul>
          <a class="btn btn--wine" href="groepen.html?type=high-wine#aanvraag">High wine aanvragen</a>
        </div>
      </article>
    </div>
    <p class="note">In de Heerenkamer zit je met 10 tot 22 personen aan één lange tafel, of tot 30 personen in restaurantopstelling. <a href="groepen.html">Meer over de Heerenkamer</a></p>
  </div>
</section>
</main>
'''

# ---------------------------------------------------------------- GROEPEN
OPTIONS = [
    ("lunch.jpg", "10 tot 30 personen", "Lunch", "Een broodjes- of specialiteitenlunch, of we geven invulling aan je eigen idee.", ""),
    ("hightea-etagere.jpg", "10 tot 30 personen", "High tea of high wine", "Huisgemaakte gerechten, ook vegetarisch. Vanaf € 24,50 per persoon.", '<a class="btn btn--line" href="highs.html">Bekijk de highs</a>'),
    ("heerenkamer.jpg", "10 tot 30 personen", "Diner", "Een drie- of meergangendiner van onze chef. Vanaf 10 personen werken we met een groepsmenu, aangepast aan wensen en diëten.", ""),
    ("openhaard.jpg", "10 tot 30 personen", "Dinerspel", "Een dinerspel van dinerspel.nl, met een speciaal groepsmenu.", ""),
    ("borrel.jpg", "Tot 70 personen", "(Afstudeer)borrel", "Hapjes naar wens in overleg met de chef. Eventueel met een eigen biertap in de ruimte.", '<a class="btn btn--line" href="menukaarten.html#borrel">Borrelkaart</a>'),
]


def option_card(o):
    src, meta, title, text, btn = o
    return f'''<article class="card reveal"><div class="frame">{img(src, "", title, light=True)}</div>
  <div class="card__body"><span class="card__meta">{meta}</span><h3>{title}</h3><p>{text}</p>{btn}</div></article>'''


def field(id_, label, kind="text", required=False, hint="", attrs="", label_key=None):
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    r = " required" if required else ""
    hint_html = f'<span class="hint" id="{id_}-hint">{hint}</span>' if hint else ""
    desc = f' aria-describedby="{id_}-hint {id_}-error"' if hint else f' aria-describedby="{id_}-error"'
    data = f' data-label="{label_key or label}"'
    if kind == "textarea":
        ctrl = f'<textarea id="{id_}" name="{id_}"{r}{desc}{data} {attrs}></textarea>'
    elif kind.startswith("select:"):
        opts = "".join(f"<option>{o}</option>" for o in kind[7:].split("|"))
        ctrl = f'<select id="{id_}" name="{id_}"{r}{desc}{data} {attrs}><option value="">Maak een keuze</option>{opts}</select>'
    else:
        ctrl = f'<input id="{id_}" name="{id_}" type="{kind}"{r}{desc}{data} {attrs}>'
    return f'<div class="field"><label for="{id_}">{label}{req}</label>{hint_html}{ctrl}<span class="error" id="{id_}-error" aria-live="polite"></span></div>'


GROUP_FORM = f'''<form class="form" data-mailform data-subject="Groepsaanvraag Scarlatti" novalidate>
  <p class="muted">Velden met <span class="req">*</span> zijn verplicht. We nemen zo snel mogelijk contact met je op met een voorstel.</p>
  <div class="row">
    {field("soort", "Wat wil je doen?", "select:Lunch|High tea|High wine|Diner|Dinerspel|Borrel|Iets anders", True, label_key="Soort", attrs='data-error="Kies wat je wilt doen."')}
    {field("personen", "Aantal personen", "number", True, "Van 10 tot 70 personen", 'min="10" max="70" inputmode="numeric" data-error="Vul het aantal personen in."', "Personen")}
  </div>
  <div class="row">
    {field("datum", "Gewenste datum", "date", True, attrs='data-error="Kies een datum."', label_key="Datum")}
    {field("tijd", "Tijd (ongeveer)", "time", label_key="Tijd")}
  </div>
  <div class="row">
    {field("naam", "Naam", "text", True, attrs='autocomplete="name" data-error="Vul je naam in."', label_key="Naam")}
    {field("telefoon", "Telefoonnummer", "tel", attrs='autocomplete="tel"', label_key="Telefoon")}
  </div>
  {field("email", "E-mailadres", "email", True, attrs='autocomplete="email" data-error="Vul een geldig e-mailadres in."', label_key="E-mail")}
  {field("wensen", "Wensen, gelegenheid of dieetwensen", "textarea", label_key="Wensen")}
  <div><button class="btn btn--wine" type="submit">Aanvraag versturen</button></div>
  <p class="form-status" role="status" tabindex="-1" hidden></p>
</form>'''

GROEPEN = f'''<main id="main">
<section class="page-hero">
  {img("heerenkamer.jpg", "", "Heerenkamer", eager=True)}
  <div class="wrap"><span class="eyebrow">Groepen · 10 tot 70 personen</span><h1>De Heerenkamer</h1></div>
</section>
<section class="section">
  <div class="wrap grid-2">
    <div class="reveal">
      <span class="eyebrow">Eerste etage</span>
      <h2>Open haard, daglicht en een eikenhouten vloer</h2>
      <p class="lead" style="margin-top:1.2rem">Zeer geschikt voor (afstudeer)borrels en diners. Aan één lange tafel zit je met 10 tot 22 personen, in restaurantopstelling met maximaal 30, en voor een borrel is er plek voor 70.</p>
      <dl class="facts">
        <div><dt>Lange tafel</dt><dd>10 – 22</dd></div>
        <div><dt>Restaurant</dt><dd>tot 30</dd></div>
        <div><dt>Borrel</dt><dd>tot 70</dd></div>
      </dl>
      <p class="note">Geen zaalhuur. Voor exclusief gebruik geldt een minimale besteding: zondag t/m donderdag € 550, vrijdag en zaterdag € 700.</p>
      <div class="btn-row"><a class="btn btn--wine" href="#aanvraag">Aanvraag doen</a><a class="btn btn--line" href="{TEL_HREF}">Bel {TEL}</a></div>
    </div>
    <div class="frame frame--tall reveal">{img("openhaard.jpg", "De open haard in de Heerenkamer", "Open haard", light=True)}</div>
  </div>
</section>
<section class="section section--cream">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Mogelijkheden</span><h2>Wat we voor je groep doen</h2></div>
    <div class="cards cards--3">{"".join(option_card(o) for o in OPTIONS)}
      <article class="card reveal"><div class="card__body"><span class="card__meta">Praktisch</span><h3>Goed om te weten</h3>
        <ul class="checks"><li>Individuele menukeuze graag minimaal 5 werkdagen vooraf; anders € 2,50 p.p. meerprijs.</li><li>Vanaf 10 personen werken we met een groepsmenu.</li><li>Allergieën en diëten stemmen we vooraf af.</li></ul></div></article>
    </div>
  </div>
</section>
<section class="section" id="aanvraag" aria-labelledby="aanvraag-t">
  <div class="wrap grid-2" style="align-items:start">
    <div>
      <span class="eyebrow">Groepsaanvraag</span>
      <h2 id="aanvraag-t">Vraag de Heerenkamer aan</h2>
      <p class="lead" style="margin-top:1rem">Vertel ons wanneer, met hoeveel en wat je in gedachten hebt. Liever bellen? <a href="{TEL_HREF}">{TEL}</a></p>
      <p class="muted" style="margin-top:1rem">Met minder dan 10 personen? Dan reserveer je gewoon een tafel.</p>
      <div class="btn-row">{BOOK.format(cls="btn--line", label="Tafel reserveren")}</div>
    </div>
    {GROUP_FORM}
  </div>
</section>
</main>
<script>
/* Voorselectie vanuit highs-pagina (?type=high-tea) */
(function(){{var t=new URLSearchParams(location.search).get("type");var s=document.getElementById("soort");if(!t||!s)return;var m={{"high-tea":"High tea","high-wine":"High wine"}}[t];if(m)s.value=m;}})();
</script>
'''

# ---------------------------------------------------------------- VACATURES
def job(id_, title, meta, intro, what_t, what, offer_t, offer):
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    subj = f"Sollicitatie {title.lower()}".replace(" ", "%20")
    return f'''<article class="card reveal" aria-labelledby="{id_}">
  <div class="card__body">
    <span class="card__meta">{meta}</span><h2 id="{id_}" style="font-size:1.7rem;color:var(--wine)">{title}</h2>
    <p>{intro}</p>
    <h3 style="font-size:1.1rem;margin-top:.6rem">{what_t}</h3><ul class="checks">{li(what)}</ul>
    <h3 style="font-size:1.1rem;margin-top:.6rem">{offer_t}</h3><ul class="checks">{li(offer)}</ul>
    <a class="btn btn--wine" href="mailto:{MAIL}?subject={subj}">Solliciteer</a>
    <p class="muted" style="font-size:.92rem">Of mail je cv naar {MAIL}</p>
  </div>
</article>'''


VACATURES = f'''<main id="main">
<section class="page-hero">
  {img("stad.jpg", "", "Leiden", eager=True)}
  <div class="wrap"><span class="eyebrow">Werken in hartje Leiden</span><h1>Vacatures</h1></div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="lead">Een betrokken team, gasten die al jaren terugkomen en een plek aan het water. Zie je jezelf hier werken? We horen graag van je, ook als je vacature er (nog) niet tussen staat.</p></div>
    <div class="cards">
      {job("job-lb", "Leidinggevende bediening", "Uren in overleg",
           "Ben jij een geboren leider met oog voor detail, passie voor gastvrijheid en een hart voor teamwork? Je bent sterk op de vloer en denkt achter de schermen strategisch mee.",
           "Wat ga je doen", ["Restaurantmanagement: gastbeleving, in- en verkoop, groepsreserveringen", "Personeel: roosters, verlof, aannemen, inwerken en beoordelen", "Aanspreekpunt voor HR, marketing en onze andere locaties"],
           "Wat bieden wij", ["Bruto € 2.900 – € 3.300 per maand op fulltime basis", "Ruimte voor eigen initiatief en groei, leasefietsplan", "Overuren uitbetaald of tijd voor tijd", "Een betrokken en gezellig team"])}
      {job("job-af", "Afwasser", "Vaste dagen in overleg",
           "Jij zorgt dat de keuken soepel blijft draaien: vaat, bestek en apparatuur schoon en op tijd klaar voor het team.",
           "Wie zoeken we", ["Hands-on: je pakt aan waar nodig", "Je werkt netjes en houdt van een schone werkplek", "Werkervaring is fijn, maar geen vereiste"],
           "Wat bieden wij", ["Vaste werkdagen, dag- en avonddiensten", "Marktconform salaris, fooi en vakantiegeld", "Doorgroei- en ontwikkelmogelijkheden"])}
    </div>
  </div>
</section>
</main>
'''

# ---------------------------------------------------------------- CONTACT
CONTACT_FORM = f'''<form class="form" data-mailform data-subject="Vraag via website" novalidate>
  <div class="row">
    {field("c-naam", "Naam", "text", True, attrs='autocomplete="name" data-error="Vul je naam in."', label_key="Naam")}
    {field("c-tel", "Telefoonnummer", "tel", attrs='autocomplete="tel"', label_key="Telefoon")}
  </div>
  {field("c-email", "E-mailadres", "email", True, attrs='autocomplete="email" data-error="Vul een geldig e-mailadres in."', label_key="E-mail")}
  {field("c-bericht", "Bericht", "textarea", True, attrs='data-error="Schrijf je vraag."', label_key="Bericht")}
  <div><button class="btn btn--wine" type="submit">Versturen</button></div>
  <p class="form-status" role="status" tabindex="-1" hidden></p>
</form>'''

CONTACT = f'''<main id="main">
<section class="page-hero">
  {img("terras.jpg", "", "Terras", eager=True)}
  <div class="wrap"><span class="eyebrow">Contact</span><h1>Tot snel bij Scarlatti</h1></div>
</section>
<section class="section" id="reserveren" aria-labelledby="res-t">
  <div class="wrap grid-2" style="align-items:start">
    <div>
      <span class="eyebrow">Reserveren</span>
      <h2 id="res-t">Een tafel voor 2 tot 30</h2>
      <p class="lead" style="margin-top:1rem">Reserveer direct online, bel ons of loop gewoon binnen.</p>
      <div class="btn-row">{BOOK.format(cls="btn--wine", label="Online reserveren")}<a class="btn btn--line" href="{TEL_HREF}">Bel {TEL}</a></div>
      <p class="muted" style="margin-top:1.2rem">Groep van 10 of meer, high tea of de Heerenkamer? <a href="groepen.html#aanvraag">Doe een groepsaanvraag</a>.</p>
      <div class="info" style="grid-template-columns:1fr;margin-top:2.6rem">
        <div><h3>Openingstijden</h3>{HOURS_TABLE}</div>
        <div><h3>Direct contact</h3><p><a href="{TEL_HREF}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a><br><a href="https://www.instagram.com/restaurantscarlatti/" rel="noopener">Instagram</a> · <a href="https://www.facebook.com/ScarlattiLeiden" rel="noopener">Facebook</a></p></div>
      </div>
    </div>
    <div>
      <span class="eyebrow">Een vraag?</span>
      <h2>Stuur een bericht</h2>
      <p class="muted" style="margin:1rem 0 1.6rem">Over de mogelijkheden, een allergie of iets anders. Voor tafelreserveringen gebruik je de knop hiernaast.</p>
      {CONTACT_FORM}
    </div>
  </div>
</section>
<section class="section section--rose" id="vinden" aria-labelledby="vind-t">
  <div class="wrap grid-2">
    <div>
      <span class="eyebrow">Vinden</span>
      <h2 id="vind-t">Stille Mare 4, Leiden</h2>
      <p class="lead" style="margin-top:1rem">In hartje Leiden aan het water, tegenover de Stadsgehoorzaal.</p>
      <div class="btn-row"><a class="btn btn--wine" href="https://www.google.com/maps/dir/?api=1&amp;destination=Restaurant+Scarlatti+Stille+Mare+4+Leiden" rel="noopener">Routebeschrijving</a></div>
    </div>
    <div class="frame">{img("gevel.jpg", "De gevel van Scarlatti aan de Stille Mare", "Stille Mare", light=True)}</div>
  </div>
</section>
</main>
'''

PAGES = {
    "index": ("Home", "Restaurant Scarlatti in Leiden: lunch, diner, borrel, high tea en high wine aan de Stille Mare. Heerenkamer voor groepen tot 70 personen.", HOME),
    "menukaarten": ("Menukaarten", "De lunch-, diner-, fondue- en borrelkaart van Restaurant Scarlatti in Leiden.", MENU),
    "highs": ("High tea & high wine", "High tea vanaf € 24,50 en high wine vanaf € 32,50 p.p. voor groepen van 10 tot 30 personen bij Scarlatti Leiden.", HIGHS),
    "groepen": ("Groepen & Heerenkamer", "De Heerenkamer van Scarlatti: eigen ruimte met open haard voor 10 tot 70 personen. Lunch, diner, highs en borrels.", GROEPEN),
    "vacatures": ("Vacatures", "Werken bij Restaurant Scarlatti in hartje Leiden. Bekijk onze vacatures.", VACATURES),
    "contact": ("Contact & reserveren", "Reserveer een tafel bij Scarlatti, Stille Mare 4 Leiden. Bel 071 512 21 14 of reserveer online.", CONTACT),
}

if __name__ == "__main__":
    for slug, (title, desc, body) in PAGES.items():
        html = head(title, desc, slug) + header(slug) + body + FOOTER
        (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")
        print("✓", f"{slug}.html")
