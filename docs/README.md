# noedesign.no

Statisk side, generert med Python.

- Innhold: `build/pages.py` (sider, priser, sitater, caser)
- Mal og hjelpefunksjoner: `build/build.py`
- Bygg: `python3 build/build.py` → skriver til `public/`
- Netlify publiserer `public/` direkte (ingen byggkommando). Redirects fra gamle Wix-URL-er ligger i `netlify.toml`.
- Sporing: fyll inn ID-er i `public/assets/config.js`. Tomt = ingen sporing og ingen samtykkebanner.
- Skjemaer: Netlify Forms («kontakt» og «pakkeguide»). Slå på formdeteksjon i Netlify.

## Priser (eks. mva)
Logo fra 8 990 · Startpakke 14 990 · Visuell profil fra 29 990 · Nettside fra 24 990 · Profil + nettside fra 49 990 · Trykksaker fra 3 990 per produkt · Timepris 1 150 · Film etter avtale

## Må fylles inn før lansering
- GA4/Ads-ID i config.js
