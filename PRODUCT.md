# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Statische HTML/CSS/JS, geen framework, geen build-stap en geen nieuwe dependencies zonder akkoord van de eigenaar. Testhosting via GitHub Pages (repo D-Redhead/scarlatti-website). Mobile-first.

## Users

- **Lunch- en borrelgasten.** Leidenaren en bezoekers van de binnenstad die willen weten of ze vandaag kunnen aanschuiven, wat er op de kaart staat en of het terras open is. Ze kijken meestal op hun telefoon, vaak onderweg.
- **Dinergasten.** Ze kijken naar de kaart en in het seizoen naar de kaasfondue (september–april), en reserveren daarna.
- **High tea / high wine-gasten.** Vriendinnen, babyshowers en kleine gezelschappen van 2–30 personen. High tea en high wine worden geserveerd op di, wo, do en zo.
- **Groepsorganisatoren.** Mensen die een afstudeerborrel, verjaardag, jubileum, groepslunch of -diner of een dinerspel regelen in de Heerenkamer (30 zittend, 70 staand). Ze willen weten wat het kost, welke voorwaarden gelden en hoe ze een voorstel aanvragen.
- **Zakelijke vergaderaars.** Ze worden doorverwezen naar Boutique Hotel d'Oude Morsch, een zusterbedrijf met dezelfde eigenaren.
- **Sollicitanten.**

## Product Purpose

De website van Restaurant Scarlatti, Stille Mare 4, Leiden. De site moet bezoekers laten reserveren (Guestplan, met één tik vanaf elke pagina), groepsaanvragen binnenhalen en de praktische informatie helder geven: tijden, kaart, prijzen, bereikbaarheid. Succes betekent meer reserveringen en groepsaanvragen, en minder telefoontjes met vragen die de site had moeten beantwoorden.

## Positioning

Restaurant aan het water in hartje Leiden, met een zonnig terras en een sfeervolle Heerenkamer op de eerste verdieping (open haard, daglicht, eikenhouten vloer). Sinds de jaren '80 een begrip in Leiden. Het begon als theehuis dat de toenmalige eigenaar vernoemde naar de componist Domenico Scarlatti. Open voor lunch, borrel, diner en high tea/high wine.

**Niet** positioneren als Italiaans of Spaans restaurant. De keuken alleen beschrijven zoals de huidige site dat doet: "gevarieerde menukaart", verse gerechten, huisgemaakt.

## Operating Context

- Reserveren gaat via de Guestplan-widget (accessKey in `_audit/content.md`).
- Groepsaanvragen gaan via een Formspree-formulier ([AANVULLEN: Formspree-endpoint]) met de velden van de huidige site: arrangement, aantal gasten, datum, tijd, voornaam, achternaam, telefoon, e-mail.
- Contact en factuurgegevens gaan ook via Formspree, met een eigen endpoint per formulier en dezelfde velden als nu.
- Solliciteren gaat via de bestaande Link Hospitality-widget (geen balk bovenaan meer, wel een knop op de vacaturepagina).
- Gifty (cadeaubonnen) vervalt.
- Een dinerspel boek je extern via dinerspel.nl. Vergaderen verloopt via boutiquehoteldeoudemorsch.nl/vergaderruimte/ en moet makkelijk te vinden zijn.
- Menukaarten bestaan als PDF (lunch, diner, borrel incl. drankkaart) en als HTML.

## Capabilities and Constraints

- Openingstijden: ma gesloten · di–do en zo 10:30–00:00 · vr–za 10:30–01:00. Keuken open 11:00–22:00. Lunch 11:00–16:30, diner vanaf 17:00. Geen ontbijt.
- Het pand is niet rolstoeltoegankelijk. Dat vermelden we eerlijk bij de praktische info.
- Nederlands is leidend. Er komt een Engelse versie als letterlijke vertaling, pas na akkoord op NL.
- Geen blog, webshop, login, betalingen, CMS of dark mode.
- Alle feiten komen uit `_audit/content.md` en uit de aanvullende feiten hierboven. Wat ontbreekt markeren we als `[AANVULLEN: …]`.

## Brand Commitments

- Naam: Restaurant Scarlatti, met de ondertitel "Lunch & Diner" in het logo.
- Bestaand logo (wit script-wordmark, `assets/Scarlatti-Logo-Wit.png`) en favicon (rode S).
- Bestaande huisstijlkleur: diep wijnrood (circa #8f0b2f). Dit is geen bindende eis, maar de herkenbaarheid van het logo en het rood blijft gewenst.
- Toon: warm, informeel, je-vorm ("Voel je welkom bij Restaurant Scarlatti!", "Tot snel!").

## Evidence on Hand

- Eigen fotografie in `assets/` (terras aan het water met uithangbord, Heerenkamer, bar, gerechten, high tea, kaasfondue, teamfoto).
- Menu's en prijzen in `_audit/content.md` en `_audit/menukaarten/*.pdf`.
- **Afwezig, dus niet verzinnen:** reviews, beoordelingscijfers, klantnamen, teamnamen, awards, persvermeldingen, een foto vanaf het water en een logo als vector.

## Product Principles

1. Reserveren is altijd één tik weg, op elke pagina en elke schermbreedte.
2. De praktische info (open vandaag, keukentijden, adres, toegankelijkheid) staat vooraan, niet onderaan.
3. Het water, het terras en de Heerenkamer zijn het verhaal. De foto's zijn echt en de feiten kloppen.
4. Groepsinformatie is volledig, eerlijk over kosten en voorwaarden, en staat één keer op de site in plaats van vijf keer herhaald.

## Accessibility & Inclusion

WCAG 2.2 AA. Geen informatie die alleen in afbeeldingen staat. Leesbare lopende tekst, dus geen kapitalen. Bedienbaar met toetsenbord. Vermeld eerlijk dat het pand niet rolstoeltoegankelijk is.
