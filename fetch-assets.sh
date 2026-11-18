#!/usr/bin/env bash
# Haalt de foto's van de huidige site op naar assets/ en verkleint ze voor het web.
# Gebruik:  bash fetch-assets.sh        (vereist curl; sips (macOS) of ImageMagick optioneel)
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p assets
U="https://scarlatti-leiden.nl/wp-content/uploads"
while read -r name src; do
  [ -z "$name" ] && continue
  echo "→ assets/$name"
  curl -fsSL "$U/$src" -o "assets/$name"
  [[ "$name" == *.png ]] && continue
  if python3 -c "import PIL" 2>/dev/null; then
    python3 - "assets/$name" <<'PY'
import sys
from PIL import Image, ImageOps
p = sys.argv[1]
im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
im.thumbnail((1600, 1600))
im.save(p, "JPEG", quality=74, optimize=True, progressive=True)
PY
  elif command -v sips >/dev/null; then sips -Z 1800 -s formatOptions 78 "assets/$name" >/dev/null
  elif command -v magick >/dev/null; then magick "assets/$name" -resize '1800x1800>' -quality 78 -strip "assets/$name"
  elif command -v convert >/dev/null; then convert "assets/$name" -resize '1800x1800>' -quality 78 -strip "assets/$name"
  fi
done <<'LIST'
gevel.jpg            2024/07/20170727Scarlatti27-scaled.jpg
uithangbord.jpg      2026/06/MG_3453-3.jpg
lunch.jpg            2026/06/MG_3289.jpg
hightea.jpg          2025/01/MG_7179.jpg
hightea-etagere.jpg  2025/01/MG_7147.jpg
fondue.jpg           2026/09/MG_7058.jpg
heerenkamer.jpg      2025/10/2023_Heerenkamer-15-scaled.jpeg
openhaard.jpg        2025/04/MG_7221.jpg
terras.jpg           2025/04/MG_8360-1.jpg
borrel.jpg           2025/04/MG_8845-e1746000609563.jpg
wijn.jpg             2025/04/MG_8433-rotated-e1746001534530.jpg
stad.jpg             2025/08/MG_9456.jpg
logo-wit.png         2017/06/Scarlatti-Logo-Wit.png
LIST
echo "Klaar."
