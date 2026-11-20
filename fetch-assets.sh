#!/usr/bin/env bash
# Wordt aangeroepen door .github/workflows/testserver.yml (GitHub Pages-testserver), vóór het samenstellen van _site/.
# Sinds de redesign staan alle foto's, lettertypes en menukaart-PDF's al in de repo, dus er hoeft niets opgehaald te worden.
# De workflow kopieert zelf alleen de bestanden in de root; daarom zet dit script de Engelse versie (en/) alvast klaar,
# met dezelfde noindex-tag als de rest van de testsite. (De workflow zelf aanpassen vraagt de GitHub 'workflow'-scope.)
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p _site
cp -r en _site/
sed -i 's#<head>#<head>\n  <meta name="robots" content="noindex, nofollow">#' _site/en/*.html
echo "Engelse versie klaargezet in _site/en/."
