#!/usr/bin/env python3
"""Bygger noedesign.no som statiske sider i /public.

Kjør:  python3 build/build.py
Alt innhold ligger i build/pages.py. Bilder ligger ferdig konvertert i public/img.
"""
import json, os, re, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pages as P  # noqa: E402

SITE = "https://noedesign.no"
CAL = "https://calendly.com/noedesign-info/30min"
TEL = "+4746938750"
TEL_SHOW = "46 93 87 50"
MAIL = "info@noedesign.no"
LINKEDIN = "https://www.linkedin.com/company/noedesign"
VERSION = "28"

IMG_WIDTHS = {}
for f in (PUB / "img").glob("*.webp"):
    m = re.match(r"(.+)-(\d+)\.webp$", f.name)
    if m:
        IMG_WIDTHS.setdefault(m.group(1), []).append(int(m.group(2)))
for k in IMG_WIDTHS:
    IMG_WIDTHS[k].sort()


def esc(s):
    return html.escape(s, quote=True)


def pic(name, alt, sizes="(max-width: 860px) 100vw, 50vw", eager=False, cls="", ratio=None):
    ws = IMG_WIDTHS.get(name)
    if not ws:
        raise SystemExit(f"Mangler bilde: {name}")
    srcset = ", ".join(f"/img/{name}-{w}.webp {w}w" for w in ws)
    default = ws[-1] if ws[-1] <= 1280 else (1280 if 1280 in ws else ws[0])
    from PIL import Image  # bare for å lese mål
    with Image.open(PUB / "img" / f"{name}-{ws[0]}.webp") as im:
        w, h = im.size
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="/img/{name}-{default}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{esc(alt)}" {load}>')


BUSINESS = {
    "@type": "ProfessionalService",
    "@id": f"{SITE}/#business",
    "name": "noedesign",
    "url": SITE,
    "description": "Grafisk designer i Oslo. Logo, visuell profil, nettside og film for små bedrifter, til fast pris.",
    "telephone": "+47 46 93 87 50",
    "email": MAIL,
    "image": f"{SITE}/img/og-default.jpg",
    "logo": f"{SITE}/img/noedesign-dark.png",
    "address": {"@type": "PostalAddress", "addressLocality": "Oslo", "addressCountry": "NO"},
    "areaServed": [{"@type": "City", "name": "Oslo"}, {"@type": "Country", "name": "Norge"}],
    "priceRange": "kr 8 990–49 990",
    "founder": {"@type": "Person", "name": "Marius Moen", "jobTitle": "Grafisk designer", "image": f"{SITE}/img/marius-640.webp"},
    "foundingDate": "2018",
    "legalName": "Moen Design",
    "vatID": "NO921420544MVA",
    "identifier": {"@type": "PropertyValue", "propertyID": "orgnr", "value": "921420544"},
    "sameAs": [LINKEDIN],
}

NAV = [("/arbeid", "Arbeid"), ("/priser", "Tjenester og priser"), ("/om", "Om"), ("/kontakt", "Kontakt")]


def header(path):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if path == h or (h != "/" and path.startswith(h + "/")) else ""}>{t}</a>'
        for h, t in NAV)
    mlinks = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<a class="skip" href="#innhold">Hopp til innholdet</a>
<header class="site-header"><div class="wrap hdr">
  <a class="logo" href="/" aria-label="noedesign, til forsiden"><img src="/img/noedesign-dark.png" width="520" height="111" alt="noedesign"></a>
  <nav class="nav" aria-label="Hovedmeny"><span class="nl">{links}</span><span class="nr"><a class="tel" href="tel:{TEL}">{TEL_SHOW}</a><a class="btn" href="/finn-riktig-pakke">Finn riktig pakke</a></span></nav>
  <details class="menu"><summary>Meny</summary><div class="panel">{mlinks}<a class="btn" href="/finn-riktig-pakke">Finn riktig pakke</a></div></details>
</div></header>'''


def footer():
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="fgrid">
    <div class="stack">
      <a class="logo" href="/" aria-label="noedesign"><img src="/img/noedesign-light.png" width="520" height="111" alt="noedesign" loading="lazy"></a>
      <p style="color:var(--on-dark-muted);max-width:34ch">Logo, nettside og film for små bedrifter i Oslo. Fra én designer, til fast pris.</p>
    </div>
    <div><h2>Tjenester</h2><ul>
      <li><a href="/logo-design">Logodesign</a></li><li><a href="/startpakke">Startpakke</a></li>
      <li><a href="/visuell-profil">Visuell profil</a></li><li><a href="/nettside">Nettside</a></li>
      <li><a href="/grafisk-design">Grafisk design og trykk</a></li><li><a href="/kafe-og-restaurant">Kafé og restaurant</a></li>
    </ul></div>
    <div><h2>Mer</h2><ul>
      <li><a href="/arbeid">Arbeid</a></li><li><a href="/priser">Tjenester og priser</a></li><li><a href="/finn-riktig-pakke">Finn riktig pakke</a></li>
      <li><a href="/om">Om meg</a></li><li><a href="/personvern">Personvern</a></li>
    </ul></div>
    <div><h2>Kontakt</h2><ul>
      <li><a href="tel:{TEL}">{TEL_SHOW}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li>
      <li><a href="{CAL}" target="_blank" rel="noopener">Book en gratis prat</a></li>
      <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li><li>Oslo</li>
    </ul></div>
  </div>
  <div class="bottom"><span>© noedesign · Moen Design · Org.nr. 921 420 544 MVA</span><span>Svar innen én arbeidsdag</span></div>
</div></footer>
<div class="mobilebar"><a class="btn ghost" href="tel:{TEL}">Ring</a><a class="btn" href="{CAL}" target="_blank" rel="noopener">Book en prat <span class="sq" aria-hidden="true"></span></a></div>'''


def contact_form(title="Fortell kort om bedriften din", default_service=""):
    opts = ["Vet ikke ennå", "Logo", "Startpakke", "Visuell profil", "Nettside", "Profil + nettside", "Trykksaker", "Film"]
    o = "".join(f'<option{" selected" if x == default_service else ""}>{x}</option>' for x in opts)
    return f'''<form class="form-card" name="kontakt" method="POST" action="/takk" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="kontakt">
  <p class="hp"><label>Ikke fyll ut dette feltet <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
  <h3 class="h-m">{title}</h3>
  <p class="small muted">Jeg svarer innen én arbeidsdag, med et forslag og en fast pris.</p>
  <div class="row2">
    <div class="field"><label for="k-navn">Navn</label><input id="k-navn" name="navn" required autocomplete="name"></div>
    <div class="field"><label for="k-epost">E-post</label><input id="k-epost" name="epost" type="email" required autocomplete="email"></div>
  </div>
  <div class="row2">
    <div class="field"><label for="k-tel">Telefon <span class="valgfri">(valgfritt)</span></label><input id="k-tel" name="telefon" type="tel" autocomplete="tel"></div>
    <div class="field"><label for="k-bedrift">Bedrift <span class="valgfri">(valgfritt)</span></label><input id="k-bedrift" name="bedrift" autocomplete="organization"></div>
  </div>
  <div class="row2">
    <div class="field"><label for="k-tjeneste">Hva trenger du?</label><select id="k-tjeneste" name="tjeneste">{o}</select></div>
    <div class="field"><label for="k-budsjett">Budsjett (eks. mva)</label><select id="k-budsjett" name="budsjett"><option>Vet ikke</option><option>Logo, fra 8 990 kr</option><option>Startpakke, 14 990 kr</option><option>Nettside, fra 24 990 kr</option><option>Visuell profil, fra 29 990 kr</option><option>Profil + nettside, fra 49 990 kr</option><option>Over 50 000 kr</option></select></div>
  </div>
  <div class="field"><label for="k-melding">Kort om prosjektet</label><textarea id="k-melding" name="melding" required placeholder="Hva gjør bedriften, og hva trenger du hjelp med?"></textarea></div>
  <p class="small muted">Jeg bruker opplysningene dine bare til å svare på henvendelsen. Les mer i <a class="textlink" href="/personvern">personvernerklæringen</a>.</p>
  <div class="btns"><button class="btn" type="submit">Send <span class="sq" aria-hidden="true"></span></button><span class="small muted">eller <a class="textlink" href="{CAL}" target="_blank" rel="noopener">book en gratis prat</a></span></div>
</form>'''


def cta_band(title="Klar for å komme i gang?", text=None, service=""):
    text = text or "Book en gratis prat på 30 minutter, eller send en kort melding. Du får en fast pris før noe starter."
    return f'''<section class="section dark" id="kontakt"><div class="wrap cta-band">
  <div class="stack-l">
    <div class="stack"><span class="eyebrow">Kontakt</span><h2 class="h-l">{title}</h2><p class="lede">{text}</p></div>
    <div class="contact-list">
      <a href="{CAL}" target="_blank" rel="noopener"><span>Book en gratis prat</span><b>30 minutter, video eller telefon</b></a>
      <a href="tel:{TEL}"><span>Ring</span><b>{TEL_SHOW}</b></a>
      <a href="mailto:{MAIL}"><span>E-post</span><b>{MAIL}</b></a>
    </div>
  </div>
  {contact_form(default_service=service)}
</div></section>'''


def breadcrumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
                                for i, (n, u) in enumerate(items)]}


def crumbs_html(items):
    parts = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<span aria-current="page">{esc(n)}</span>')
        else:
            parts.append(f'<a href="{u}">{esc(n)}</a><span aria-hidden="true">/</span>')
    return f'<nav class="crumbs" aria-label="Brødsmuler">{"".join(parts)}</nav>'


def page(path, title, desc, body, page_id, ld=None, noindex=False, og=None, scripts=""):
    canonical = SITE + (path if path != "/" else "/")
    og_img = SITE + "/img/" + (og or "og-default.jpg")
    lds = [dict({"@context": "https://schema.org"}, **BUSINESS)] + (ld or [])
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    robots = '<meta name="robots" content="noindex, follow">' if noindex else ""
    return f'''<!doctype html>
<html lang="no">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:locale" content="nb_NO"><meta property="og:site_name" content="noedesign">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{og_img}">
<meta name="theme-color" content="#F4F4F1">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/newsreader-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/hanken-grotesk-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={VERSION}">
{ld_html}
</head>
<body data-page="{page_id}">
{header(path)}
<main id="innhold">
{body}
</main>
{footer()}
<script src="/assets/config.js?v={VERSION}"></script>
<script src="/assets/site.js?v={VERSION}" defer></script>
{scripts}
</body>
</html>
'''


def write(path, content):
    out = PUB / ("index.html" if path == "/" else path.strip("/") + ("/index.html" if not path.endswith(".html") else ""))
    if path.endswith(".html"):
        out = PUB / path.strip("/")
    # Gult punktum: avsluttende punktum i hovedoverskriften får aksentfargen
    content = re.sub(r'(<h1 class="h-xl">.*?)\.</h1>', r'\1<span class="dot">.</span></h1>', content, count=1, flags=re.S)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")


def main():
    ctx = dict(pic=pic, esc=esc, cta_band=cta_band, contact_form=contact_form, crumbs_html=crumbs_html,
               breadcrumbs_ld=breadcrumbs_ld, CAL=CAL, TEL=TEL, TEL_SHOW=TEL_SHOW, MAIL=MAIL, SITE=SITE, LINKEDIN=LINKEDIN)
    built = P.build_all(ctx)
    problems = []
    urls = []
    for pg in built:
        t, d = pg["title"], pg["desc"]
        if not pg.get("noindex"):
            if not (40 <= len(t) <= 62): problems.append(f"Tittel {len(t)} tegn: {pg['path']} – {t}")
            if not (120 <= len(d) <= 160): problems.append(f"Beskrivelse {len(d)} tegn: {pg['path']}")
            if pg["path"] != "/404.html": urls.append(pg["path"])
        if pg["body"].count("<h1") != 1: problems.append(f"H1-antall {pg['body'].count('<h1')}: {pg['path']}")
        write(pg["path"], page(pg["path"], t, d, pg["body"], pg["id"], pg.get("ld"), pg.get("noindex"), pg.get("og"), pg.get("scripts", "")))
    sm = "".join(f"<url><loc>{SITE}{u}</loc></url>" for u in urls)
    (PUB / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n', encoding="utf-8")
    (PUB / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /takk\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print(f"Bygget {len(built)} sider.")
    for p in problems: print("ADVARSEL:", p)


if __name__ == "__main__":
    main()
