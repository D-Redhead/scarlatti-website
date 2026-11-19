---
name: Scarlatti – De twee verdiepingen
version: 1
colors:
  wine: "#7A0E2A"        # wijnrood: merkvlak, header, footer, primaire knop-tekst
  wine-deep: "#5E0A20"   # hover/pressed op wijnrood
  oak: "#7E5130"         # eikenhout: vlak van de 1e verdieping (Heerenkamer)
  oak-deep: "#66411F"
  wall: "#3D4A43"        # muurgroen: secundair vlak (seizoen, highs)
  lime: "#F4EFE8"        # kalk: ondergrond voor lange tekst
  lime-alt: "#EAE2D6"    # kalk, een stap donkerder: panelen op kalk
  ink: "#1E1A17"         # tekst op kalk
  ink-soft: "#5A4F47"    # secundaire tekst op kalk (7.1:1 op lime)
  on-dark: "#F4EFE8"     # tekst op wijn, eiken, muurgroen
  on-dark-soft: "#E6D9CC" # secundaire tekst op donkere vlakken
  line: "#D6CBBB"        # haarlijn op kalk
  white: "#FFFFFF"       # invoervelden en hover-vlak op kalk
  open: "#7FC48F"        # stip 'nu open' (geen tekst)
  field-border: "#8C7F73" # rand van invoervelden (3:1 op wit)
  error: "#9E1C14"       # foutmelding op kalk
  error-border: "#B3261E"
  error-on-dark: "#FFD7D2" # foutmelding op muurgroen
typography:
  display: "Young Serif, Georgia, serif"   # één gewicht (400), koppen
  body: "Figtree, system-ui, sans-serif"   # 400 / 500 / 600
  scale: { h1: "clamp(2.5rem, 6vw, 4.5rem)", h2: "clamp(2rem, 4vw, 3rem)", h3: "1.375rem", body: "1.0625rem", small: "0.9375rem" }
radius: { none: 0, control: "2px" }
spacing: { section: "clamp(4.5rem, 9vw, 8rem)", gutter: "1rem (mobiel) / 2rem", wrap: "1200px" }
---

# DESIGN.md – Restaurant Scarlatti

Richting **A, De twee verdiepingen**, gekozen op 19-11-2026. Productfeiten staan in `PRODUCT.md`, inhoud in `_audit/content.md`.

## Idee

De site is gebouwd zoals het pand. **Begane grond** is het restaurant aan het water, met het terras, de lunch, het diner en de borrel. **1e verdieping** is de Heerenkamer. Elke verdieping heeft een eigen kleurvlak: de begane grond wijnrood en kalk, de 1e verdieping eikenhout. Een kleine verdiepingsaanduiding ("Begane grond", "1e verdieping") staat in de sectiekoppen en in de navigatie, zodat je merkt dat je "naar boven gaat". Het is een aanduiding van plaats, geen versiering, en geen eyebrow-label boven elke kop. Hij staat alleen bij de twee verdiepingsovergangen.

## Kleur

- **Committed:** wijnrood draagt 30–50% van het oppervlak als echte vlakken (hero-tekstvlak, header, footer). Het is geen accent dat over wit gestrooid wordt.
- Lopende tekst, menu's, prijzen en voorwaarden staan **altijd op kalk** (`lime`), in `ink`.
- Op wijn, eiken en muurgroen staat tekst altijd in `on-dark`, nooit in grijs. Contrast: lime op wine 12:1, op wall 8:1, op oak 5.9:1; on-dark-soft op oak 4.9:1.
- Geen verlopen, geen glas, geen blur, geen schaduwen als versiering.
- Tekstselectie in wine op lime, en focusringen in wine (op donkere vlakken in lime).

## Letters

- **Young Serif** voor koppen. Eén gewicht, nooit cursief en nooit in kapitalen. Koppen zijn kort en noemen iets ("Eten & drinken", "De Heerenkamer").
- **Figtree** voor alle overige tekst, zonder kapitalen-tekst. Lijsttekst (menu, tijden) is minimaal 16px. Prijzen staan in `font-variant-numeric: tabular-nums` op een vaste rechterkolom.
- Beide fonts worden lokaal meegeleverd in `assets/fonts/` (woff2, OFL) en geladen met `font-display: swap`.

## Beeld

- Alleen eigen foto's uit `assets/` (webversies in `assets/img/`). Rechte hoeken, geen filters, **geen tekst op foto's**.
- Ontbreekt een foto, dan blijft het vak weg of gebruiken we een andere eigen foto. Nooit stockbeeld.
- Elke foto heeft een beschrijvende alt-tekst in het Nederlands.
- Hover op een gelinkte foto: zoom 1.03 binnen het kader, 400 ms ease-out.

## Componenten

- **Header:** wijnrood, met het witte logo links en de navigatie (Eten & drinken · High tea & wine · Groepen · Vacatures · Contact) en de knop **Reserveer** rechts. Op mobiel: logo, Reserveer en een menuknop; het menu opent als volledig scherm op wijnrood.
- **Reserveerknop:** opent de Guestplan-widget (`_gstpln.openWidget()`). Zonder JavaScript gaat de link naar `contact.html#reserveren` (telefoon). Op mobiel staat er onderaan altijd een balk met *Reserveer een tafel* en *Bel*.
- **Knoppen:** één primaire stijl (kalk op wijn, wijn op kalk) en één tekstlink-stijl met een onderstreping die bij hover aangroeit. Hoeken 2px. Hover: −1px omhoog. Ingedrukt: terug.
- **Menurij:** gerechtnaam (Figtree 600) en prijs rechts, daaronder de ingrediënten in `ink-soft`, gescheiden door "·" in plaats van "|".
- **Vandaag-strook:** wordt met JS berekend uit de openingstijden ("Vandaag open tot 00:00 · keuken 11:00–22:00", of "Maandag gesloten · dinsdag weer open vanaf 10:30"). Zonder JS staat er een statische samenvatting.
- **Formulieren (Formspree):** labels boven de velden, foutmeldingen onder het veld met tekst en `aria-describedby`, en de stappen arrangement → aantal en datum → gegevens.

## Ritme en layout

- Mobile-first. De wrap is 1200px met 16px gutter op mobiel en 32px vanaf 768px. Geen horizontale scroll.
- Sectieruimte `clamp(4.5rem, 9vw, 8rem)`. Boven een kop meer ruimte dan eronder.
- Composities wisselen per sectie, nooit twee keer dezelfde opbouw na elkaar: split, drie rijen, band, paar, tekst met foto, tabel.
- Beweging: alleen hover en focus, plus het openen van het mobiele menu. Geen scroll-reveals. `prefers-reduced-motion` zet alles stil.

## Niet doen

Italiaanse of Spaanse clichés (vlaggen, olijftakken, "trattoria"). Kapitalen voor lopende tekst. Tekst in afbeeldingen. Verzonnen reviews of cijfers. Een kicker of eyebrow boven koppen, buiten de twee verdiepingsaanduidingen. Kaartenrijen met icoon, kop en tekst. Dark mode.
