# Nog aan te vullen of te controleren

Stand van zaken: 19-11-2026, Nederlandse versie (14 pagina's). De Engelse versie volgt na akkoord.

## [AANVULLEN] – verplicht vóór livegang

| # | Wat | Waar | Hoe |
|---|---|---|---|
| 1 | **Formspree-endpoint groepsaanvraag** | `groepen.html`, `action="https://formspree.io/f/AANVULLEN-groepsaanvraag"` (staat bij de HTML-commentaar `[AANVULLEN: Formspree-endpoint groepsaanvraag]`) | Maak een formulier aan op formspree.io en vervang de URL. Tot die tijd meldt het formulier netjes dat het nog niet gekoppeld is en verwijst het naar telefoon en mail. |
| 2 | **Formspree-endpoint contact** | `contact.html`, `AANVULLEN-contact` | idem |
| 3 | **Formspree-endpoint factuurgegevens** | `factuurgegevens.html`, `AANVULLEN-factuur` | idem |

## Placeholders en ontbrekende assets

Er staan geen beeld-placeholders op de site: elke sectie heeft een eigen foto van de huidige site. Wel ontbreken deze bestanden of zouden ze helpen:

| # | Wat | Waarom |
|---|---|---|
| 4 | Logo als **SVG** (of een grotere PNG), wit én donker | Het enige beschikbare logo is een witte PNG van 300×162 px. Op retina-schermen is het net niet haarscherp, en er is geen donkere versie voor gebruik op een lichte achtergrond. |
| 5 | Grotere versies (≥1600 px) van `MG_8635` (steak), `MG_8845` (borrelhapjes) en `MG_8576` (flammkuchen) | Op de huidige site staan deze foto's alleen in 720 px breed. Ze worden gebruikt op de homepage en op de pagina's Eten & drinken en Borrel. |
| 6 | Eventueel: een foto van het pand of terras **vanaf het water** en een interieurfoto van het restaurant beneden overdag | Er is geen gat op de site, maar deze foto's zouden "aan het water" en de begane grond sterker laten zien. |
| 7 | **Teamnamen** | Ze stonden niet op de huidige site en zijn dus niet opgenomen. Als je ze wilt tonen, lever ze aan, dan voeg ik een sectie toe. |

## Hosting: eerst een testronde via GitHub en Netlify, later live via Plesk

**Testronde (GitHub + Netlify):** zet de inhoud van `redesign/` in de repo `D-Redhead/scarlatti-website` en koppel die aan Netlify. Laat de build command leeg en zet de publish directory op de map met `index.html`. Er is geen build-stap. Aandachtspunten tijdens de test:
- **Staat live op https://scarlatti-testsite.netlify.app** (deploy van 19-11-2026). Alle pagina's geven HTTP 200. Er staat een `X-Robots-Tag: noindex` op, zodat Google de testsite niet indexeert naast de echte site. Dat staat in het `_headers`-bestand van de deploy, niet in `redesign/`.
- De Guestplan-widget werkt op het Netlify-adres: de reserveerknop opent de echte widget. Op `*.github.io` is dat nog niet getest.
- Formspree werkt ook op Netlify. De formulieren melden "nog niet gekoppeld" tot de endpoints zijn ingevuld (punten 1–3).
- Doorverwijzingen van de oude WordPress-adressen zijn op de testomgeving niet nodig. Die komen pas bij de overstap naar Plesk (punt 10).

Uploaden naar Plesk: zet de inhoud van `redesign/` in `httpdocs/` van scarlatti-leiden.nl. Laat de werkmappen `_audit/` en `_screens/` en de bestanden `PRODUCT.md`, `DESIGN.md` en `AANVULLEN.md` weg. Er is geen PHP, database of build-stap nodig.

| # | Wat |
|---|---|
| 8 | De **Guestplan-widget** gebruikt de accessKey van de huidige site. Op het eigen domein via Plesk werkt hij naar verwachting zoals nu. Op `github.io` (test) kan Guestplan het domein weigeren; de knop valt dan terug op `contact.html#reserveren` (telefoon). |
| 9 | De **Link Hospitality**-sollicitatiebalk staat alleen op `vacatures.html`. Controleer na livegang dat hij verschijnt. |
| 10 | **Oude WordPress-adressen** (`/menukaarten/`, `/staff-wanted/`, `/groepsmenu/` enz.) bestaan straks niet meer. Zonder 301-doorverwijzingen geven links uit Google en social media een 404. [AANVULLEN: akkoord op een `.htaccess` met doorverwijzingen; Plesk draait standaard Apache achter nginx, dus dat werkt.] |
| 11 | **HTTPS**: zet in Plesk het Let's Encrypt-certificaat aan en kies "permanente 301-doorverwijzing van HTTP naar HTTPS". De canonieke URL's wijzen naar `https://www.scarlatti-leiden.nl/`, dus kies ook www als voorkeursdomein. |
| 12 | Maak een **back-up van de huidige WordPress-site** in Plesk voordat je de bestanden vervangt. |
| 13 | De menuprijzen staan zowel in de HTML als in de PDF's (`assets/menukaarten/*_nov26.pdf`). Werk bij een nieuwe kaart beide bij. |

## Bewuste keuzes (ter info)

- **Gifty (cadeaubonnen)** is weggelaten, op jouw verzoek.
- De **Google Maps-embed** is vervangen door een routelink. Dat laadt sneller en er worden geen cookies van derden geplaatst vóór toestemming.
- De **cookiebalk** is vervallen. De nieuwe site plaatst zelf geen tracking-cookies. Guestplan en Link Hospitality laden wel scripts van derden. [AANVULLEN: laat juridisch checken of daarvoor een cookiemelding nodig is.]
- Het blok "Goed om te weten" stond vijf keer op de oude site. Het staat nu volledig op `groepen.html#goed-om-te-weten`. De subpagina's tonen alleen hun eigen afspraken en linken door.
- De meta-tekst van de oude contactpagina noemde de "Stille Rijn". Dat is gecorrigeerd naar Stille Mare.
