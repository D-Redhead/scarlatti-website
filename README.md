# Restaurant Scarlatti — statische website

Zes pagina's, puur HTML/CSS/JS. Geen CMS, geen build-stap nodig om te hosten.

```
index.html  menukaarten.html  highs.html  groepen.html  vacatures.html  contact.html
css/style.css   js/main.js   assets/ (foto's)
build.py          ← genereert de .html-bestanden (gedeelde header/footer)
fetch-assets.sh   ← haalt de foto's van de huidige site naar assets/
```

## Starten
1. `bash fetch-assets.sh` — vult `assets/` (12 foto's, verkleind naar max. 1800 px).
2. Open `index.html` of draai `python3 -m http.server` en ga naar http://localhost:8000.

## Aanpassen
- Teksten, menu en prijzen staan in `build.py` (lijsten `LUNCH`, `DINER`, `FONDUE`, `BORREL`). Pas aan en draai `python3 build.py`.
- Openingstijden staan op twee plekken: `HOURS_TABLE` in `build.py` (weergave) en `HOURS` in `js/main.js` (open/dicht-status).
- Kleuren en fonts: bovenaan `css/style.css` (`:root`).

## Reserveren
- Alle knoppen met `data-book` openen de Guestplan-widget (`_gstpln.openBookingWidget()`).
  Laadt de widget niet, dan gaat de knop naar `contact.html#reserveren` met telefoonnummer.
- Op mobiel staat onderin op elke pagina een vaste balk: **Tafel reserveren** + **Bel**.
- Groepen (10–70 p.) hebben een eigen route: `groepen.html#aanvraag`. Het formulier opent een
  vooraf ingevulde e-mail naar info@scarlatti-leiden.nl (geen server nodig).

## Toegankelijkheid (WCAG 2.2 AA)
Skiplink, zichtbare focus, tikdoelen ≥ 44 px, `aria-current` in navigatie, menu sluit met Esc,
formulieren met labels + foutmeldingen via `aria-live`, `prefers-reduced-motion` gerespecteerd,
tekstcontrast ≥ 4.5:1.

## Nog te doen
- Engelse versie (`/en/`) — structuur is klaar om te dupliceren.
- Openingstijden, prijzen en vacatures controleren op actualiteit.
- `_gstpln.open=false` staat uit zodat de zwevende Guestplan-knop niet over de mobiele balk valt; testen op productie.
- Logo: nu een typografisch woordmerk; vervang door het SVG-logo zodra beschikbaar.
