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

All måling går via `window.ndTrack()` i `public/assets/site.js`. Hendelser som skjer før besøkende har svart på samtykkebanneret, venter i kø og sendes etter at samtykkeinnstillingen er satt. Ingen navn, e-post, telefon eller meldingstekst sendes til Google.

| Hendelse | Når | Parametere | Er det et lead? |
| --- | --- | --- | --- |
| `generate_lead` | /takk vises etter at et skjema faktisk er sendt i samme økt | `skjema` (kontakt / pakkeguide), `side` (siden skjemaet ble sendt fra), `tjeneste` (valget i kontaktskjemaet) eller `pakke` (pakken guiden anbefalte) | **Ja.** Dette er den reelle henvendelsen. |
| `guide_fullfort` | Pakkeguiden viser en anbefaling. Én gang per svarkombinasjon per sidevisning. | `guide` (logo og profil / nettside), `anbefalt` (pakkenavn) | Nei. Interesse, ikke henvendelse. |
| `kontakt_klikk` | Klikk på booking (Calendly), telefon eller e-post | `metode` (booking / ring / epost), `side` | Nei. Et klikk, ikke en avtale. Selve bookingen i Calendly måles ikke. |

**Ingen dobbelttelling:** når et skjema sendes, lagres skjemanavn, side og pakke/tjeneste i `sessionStorage` (nøkkel `nd-lead`). På /takk brukes det én gang og slettes. Oppdatering av /takk, eller direkte besøk, gir ingen ny `generate_lead`. Det samme gjelder Google Ads-konverteringen når den slås på.

**Fasit for antall henvendelser er Netlify Forms** (Netlify → Forms). GA4 viser hvor henvendelsene kommer fra. Små avvik er normalt: blokkert sporing og spam som Netlify avviser.

## Slik følger du resultatene i GA4

**Én gang (5 min):** Admin → Egendefinerte definisjoner → Opprett egendefinert dimensjon, omfang **Hendelse**, for hver av disse: `skjema`, `side`, `tjeneste`, `pakke`, `guide`, `anbefalt`, `metode`. Data vises bare fra den dagen dimensjonen er laget.

**Nøkkelhendelser:** Admin → Hendelser. `generate_lead` skal være merket som nøkkelhendelse (lead). `kontakt_klikk` kan være nøkkelhendelse som sekundær konvertering. `guide_fullfort` skal ikke være nøkkelhendelse.

**Rapporter:**
- *Antall leads og kilde:* Rapporter → Engasjement → Hendelser → `generate_lead`. Legg til dimensjonen `skjema` for kontaktskjema mot pakkeguide, og `side` for hvilken side de kom fra.
- *Hvilke kanaler gir leads:* Rapporter → Anskaffelse → Trafikkanskaffelse, med nøkkelhendelse `generate_lead`.
- *Pakkeguiden:* Utforsk → Traktutforsking med stegene `page_view` på /finn-riktig-pakke/ → `guide_fullfort` → `generate_lead` med `skjema` = pakkeguide.
- *Klikk:* `kontakt_klikk` fordelt på `metode` og `side`.

**Testing uten å påvirke tallene:** åpne siden med GA4 DebugView (Admin → DebugView) og Tag Assistant. Ikke send testinnsendinger til produksjon uten avtale. Merk dem i så fall «TEST» og slett dem i Netlify etterpå.
