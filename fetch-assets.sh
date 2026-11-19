#!/usr/bin/env bash
# Wordt aangeroepen door .github/workflows/testserver.yml.
# Sinds de redesign staan alle (verkleinde) foto's, lettertypes en menukaart-PDF's
# al in de repo (assets/img, assets/fonts, assets/menukaarten), dus er hoeft niets
# opgehaald te worden. Dit script blijft bestaan zodat de workflow ongewijzigd werkt.
echo "Assets staan al in de repo; niets op te halen."
