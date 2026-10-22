# Sporing og måling – noedesign.no

All sporing styres fra `public/assets/config.js`. Tomme felter = ingen sporing, ingen samtykkebanner.

## 1. Google Analytics 4
1. analytics.google.com → Opprett eiendom «noedesign.no» (tidssone Oslo, valuta NOK).
2. Legg til nettstrøm for `https://noedesign.no`. Kopier måle-ID-en (`G-…`).
3. Lim inn som `GA4_ID` i `config.js`.
4. Under Admin → Hendelser: merk `generate_lead` og `kontakt_klikk` som nøkkelhendelser.

## 2. Google Search Console
1. search.google.com/search-console → Legg til domene `noedesign.no` (DNS-verifisering, TXT-post hos DNS-leverandøren).
2. Send inn `https://noedesign.no/sitemap.xml`.

## 3. Google Ads (når siden har måling som virker)
1. Mål → Konverteringer → Ny → Nettsted → manuelt med kode.
2. Navn «Lead – skjema», kategori «Send inn skjema for potensielle kunder».
3. Fra koden: `AW-…` → `ADS_ID`, delen etter skråstreken → `ADS_LEAD_LABEL`.
4. Koble Ads og GA4 (GA4 Admin → Produktkoblinger).

## Hva som måles
- `generate_lead` (GA4) og Ads-konvertering: når noen lander på `/takk` etter skjema.
- `kontakt_klikk` med `metode` = ring / epost / booking.
- Consent Mode v2: alt er «denied» til besøkende godtar.
