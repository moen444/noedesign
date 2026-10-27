"""Innhold for noedesign.no. Alle priser er eks. mva og står i docs/priser.md."""

PKGS = {
    "logo": dict(name="Logo", price="8 990", frm=True, url="/logo-design", num=8990,
                 for_="For deg som bare trenger en logo.",
                 inc=["Logo i 2 konsepter", "Én runde revisjon", "Varianter: liggende, stående og symbol", "Farger", "Filer som SVG og PNG, i mørk og lys variant, for skjerm og trykk"]),
    "start": dict(name="Startpakke", price="14 990", frm=False, url="/startpakke", num=14990,
                  for_="For deg som vil komme raskt i gang, uten strategifase.",
                  inc=["Logo med varianter og fargepalett", "Designhåndbok (PDF)", "Salgspresentasjon, 10–15 sider", "Én runde revisjon"]),
    "profil": dict(name="Visuell profil", price="29 990", frm=True, url="/visuell-profil", num=29990,
                   for_="For deg som vil bygge en hel merkevare, ikke bare komme i gang.",
                   inc=["Alt i Startpakken", "Strategimøte og 2–3 logokonsepter", "To runder revisjon", "Grafiske elementer og bildestil", "Fullstendig designmanual", "Maler: visittkort, brev, e-postsignatur og 3–5 for sosiale medier"]),
    "web": dict(name="Nettside", price="24 990", frm=True, url="/nettside", num=24990,
                for_="For deg som har profilen og trenger en side som gir henvendelser.",
                inc=["Opptil 5 sider", "Tilpasset mobil", "SEO-grunnoppsett", "Kontaktskjema"]),
}

QUOTES = {
    "madelene": ("Noe Design var veldig enkelt å samarbeide med og de skjønte kjapt hva jeg var ute etter. Jeg fikk hjelp med utvikling av et nytt design for våre logoer som skal representere vår bedrift fremover og være synlig på alle våre kaffekrus ut til kunden. Er kjempe fornøyd med både samarbeidet og resultatet så jeg kan virkelig anbefale Noe Design videre for lignende prosjekter og vårt samarbeid er absolutt ikke over enda. Effektiv, proff og engasjert!", "Madelene", "Java & Mocca"),
    "madelene_short": ("Er kjempe fornøyd med både samarbeidet og resultatet. Effektiv, proff og engasjert!", "Madelene", "Java & Mocca"),
    "kirsti": ("Rask og effektiv. Gode løsninger. Lett å kommunisere med. Anbefales til alle som ønsker ny logo/hjemmeside. Marius er superhyggelig og hjalp oss både av utvikling av siden - og senere med de oppdateringene vi ønsket.", "Kirsti", "Private Living Lofoten"),
    "caroline": ("Vi har hatt gleden av å samarbeide med Noedesign for å utvikle vår nye hjemmeside, og vi er svært fornøyde med resultatet. De var svært effektivt, og deres kreative ideer og tanker bidro til å gi nettsiden vår en frisk og moderne følelse som passer konseptet vårt bra. Anbefales!", "Caroline", "Bacalao Bar"),
    "james": ("Brukt Marius for å lage logo til en pizzeria. Rask, flink og enkel å jobbe sammen med! Anbefales!", "James", "Slice Pizza"),
    "johanne": ("For en fornøyelse å jobbe med Noe Design! Jeg hadde en idé om hva jeg ønsket for brandet mitt, og Marius leverte en pakke som var over all forventning.", "Johanne Regine Gustavsen", "Google-anmeldelse"),
    "elektro": ("En veldig god investering hvis man ønsker en tydeligere profil og et mer gjennomført førsteinntrykk.", "Elektro Kraft", "Startpakke"),
    "premiumruss": ("Det å få på plass en ferdig visuell identitet gjorde det mye enklere å fremstå profesjonelt og helhetlig.", "Premiumruss", "Startpakke"),
}

CASES = [
    dict(slug="roots-of-alpicella", name="Roots of Alpicella", kind="Vingård, Italia", tags="Logo · Profil · Nettside · Film", cover="roa-cover",
         title="Roots of Alpicella: profil, nettside og film for vingård",
         desc="Logo, designhåndbok, nettside og film for Roots of Alpicella, en liten vingård på 660 meter i de liguriske alpene. Hele merkevaren fra samme hånd.",
         lede="En ny vingård i Liguria, fra første skisse til ferdig nettside og film.",
         problem="Roots of Alpicella dyrker vin, oliven og grønnsaker uten sprøytemidler på gamle terrasser i Liguria. Prosjektet var helt nytt, uten logo eller nettside, og trengte et uttrykk som var like rolig og jordnært som stedet, og som fungerte på alt fra vinetikett til mobil.",
         solution="Jeg tegnet logoen: en kvinneprofil i én tynn linje, med vinblad og drueklase i håret, satt sammen med navnet. Rundt den laget jeg en designhåndbok med farger hentet fra logoen, typografi, tone og eksempler på etikett, visittkort og nettside. Nettsiden er bygget fra bunnen, med video fra innhøstingen, og jeg var på stedet for å filme og fotografere da druene ble plukket.",
         deliver=["Logo, symbol og ordmerke", "Designhåndbok", "Nettside tilpasset mobil", "Showreel og fortellerfilm fra innhøstingen", "Foto", "Konsept for merch"],
         images=[("roa-logo", "Roots of Alpicella-logoen på lys bakgrunn"), ("roa-web-mobile", "Tre sider fra nettsiden på mobil"), ("roa-handbook", "Forside og logoside i designhåndboken"), ("roa-colors", "Fargepalett og tone i designhåndboken"), ("roa-web-desk", "Vineyard-siden til Roots of Alpicella på en stor skjerm"), ("roa-harvest", "Hender ved et kar under innhøstingen"), ("roa-merch", "Konsept for t-skjorter og caps med ROA-ordmerket og logoen", "full")],
         hero_video=dict(src="/video/roa-showreel.mp4", mobile="/video/roa-showreel-mobile.mp4", poster="roa-showreel-poster"),
         film=dict(src="/video/roa-film.mp4", poster="roa-film-poster", eyebrow="Filmen", caption="Fortellerfilmen om Roots of Alpicella, filmet under innhøstingen. 2 minutter, med lyd."),
         quote=None, link=("https://rootsofalpicella.com", "rootsofalpicella.com")),
    dict(slug="elektro-kraft", name="Elektro Kraft", kind="Elektrotjenester, Bergen", tags="Logo · Designhåndbok · Profil", cover="ek-cover",
         title="Elektro Kraft: logo og designhåndbok for elektrikere",
         desc="Logo, symbol, farger, typografi og designhåndbok for Elektro Kraft. En Startpakke som gir et pålitelig og moderne førsteinntrykk.",
         lede="En identitet som skal få kundene til å føle seg trygge før de har snakket med noen.",
         problem="Elektro Kraft skulle fremstå som pålitelig, kompetent og moderne, med tydelig og direkte kommunikasjon. Kundene skal føle seg trygge på kvalitet og fagkunnskap, både på nett og på trykk.",
         solution="Jeg tegnet et symbol der bokstaven E møter en lynbolt, med diagonale linjer som gir bevegelse og energi. Logoen finnes i tre former: liggende, kvadratisk og som alene-stående symbol, slik at den fungerer fra nettside til profilbilde. Fargene er mørk marineblå med elektrisk blå som aksent, og navnet er satt i Montserrat, med ELEKTRO i bold og KRAFT i regular. Alt er samlet i en designhåndbok, så profilen blir brukt riktig videre.",
         deliver=["Logo i tre varianter", "Symbol og favicon", "Fargepalett og typografi", "Designhåndbok (PDF)", "Filer for skjerm og trykk"],
         images=[("ek-logo", "Elektro Kraft-logoen i liggende, kvadratisk og symbolversjon"), ("ek-symbol", "Symbolet med E og lynbolt i tre fargeversjoner"), ("ek-palett", "Fargepaletten i designhåndboken"), ("ek-font", "Eksempel på typografi i bruk")],
         quote="elektro", link=("https://elektrokraft.no", "elektrokraft.no")),
    dict(slug="kjeoya-lodge", name="Kjeøya Lodge", kind="Lodge, Lofoten", tags="Logo · Visuell profil · Nettsideretningslinjer", cover="kj-cover",
         title="Kjeøya Lodge: logo og visuell profil i Lofoten",
         desc="Logo med fjell og hytte, farger, typografi og retningslinjer for nettside til Kjeøya Lodge i Lofoten. En visuell profil som passer stedet.",
         lede="En profil med fjellet og hytta i midten, laget for en lodge i Lofoten.",
         problem="Kjeøya er en lodge i Lofoten og trengte en visuell profil som fungerer på nettsiden, i sosiale medier og i trykk, med et rolig uttrykk som passer stedet.",
         solution="Logoen har et fjellsymbol med en hytte under toppen, over navnet i Garamond Premier Pro Bold og «Lofoten» i grønn. Den finnes i flere formater, for nettside og for sosiale medier, i blågrønn og hvit. I tillegg tegnet jeg symboler, favicon og et bølgeikon til menyen. Fargene er dyp blågrønn og en lysere grønn, med Avenir Next og Baskerville som skrifter. Profilen inkluderer også retningslinjer for nettsiden: logo på mørk og lys bakgrunn, knapper og lenker.",
         deliver=["Logo i flere formater", "Symboler, favicon og menyikon", "Fargepalett og typografi", "Visuell profil (PDF)", "Retningslinjer for nettside"],
         images=[("kj-logo", "Kjeøya-logoen med fjell og hytte, symboler og fargepalett"), ("kj-web", "Retningslinjer for nettside og bruk av logo"), ("kj-font", "Typografi i den visuelle profilen"), ("kj-ny", "Kjeøya Lofoten-logoen i stående format")],
         quote=None),
    dict(slug="java-mocca", name="Java & Mocca", kind="Kaffebar, Oslo", tags="Logo · Kopper · Profil", cover="java-hero",
         title="Java & Mocca: logo og kopper for to kaféer i Oslo",
         desc="Nye logoer og take-away-kopper for Mocca Briskeby og Java St. Hanshaugen. Et helhetlig uttrykk for to av Oslos mest sjarmerende kaféer.",
         lede="To kaféer, to logoer og ett felles uttrykk som kundene tar med seg ut døra.",
         problem="Mocca Briskeby og Java St. Hanshaugen trengte logoer som passet atmosfæren i kaféene, og som fungerte der kundene faktisk ser dem: på koppen.",
         solution="Jeg tegnet nye logoer for begge kaféene og designet take-away-koppene, slik at de fikk et helhetlig og gjenkjennelig uttrykk. Det visuelle uttrykket er godt mottatt og løfter kaféenes identitet i et marked med mye konkurranse.",
         deliver=["Logo for Java St. Hanshaugen", "Logo for Mocca Briskeby", "Design av take-away-kopper", "Profil på tvers av kaféene"],
         images=[("java-cups", "Stablede take-away-kopper med Java- og Mocca-logo"), ("mocca-cup", "Hvit Mocca-kopp på en benk"), ("java-pour", "Kaffe som helles i en Mocca-kopp"), ("mocca-oatly", "Mocca-kopp sammen med Oatly"), ("java-carry", "To Java-kopper i en papirholder")],
         quote="madelene"),
    dict(slug="slice-pizza", name="Slice Pizza", kind="Pizzeria", tags="Logo · Identitet · Emballasje", cover="slice-restaurant",
         title="Slice Pizza: logo og identitet for en pizzeria",
         desc="En leken logo formet som et pizzastykke, og en identitet som balanserer lekenhet og profesjonalitet. Fra pizzaeske til neonskilt.",
         lede="En logo formet som et pizzastykke: enkel, original og lett å kjenne igjen.",
         problem="Slice trengte en identitet som var leken nok til å passe en pizzeria, uten å virke useriøs.",
         solution="Jeg tegnet en logo formet som et pizzastykke, og bygget en identitet rundt den med farger og typografi som tåler alt fra pizzaesker til neonskilt og t-skjorter.",
         deliver=["Logo", "Visuell identitet", "Design av pizzaeske", "Profilering"],
         images=[("slice-box", "Stablede pizzaesker med Slice-logo"), ("slice-neon", "Slice-logo som rødt neonskilt"), ("slice-tee", "T-skjorte med Slice-logo"), ("slice-dark", "Svart pizzaeske med Slice-logo")],
         quote="james"),
    dict(slug="bacalao-bar", name="Bacalao Bar", kind="Restaurant, Lofoten", tags="Nettside · Identitet", cover="bacalao-desk",
         title="Bacalao Bar: nettside og identitet for restaurant i Lofoten",
         desc="Visuell identitet og responsiv nettside for Bacalao Bar i Lofoten, inspirert av kystlandskapet og restaurantens levende atmosfære.",
         lede="En nettside som har samme stemning som restauranten.",
         problem="Bacalao Bar ville ha en digital tilstedeværelse som speilte stemningen i restauranten, og som gjorde det lett å finne meny, åpningstider og booking.",
         solution="Jeg utviklet en helhetlig visuell identitet og en nettside inspirert av Lofotens røffe kystlandskap og restaurantens atmosfære. Stilrent, moderne og med lokal sjel.",
         deliver=["Visuell identitet", "Nettside tilpasset mobil", "Meny og booking på siden"],
         images=[("bacalao-phone", "Bacalao-nettsiden på mobil ved siden av en kaffe"), ("bacalao-m1", "Forsiden til Bacalao Bar på mobil"), ("bacalao-m2", "Arrangementsside på mobil"), ("bacalao-m3", "Bildeside fra Henningsvær på mobil")],
         quote="caroline"),
    dict(slug="private-living", name="Private Living", kind="Overnatting, Lofoten", tags="Nettside · Logo", cover="pl-phone",
         title="Private Living: ny nettside og logo i Lofoten",
         desc="Ny nettside og logo for Private Living, en overnattingsbedrift i Lofoten. Moderne, responsivt design som løfter overnattingstilbudet.",
         lede="En profesjonell og brukervennlig side for overnatting i hjertet av Lofoten.",
         problem="Private Living trengte en nettside og logo som viste fram overnattingstilbudet sitt, og som var enkel å holde oppdatert.",
         solution="Jeg laget ny logo og en moderne, responsiv nettside. Etter lansering har jeg også hjulpet med oppdateringene de har ønsket seg.",
         deliver=["Logo", "Nettside tilpasset mobil", "Oppdateringer etter lansering"],
         images=[("pl-hero", "Forsiden til Private Living med fjellandskap"), ("pl-page", "Undersiden for leiligheter hos Private Living")],
         quote="kirsti"),
    dict(slug="cold-water-kids", name="Cold Water Kids", kind="Mitt eget klesmerke", tags="Identitet · Nettbutikk · Klær", cover="cwk-coast",
         title="Cold Water Kids: identitet, nettbutikk og klær",
         desc="Cold Water Kids er mitt eget klesmerke fra 2019, inspirert av surf, kunst og hav. Logo, nettbutikk, grafikk og klesdesign fra samme hånd.",
         lede="Mitt eget merke, der jeg har brukt nesten alt jeg tilbyr.",
         problem="Cold Water Kids er klesmerket jeg startet i 2019, inspirert av surf, kunst og havet i nord. Merket trengte et uttrykk som var like sterkt på en t-skjorte som på en nettside.",
         solution="Jeg har laget logo, nettbutikk, grafiske elementer og klesdesign. Merket er også der jeg lager film: dokumentarene fra Lofoten og havet hører hjemme her.",
         deliver=["Logo og visuell identitet", "Nettbutikk", "Grafikk og klesdesign", "Film og innhold"],
         images=[("cwk-portrait", "Surfer med Cold Water Kids-t-skjorte i snø"), ("cwk-desk", "Cold Water Kids-nettsiden på en stor skjerm"), ("cwk-tee", "Svart Cold Water Kids-t-skjorte"), ("cwk-wake", "Wakeboarder i Cold Water Kids-t-skjorte")],
         quote=None, link=("https://coldwaterkids.com", "coldwaterkids.com")),
]


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def quote_fig(key, short=False):
    q, who, where = QUOTES[key]
    return f'<figure class="quote"><blockquote>«{q}»</blockquote><figcaption><span class="stars" aria-label="5 av 5">★★★★★</span><b>{who}</b>{where}</figcaption></figure>'


def pkg_card(key, rec=False, badge="Mest valgt"):
    p = PKGS[key]
    b = f'<span class="badge">{badge}</span>' if rec else ""
    pr = ("fra " if p["frm"] else "") + p["price"]
    return f'''<article class="pkg{' rec' if rec else ''}">{b}<h3>{p["name"]}</h3>
<div class="price">{pr} kr <small>eks. mva</small></div><p class="for">{p["for_"]}</p>{checks(p["inc"])}
<div class="acts"><a class="btn" href="{p["url"]}#kontakt">Få tilbud</a><a class="textlink" href="{p["url"]}">Les mer</a></div></article>'''


def packages(c):
    return f'''<div class="pkgs">{pkg_card("logo")}{pkg_card("start", True)}{pkg_card("profil")}{pkg_card("web")}</div>
<div class="addons">
  <div class="addon"><b>Profil + nettside</b><span>Visuell profil og nettside samlet.</span><span class="p">fra 49 990 kr</span></div>
  <div class="addon"><b>Trykksaker</b><span>Visittkort, flyer, meny eller plakat.</span><span class="p">fra 3 990 kr per produkt</span></div>
  <div class="addon"><b>Film</b><span>Kort film til lansering, nettside eller sosiale medier.</span><span class="p">pris etter avtale</span></div>
</div>'''


def steps(dark=False):
    return '''<div class="steps">
  <div class="step"><h3>Gratis prat</h3><p>30 minutter på video eller telefon. Du forteller om bedriften og hva du trenger.</p></div>
  <div class="step"><h3>Fast pris</h3><p>Du får et tilbud med pris, innhold og leveringstid før noe starter.</p></div>
  <div class="step"><h3>Design og tilbakemelding</h3><p>Jeg lager konseptene, du sier hva du mener, og vi justerer til det sitter.</p></div>
  <div class="step"><h3>Levering</h3><p>Du får alle filer ryddig organisert og klare til bruk, også av andre leverandører.</p></div>
</div>'''


def assure():
    return '''<div class="assure">
  <div><b>Fast pris før start</b><span>Du vet hva det koster før jeg begynner. Ingen overraskelser.</span></div>
  <div><b>Revisjon inkludert</b><span>Alle pakker har minst én runde med endringer.</span></div>
  <div><b>Svar innen én arbeidsdag</b><span>Du snakker med meg, ikke en selger.</span></div>
</div>'''


def logos_row():
    return '''<div class="logos" aria-label="Kunder">
  <p class="label"><b>5/5 på Google</b>5 anmeldelser fra kunder</p>
  <img class="big" src="/img/logo-java.png" width="156" height="160" alt="Java St. Hanshaugen" loading="lazy">
  <img class="wide" src="/img/logo-bacalao.png" width="869" height="160" alt="Bacalao Bar" loading="lazy">
  <img class="xwide" src="/img/logo-elektrokraft.png" width="1339" height="160" alt="Elektro Kraft" loading="lazy">
  <img class="wide" src="/img/logo-kjeoya.png" width="823" height="160" alt="Kjeøya Lodge" loading="lazy">
  <img class="wide" src="/img/logo-fluid.png" width="360" height="97" alt="Fluid" loading="lazy">
</div>'''


HERO_SLIDES = [
    ("java-hero", "Take-away-kopp fra Java St. Hanshaugen holdt i strikkevotter", "Java St. Hanshaugen og Mocca Briskeby", "Logo og kopper", "java-mocca"),
    ("slice-restaurant", "Pizzaesker med Slice-logo i en pizzeria", "Slice Pizza", "Logo og emballasje", "slice-pizza"),
    ("roa-cover", "Roots of Alpicella-logoen over vingårdsterrassene i Liguria", "Roots of Alpicella", "Profil, nettside og film", "roots-of-alpicella"),
    ("pl-phone", "Nettsiden til Private Living på en mobil", "Private Living", "Nettside og logo", "private-living"),
    ("cwk-portrait", "Surfer i Cold Water Kids-t-skjorte i snø", "Cold Water Kids", "Identitet og klær", "cold-water-kids"),
]


def hero_rotator(c):
    imgs, caps = [], []
    for i, (img, alt, name, what, slug) in enumerate(HERO_SLIDES):
        tag = c["pic"](img, alt, "(max-width: 860px) 100vw, 48vw", eager=(i == 0))
        tag = tag.replace("<img ", f'<img data-slide="{i}"{" class=\"on\"" if i == 0 else ""} ' if i == 0 else f'<img data-slide="{i}" ', 1)
        imgs.append(tag)
        caps.append(f'<a class="cap{" on" if i == 0 else ""}" data-slide="{i}" href="/arbeid/{slug}"><span>{name}</span><span>{what}</span></a>')
    return f'''<figure class="hero-media rotator" aria-roledescription="bildeserie" aria-label="Utvalgt arbeid">
    <a class="slides" href="/arbeid/{HERO_SLIDES[0][4]}" tabindex="-1" aria-hidden="true">{"".join(imgs)}</a>
    <figcaption>{"".join(caps)}</figcaption></figure>'''


FEATURED = ["roots-of-alpicella", "java-mocca", "elektro-kraft"]


def work_grid(c, cases=None, first_big=True):
    cases = cases or CASES
    out = []
    for i, cs in enumerate(cases):
        rest = len(cases) - 3
        half = first_big and i >= 3 and rest % 3 == 2 and i >= len(cases) - 2
        cls = "item big" if (first_big and i == 0) else ("item half" if half else "item")
        sizes = "(max-width: 860px) 100vw, 66vw" if "big" in cls else "(max-width: 860px) 50vw, 33vw"
        out.append(f'''<a class="{cls}" href="/arbeid/{cs["slug"]}"><div class="img">{c["pic"](cs["cover"], cs["name"] + ": " + cs["lede"], sizes)}</div>
<div class="meta"><h3>{cs["name"]}</h3><span class="tags">{cs["tags"]}</span></div></a>''')
    return '<div class="work">' + "".join(out) + "</div>"


def faq(items):
    html = '<div class="faq">' + "".join(f'<details><summary>{q}</summary><div class="a"><p>{a}</p></div></details>' for q, a in items) + "</div>"
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, ld


def service_ld(c, name, desc, url, price, frm=True):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc,
            "provider": {"@id": c["SITE"] + "/#business"}, "areaServed": {"@type": "City", "name": "Oslo"}, "url": c["SITE"] + url,
            "offers": {"@type": "Offer", "priceCurrency": "NOK", "price": str(price),
                       "priceSpecification": {"@type": "PriceSpecification", "price": str(price), "priceCurrency": "NOK",
                                              "valueAddedTaxIncluded": False, **({"minPrice": str(price)} if frm else {})}}}


# ---------------------------------------------------------------- sider

def home(c):
    body = f'''<div class="wrap hero">
  <div class="hero-copy">
    <span class="eyebrow">Grafisk designer i Oslo · oppdrag i hele Norge</span>
    <h1 class="h-xl">Logo, nettside og film for <em>små bedrifter</em>.</h1>
    <p class="lede">Fra én designer, til fast pris. Jeg har laget identitet for kaféer, restauranter og nyoppstartede bedrifter siden 2018, og du snakker med meg fra første prat til ferdig levering.</p>
    <div class="btns"><a class="btn" href="{c["CAL"]}" target="_blank" rel="noopener">Book en gratis prat <span class="sq" aria-hidden="true"></span></a><a class="btn ghost" href="/finn-riktig-pakke">Finn riktig pakke</a></div>
    <div class="pricebox"><div class="p">14 990 kr<small>eks. mva</small></div><b>Startpakke</b><span>Logo, designhåndbok og salgspresentasjon.</span><a class="textlink" href="/priser">Se alle priser</a></div>
    <div class="hero-quote"><q>Effektiv, proff og engasjert!</q><span>Madelene, Java &amp; Mocca</span></div>
  </div>
  {hero_rotator(c)}
</div>
<div class="wrap">{logos_row()}</div>

<section class="section dark why-sec"><div class="wrap">
  <div class="head"><span class="eyebrow">Hvorfor meg</span><h2 class="h-l">Én person som kan <em>hele</em> jobben.</h2>
    <p class="lede">De fleste designere leverer en logo. Jeg leverer det bedriften trenger for å bli lagt merke til og få de første kundene.</p></div>
  <div class="reasons">
    <article class="why-card"><div class="img">{c["pic"]("roa-merch", "T-skjorter og caps med logoen til Roots of Alpicella, foran vingården i Liguria", "(max-width: 860px) 100vw, 33vw")}<span class="n">01</span></div>
      <h3>Design, nettside og film fra samme hånd</h3><p>Logo, profil, nettside og film fra én person. Du slipper å koordinere tre leverandører, og alt henger sammen fra start.</p></article>
    <article class="why-card"><div class="img">{c["pic"]("bacalao-phone", "Nettsiden til Bacalao Bar på en mobil ved siden av en kaffekopp", "(max-width: 860px) 100vw, 33vw")}<span class="n">02</span></div>
      <h3>Laget for å selge, ikke bare for å se bra ut</h3><p>Startpakken gir deg en ferdig salgspresentasjon, ikke bare en logo. Jeg kjører også annonser for nettbutikker, så jeg vet hva som gir henvendelser.</p></article>
    <article class="why-card"><div class="img">{c["pic"]("java-cups", "Kopper for Java & Mocca", "(max-width: 860px) 100vw, 33vw")}<span class="n">03</span></div>
      <h3>Kjenner kafé og restaurant</h3><p>Java &amp; Mocca, Slice Pizza og Bacalao Bar. Jeg vet at logoen skal fungere på kopper, esker, menyer og skilt, ikke bare på skjerm.</p></article>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="head"><span class="eyebrow">Utvalgt arbeid</span><h2 class="h-l">Noe av det jeg har laget</h2></div>
  {work_grid(c, [cs for slug in FEATURED for cs in CASES if cs["slug"] == slug])}
  <p style="margin-top:28px"><a class="textlink" href="/arbeid">Se alt arbeid ({len(CASES)})</a></p>
</div></section>

<section class="section" id="priser"><div class="wrap">
  <div class="head"><span class="eyebrow">Tjenester og priser</span><h2 class="h-l">Priser fra 8 990 kr. Fast pris før vi starter.</h2>
    <p class="lede">Usikker på hva du trenger? <a class="textlink" href="/finn-riktig-pakke">Svar på fire spørsmål</a>, så får du et forslag med pris.</p></div>
  {mini_cards()}
  <p class="small muted" style="margin-top:16px">Alle priser er eks. mva. Endelig pris avtaler vi etter en kort prat. <a class="textlink" href="/priser">Se alle detaljer og sammenligning</a></p>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="head"><span class="eyebrow">Slik jobber vi</span><h2 class="h-l">Fire steg, ingen overraskelser</h2></div>
  {steps(True)}
</div></section>

<section class="section"><div class="wrap">
  <div class="head"><span class="eyebrow">Hva kundene sier</span><h2 class="h-l">5/5 på Google, 5 anmeldelser</h2></div>
  <div class="quotes">{quote_fig("kirsti")}{quote_fig("caroline")}{quote_fig("johanne")}</div>
</div></section>

<section class="section white"><div class="wrap about">
  {c["pic"]("marius", "Portrett av Marius Moen", "(max-width: 760px) 260px, 320px")}
  <div class="stack">
    <span class="eyebrow">Hvem du jobber med</span>
    <h2 class="h-l">Hei, jeg er Marius.</h2>
    <p class="lede">Jeg har drevet noedesign siden 2018. Jeg lager logoer, profiler og nettsider for små bedrifter, mest i Oslo, men også i Lofoten. Jeg lager også dokumentarfilm, og det samme blikket bruker jeg når en bedrift trenger en kort film.</p>
    <p><a class="textlink" href="/om">Mer om meg</a></p>
  </div>
</div></section>
{c["cta_band"]()}'''
    return dict(path="/", id="forside", title="Grafisk designer i Oslo – logo, nettside og film | noedesign",
                desc="Grafisk designer i Oslo. Logo, visuell profil, nettside og film for små bedrifter, til fast pris. Startpakke 14 990 kr. Book en gratis prat.",
                body=body, ld=[], og="og-default.jpg")


CTA_LABEL = {"logo": "logo", "startpakke": "Startpakke", "profil": "visuell profil", "nettside": "nettside", "grafisk": "trykksaker", "kafe": "logo og profil"}


def service_page(c, path, pid, crumb, title, desc, eyebrow, h1, lede, image, image_alt, price_html, inc_title, inc, who, extra, cases, faqs, service, ld_name, ld_price, ld_from=True):
    f_html, f_ld = faq(faqs)
    crumbs = [("Forside", "/"), (crumb, path)]
    body = f'''<div class="wrap hero">
  <div class="hero-copy">
    {c["crumbs_html"](crumbs)}
    <span class="eyebrow">{eyebrow}</span>
    <h1 class="h-xl">{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="btns"><a class="btn" href="{c["CAL"]}" target="_blank" rel="noopener">Book en gratis prat <span class="sq" aria-hidden="true"></span></a><a class="btn ghost" href="#kontakt">Få et tilbud</a></div>
    {price_html}
  </div>
  <figure class="hero-media">{c["pic"](image, image_alt, "(max-width: 860px) 100vw, 48vw", eager=True)}</figure>
</div>
<section class="section white"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Hva du får</span><h2 class="h-l">{inc_title}</h2><p class="lede">{who}</p></div>
  <div class="stack">{checks(inc)}</div>
</div></section>
<section class="cta-strip"><div class="wrap"><p><b>Passer dette for deg?</b> Få en fast pris innen én arbeidsdag.</p>
  <div class="btns"><a class="btn" href="#kontakt">Få tilbud på {CTA_LABEL.get(pid, crumb)} <span class="sq" aria-hidden="true"></span></a><a class="textlink" href="{c["CAL"]}" target="_blank" rel="noopener">Book gratis prat</a></div></div></section>
{extra}
<section class="section"><div class="wrap">
  <div class="head"><span class="eyebrow">Slik jobber vi</span><h2 class="h-l">Fire steg, ingen overraskelser</h2></div>
  {steps()}
  <div style="margin-top:32px">{assure()}</div>
</div></section>
<section class="section white"><div class="wrap">
  <div class="head"><span class="eyebrow">Arbeid</span><h2 class="h-l">Relevante prosjekter</h2></div>
  {work_grid(c, cases, first_big=False)}
</div></section>
<section class="section"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Spørsmål og svar</span><h2 class="h-l">Det folk lurer på</h2><p class="muted">Finner du ikke svaret? <a class="textlink" href="tel:{c["TEL"]}">Ring meg på {c["TEL_SHOW"]}</a>.</p></div>
  {f_html}
</div></section>
{c["cta_band"](service=service)}'''
    ld = [f_ld, c["breadcrumbs_ld"](crumbs), service_ld(c, ld_name, desc, path, ld_price, ld_from)]
    return dict(path=path, id=pid, title=title, desc=desc, body=body, ld=ld)


def pricebox(price, name, text, frm=True, link=("/priser", "Se alle priser")):
    p = ("fra " if frm else "") + price
    return f'<div class="pricebox"><div class="p">{p} kr<small>eks. mva</small></div><b>{name}</b><span>{text}</span><a class="textlink" href="{link[0]}">{link[1]}</a></div>'


def by_slug(*slugs):
    return [cs for s in slugs for cs in CASES if cs["slug"] == s]


def logo_page(c):
    extra = f'''<section class="section"><div class="wrap">
  <div class="head"><span class="eyebrow">Logo eller Startpakke?</span><h2 class="h-l">For 6 000 kr mer får du det du trenger for å selge</h2>
    <p class="lede">De fleste som starter med bare en logo, trenger snart en designhåndbok og en presentasjon. Derfor velger de fleste Startpakken.</p></div>
  <div class="pkgs" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{pkg_card("logo")}{pkg_card("start", True)}</div>
</div></section>
<section class="section white"><div class="wrap">
  <div class="head"><span class="eyebrow">Tidligere kunder</span><h2 class="h-l">Det de sier om logoene</h2></div>
  <div class="quotes" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">{quote_fig("james")}{quote_fig("madelene_short")}{quote_fig("kirsti")}</div>
</div></section>'''
    return service_page(
        c, "/logo-design", "logo", "Logodesign",
        "Logodesign i Oslo – fra 8 990 kr, fast pris | noedesign",
        "Logodesign i Oslo til fast pris. Logo i to konsepter med varianter og filer fra 8 990 kr, eller Startpakken med designhåndbok og presentasjon.",
        "Logodesign i Oslo", "En logo som fungerer <em>overalt</em> der kundene ser deg.",
        "Jeg tegner logoer for små bedrifter i Oslo: til skilt, kopper, esker, nettside og sosiale medier. Du får to konsepter å velge mellom, og filene du trenger til skjerm og trykk.",
        "slice-box", "Pizzaesker med Slice-logo",
        pricebox("8 990", "Logo", "To konsepter, varianter og filer til skjerm og trykk."),
        "En logo som er ferdig til bruk",
        PKGS["logo"]["inc"],
        "For deg som trenger en logo og fikser resten selv. Trenger du også designhåndbok og en presentasjon å selge med, er Startpakken et bedre kjøp.",
        extra, by_slug("slice-pizza", "java-mocca", "private-living"),
        [("Hva er forskjellen på Logo og Startpakke?", "Logo-pakken gir deg logoen i to konsepter med varianter og filer til skjerm og trykk. Startpakken gir deg i tillegg en designhåndbok og en ferdig salgspresentasjon på 10–15 sider, for 6 000 kr mer."),
         ("Hvilke filer får jeg?", "Du får logoen som SVG og PNG, i mørk og lys variant, klar for skjerm og trykk. Vil du ha andre formater, er det bare å si fra."),
         ("Hvem eier logoen?", "Du eier logoen og alle filene når fakturaen er betalt. Det gjelder også Startpakke og Visuell profil."),
         ("Hva om jeg ikke liker forslagene?", "Du får to konsepter og én runde med endringer. Trenger du flere runder, avtaler vi det før jeg fortsetter, til timepris 1 150 kr."),
         ("Hvor lang tid tar det?", "Vi avtaler leveringstid i den første praten, ut fra hva du trenger og når du trenger det."),
         ("Jobber du bare med bedrifter i Oslo?", "Nei. De fleste kundene mine er i Oslo, men jeg jobber også med bedrifter i Lofoten og resten av Norge. Alt kan gjøres på video.")],
        "Logo", "Logodesign", 8990)


def startpakke(c):
    extra = f'''<section class="section"><div class="wrap">
  <div class="head"><span class="eyebrow">Hva som er i pakken</span><h2 class="h-l">Tre ting, levert samlet</h2></div>
  <div class="grid g3">
    <div class="diff"><span class="n">01</span><h3>Logo og visuell identitet</h3><p>Logo med primær- og sekundærversjon, mørk og lys variant. Fargepalett og typografi valgt for å fungere både på trykk og skjerm.</p><p class="small muted">SVG og PNG · fargepalett · typografi · varianter</p></div>
    <div class="diff"><span class="n">02</span><h3>Designhåndbok</h3><p>Et dokument som viser nøyaktig hvordan merkevaren skal brukes: fargeverdier, fonter, logoregler og eksempler. Slik holder uttrykket seg likt, også når andre lager materiell.</p><p class="small muted">PDF · bruksregler · eksempler</p></div>
    <div class="diff"><span class="n">03</span><h3>Salgspresentasjon</h3><p>En ferdig salgspresentasjon på 10–15 sider, med profesjonelt design og innhold utviklet ut fra informasjonen du deler om virksomheten din. Leveres som en redigerbar PowerPoint- eller Google Slides-presentasjon.</p><p class="small muted">PowerPoint eller Google Slides · 10–15 sider · redigerbar · én revisjonsrunde. Omfattende research, merkevarestrategi og ekstra tekstproduksjon prises separat etter avtale.</p></div>
  </div>
  <div class="gallery" style="margin-top:40px">
    <figure>{c["pic"]("brochure", "Oransje designhåndbok slått opp", "(max-width: 640px) 100vw, 50vw")}</figure>
    <figure>{c["pic"]("ekpitch-mockup", "Salgspresentasjon for Elektro Kraft vist på skjerm og som sider", "(max-width: 640px) 100vw, 50vw")}</figure>
  </div>
</div></section>
<section class="section white"><div class="wrap">
  <div class="head"><span class="eyebrow">Eksempel</span><h2 class="h-l">Slik ser en salgspresentasjon ut</h2>
    <p class="lede">Utdrag fra presentasjonen jeg laget til Elektro Kraft. Samme profil som logoen og håndboken, klar til å brukes i møter og på e-post.</p></div>
  <div class="deckslides">
    <figure>{c["pic"]("ekpitch-omslag", "Forside i Elektro Krafts salgspresentasjon", "(max-width: 640px) 100vw, 50vw")}</figure>
    <figure>{c["pic"]("ekpitch-utfordring", "Utfordringen: tre utfordringer i Elektro Krafts presentasjon", "(max-width: 640px) 100vw, 50vw")}</figure>
    <figure>{c["pic"]("ekpitch-losning", "Løsningen i Elektro Krafts presentasjon", "(max-width: 640px) 100vw, 50vw")}</figure>
    <figure>{c["pic"]("ekpitch-prosess", "Slik fungerer det: prosessen i Elektro Krafts presentasjon", "(max-width: 640px) 100vw, 50vw")}</figure>
  </div>
</div></section>
<section class="section white"><div class="wrap">
  <div class="head"><span class="eyebrow">Tidligere kunder</span><h2 class="h-l">Det de sier om Startpakken</h2></div>
  <div class="quotes" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">{quote_fig("elektro")}{quote_fig("premiumruss")}</div>
</div></section>'''
    return service_page(
        c, "/startpakke", "startpakke", "Startpakke",
        "Startpakken – logo, designhåndbok og pitch | noedesign",
        "Startpakken fra noedesign: logo, designhåndbok og en ferdig salgspresentasjon på 10–15 sider, skrevet ut fra det du forteller meg. Fast pris 14 990 kr eks. mva.",
        "Startpakke", "Alt du trenger for å se <em>profesjonell</em> ut fra dag én.",
        "Logo, designhåndbok og salgspresentasjon, levert som én komplett pakke. For deg som skal i gang og trenger å selge, ikke bare se bra ut.",
        "magazine", "Designhåndbok og trykksaker i ny profil",
        pricebox("14 990", "Startpakke", "Fast pris, én runde revisjon inkludert.", frm=False),
        "En komplett start, ikke bare en logo",
        PKGS["start"]["inc"] + ["Alle filer ryddig organisert og klare til bruk"],
        "For nyoppstartede bedrifter og de som vil fornye seg raskt. Det eneste i pakken du ikke får andre steder, er salgspresentasjonen.",
        extra, by_slug("java-mocca", "slice-pizza", "private-living"),
        [("Hvorfor en salgspresentasjon?", "Fordi en ny bedrift trenger å selge. En ferdig presentasjon i din egen profil gjør det enklere å vise fram tilbudet til kunder, investorer og partnere. Jeg utvikler innholdet ut fra informasjonen du deler om virksomheten din, så du slipper å lage den fra bunnen."),
         ("Hva er forskjellen på Startpakken og Visuell profil?", "Startpakken gir deg logo, designhåndbok og presentasjon raskt. Visuell profil starter med et strategimøte og gir deg flere konsepter, et fullt designsystem og maler for alt fra visittkort til sosiale medier."),
         ("Kan jeg redigere presentasjonen selv?", "Ja. Den leveres som en redigerbar PowerPoint- eller Google Slides-presentasjon, så du kan oppdatere den selv senere. Én revisjonsrunde er inkludert. Omfattende research, merkevarestrategi og ekstra tekstproduksjon prises separat etter avtale."),
         ("Hvor lang tid tar det?", "Vi avtaler leveringstid i den første praten. Har du en frist, si fra, så planlegger vi ut fra den."),
         ("Hva skjer etter levering?", "Du eier filene og kan bruke dem som du vil. Trenger du endringer senere, gjør jeg det til timepris 1 150 kr.")],
        "Startpakke", "Startpakke: logo, designhåndbok og salgspresentasjon", 14990, ld_from=False)


def profil_page(c):
    extra = f'''<section class="section"><div class="wrap">
  <div class="head"><span class="eyebrow">Sammenligning</span><h2 class="h-l">Hva er forskjellen?</h2></div>
  {compare_table()}
</div></section>'''
    return service_page(
        c, "/visuell-profil", "profil", "Visuell profil",
        "Visuell profil og designhåndbok i Oslo | noedesign",
        "Visuell profil for bedrifter i Oslo: strategi, logo i flere konsepter, farger, typografi, designmanual og maler du kan bruke selv. Fra 29 990 kr eks. mva.",
        "Visuell profil i Oslo", "En merkevare som ser <em>lik ut</em> overalt, hver gang.",
        "Visuell profil er mer enn en logo. Det er et system av farger, typografi, bilder og maler som gjør at kundene kjenner deg igjen, uansett hvor de ser deg.",
        "java-cups", "Take-away-kopper i Java og Mocca sin profil",
        pricebox("29 990", "Visuell profil", "Strategi, system og maler."),
        "Et helt system, ikke bare en logo", PKGS["profil"]["inc"],
        "For bedrifter som vil bygge en merkevare som holder over tid, og som skal lage mye materiell selv.",
        extra, by_slug("java-mocca", "bacalao-bar", "cold-water-kids"),
        [("Hvorfor starter du med et strategimøte?", "Fordi en profil må bygge på hvem du er for og hvem du konkurrerer med. Vi bruker 1–2 timer på målgruppe, konkurrenter og hvordan bedriften skal oppleves, før jeg tegner noe."),
         ("Kan du jobbe videre med logoen vi har?", "Ja. Vi kan bygge profilen rundt en logo du har i dag, eller tegne den om med renere linjer og bedre varianter uten at den mister gjenkjennelsen."),
         ("Hvilke maler får jeg?", "Alt som er i Startpakken, inkludert salgspresentasjonen, pluss visittkort, brevmal, e-postsignatur og 3–5 maler for sosiale medier, alle i din nye profil."),
         ("Kan jeg få nettside samtidig?", "Ja. Profil + nettside koster fra 49 990 kr, og da henger alt sammen fra start.")],
        "Visuell profil", "Visuell profil", 29990)


def compare_table():
    rows = [
        ("Logo", "2 konsepter", "Med varianter", "2–3 konsepter"),
        ("Revisjonsrunder", "1", "1", "2"),
        ("Fargepalett og typografi", "Farger", "y", "Fullt system"),
        ("Designhåndbok", "n", "PDF", "Fullstendig designmanual"),
        ("Salgspresentasjon", "n", "10–15 sider", "10–15 sider"),
        ("Strategimøte", "n", "n", "y"),
        ("Grafiske elementer og bildestil", "n", "n", "y"),
        ("Maler for visittkort, brev og sosiale medier", "n", "n", "y"),
    ]
    def cell(v, hl=False):
        h = " hl" if hl else ""
        if v == "y": return f'<td class="y{h}">Inkludert</td>'
        if v == "n": return f'<td class="n{h}">–</td>'
        return f'<td class="y{h}">{v}</td>'
    body = "".join(f"<tr><th scope=\"row\">{r[0]}</th>{cell(r[1])}{cell(r[2], True)}{cell(r[3])}</tr>" for r in rows)
    return f'''<div class="compare-wrap"><table class="compare">
<thead><tr><th scope="col"><span class="sr">Innhold</span></th><th scope="col">Logo<small>fra 8 990 kr</small></th><th scope="col" class="hl">Startpakke<small>14 990 kr</small></th><th scope="col">Visuell profil<small>fra 29 990 kr</small></th></tr></thead>
<tbody>{body}</tbody></table></div>'''


def nettside_page(c):
    extra = f'''<section class="section"><div class="wrap">
  <div class="head"><span class="eyebrow">Bygget for henvendelser</span><h2 class="h-l">En nettside er et salgsverktøy</h2>
    <p class="lede">Jeg kjører Google- og Meta-annonser for nettbutikker, og ser hver uke hva som får folk til å ta kontakt. Det tar jeg med inn i sidene jeg lager.</p></div>
  <div class="grid g3">
    <div class="diff"><span class="n">01</span><h3>Tydelig hva du tilbyr</h3><p>Besøkende skal forstå hva du gjør, for hvem, og hva det koster, i løpet av få sekunder.</p></div>
    <div class="diff"><span class="n">02</span><h3>Lett å ta kontakt</h3><p>Knapp for å ringe eller booke på mobil, kort skjema, og en takkeside som kan måles i Google.</p></div>
    <div class="diff"><span class="n">03</span><h3>Synlig i søk</h3><p>Titler, beskrivelser, strukturerte data og rask lasting, så du kan bli funnet på det kundene søker etter.</p></div>
  </div>
</div></section>'''
    return service_page(
        c, "/nettside", "nettside", "Nettside",
        "Nettside for små bedrifter i Oslo, fra 24 990 kr",
        "Nettside for små bedrifter i Oslo, bygget for å gi henvendelser. Opptil fem sider, tilpasset mobil, SEO og kontaktskjema. Fra 24 990 kr eks. mva.",
        "Nettside i Oslo", "En nettside som gir deg <em>henvendelser</em>, ikke bare besøk.",
        "Jeg lager raske, enkle nettsider for små bedrifter, med tydelig tilbud, pris og en kort vei til å ta kontakt. Ingen maler, og du snakker med den som lager siden.",
        "bacalao-desk", "Bacalao Bar sin nettside på en stor skjerm",
        pricebox("24 990", "Nettside", "Opptil 5 sider, mobil, SEO og skjema."),
        "En side som er klar til å jobbe for deg",
        PKGS["web"]["inc"] + ["Koblet til Google-bedriftsprofilen din", "Klar for måling av henvendelser"],
        "For bedrifter som har logo og profil, og trenger en side som gjør besøkende til kunder. Mangler du profil, er Profil + nettside fra 49 990 kr.",
        extra, by_slug("bacalao-bar", "private-living", "cold-water-kids"),
        [("Kan jeg oppdatere siden selv?", "Det avtaler vi før start. Noen vil endre tekst og bilder selv, andre vil helst at jeg gjør det. Endringer gjør jeg til timepris 1 150 kr."),
         ("Lager du nettbutikk?", "Ja, men nettbutikk tilpasses hver gang, så fra-prisen gjelder ikke helt. Vi tar en kort prat om produkter og betaling først."),
         ("Hva om jeg trenger flere enn fem sider?", "Flere sider prises etter avtale i tillegg."),
         ("Hjelper du med Google-annonser?", "Ja. Jeg setter opp og kjører Google- og Meta-annonser, og kan sende trafikk til siden når den er klar."),
         ("Kan du lage film til nettsiden?", "Ja. Jeg lager også film, for eksempel en kort film om bedriften til forsiden eller sosiale medier. Pris etter avtale.")],
        "Nettside", "Nettside for små bedrifter", 24990)


def grafisk_page(c):
    extra = f'''<section class="section"><div class="wrap">
  <div class="head"><span class="eyebrow">Eksempler</span><h2 class="h-l">Fra visittkort til flasker</h2></div>
  <div class="gallery">
    <figure>{c["pic"]("cards", "Visittkort i mørk og lys utgave", "(max-width: 640px) 100vw, 50vw")}</figure>
    <figure>{c["pic"]("flyer", "Flyer for arrangement", "(max-width: 640px) 100vw, 50vw")}</figure>
    <figure>{c["pic"]("bottle", "Svart flaske med Rise-etikett", "(max-width: 640px) 100vw, 50vw")}</figure>
    <figure>{c["pic"]("cwk-tee", "T-skjorte med trykk", "(max-width: 640px) 100vw, 50vw")}</figure>
  </div>
</div></section>'''
    return service_page(
        c, "/grafisk-design", "grafisk", "Grafisk design og trykk",
        "Grafisk design og trykksaker i Oslo | noedesign",
        "Grafisk design og trykksaker i Oslo: visittkort, flyer, meny, plakat, emballasje og trykk på klær. Fra 3 990 kr per produkt eks. mva. Book en prat.",
        "Grafisk design i Oslo", "Trykksaker som ser ut som <em>deg</em>.",
        "Visittkort, menyer, flyere, plakater, emballasje og trykk på klær, laget i profilen din, så alt henger sammen.",
        "slice-tee", "T-skjorte med Slice-logo",
        pricebox("3 990", "Trykksaker", "Per produkt, klart til trykk."),
        "Ferdige filer, klare til trykkeriet",
        ["Design i din profil", "Ferdige trykkfiler", "Hjelp med valg av papir og trykkeri", "Tilpasset versjon for skjerm og sosiale medier"],
        "For deg som trenger enkelt materiell raskt, eller som vil ha alt i samme stil som logoen og profilen.",
        extra, by_slug("slice-pizza", "java-mocca", "cold-water-kids"),
        [("Hva koster det?", "Fra 3 990 kr per produkt eks. mva. Trenger du flere ting samtidig, gir jeg en samlet pris."),
         ("Ordner du trykkingen?", "Jeg leverer ferdige trykkfiler og hjelper deg med valg av papir og trykkeri. Selve trykkingen betaler du direkte."),
         ("Lager du trykk på klær?", "Ja. Jeg har lang erfaring med trykk på klær, blant annet for mitt eget merke Cold Water Kids.")],
        "Trykksaker", "Grafisk design og trykksaker", 3990)


def kafe_page(c):
    extra = f'''<section class="section"><div class="wrap">
  <div class="head"><span class="eyebrow">Det en kafé eller restaurant trenger</span><h2 class="h-l">Logoen skal fungere der gjestene er</h2>
    <p class="lede">En logo for servering skal tåle mer enn en skjerm. Den skal stå på kopper, esker, menyer, skilt og forklær, og den skal kjennes igjen fra andre siden av gata.</p></div>
  <div class="grid g4">
    <div class="diff"><span class="n">01</span><h3>Logo og profil</h3><p>Som passer stemningen og fungerer i små og store størrelser.</p></div>
    <div class="diff"><span class="n">02</span><h3>Kopper og emballasje</h3><p>Det kundene tar med seg ut døra, er den beste reklamen du har.</p></div>
    <div class="diff"><span class="n">03</span><h3>Meny og skilt</h3><p>Lett å lese, lett å oppdatere, i samme stil som resten.</p></div>
    <div class="diff"><span class="n">04</span><h3>Nettside og film</h3><p>Meny, åpningstider og booking på mobil, og en kort film som viser stedet.</p></div>
  </div>
</div></section>
<section class="section white"><div class="wrap">
  <div class="head"><span class="eyebrow">Hva de sier</span><h2 class="h-l">Fra kaféer og restauranter</h2></div>
  <div class="quotes">{quote_fig("madelene_short")}{quote_fig("james")}{quote_fig("caroline")}</div>
</div></section>'''
    return service_page(
        c, "/kafe-og-restaurant", "kafe", "Kafé og restaurant",
        "Logo og profil for kafé og restaurant i Oslo | noedesign",
        "Logo, profil, kopper, emballasje, meny og nettside for kaféer og restauranter i Oslo. Jeg har laget identitet for Java & Mocca, Slice Pizza og Bacalao Bar.",
        "Kafé og restaurant", "Logo og profil for <em>kafé og restaurant</em> i Oslo.",
        "Jeg har laget logoer, kopper, pizzaesker og nettsider for kaféer og restauranter i Oslo og Lofoten. Du får én designer som forstår hvordan gjestene møter merkevaren din.",
        "slice-restaurant", "Pizzaesker med Slice-logo i en restaurant",
        pricebox("14 990", "Startpakke", "Logo, designhåndbok og presentasjon.", frm=False),
        "Alt på ett sted",
        ["Logo og visuell profil", "Kopper, esker og emballasje", "Meny, skilt og trykksaker", "Nettside med meny, åpningstider og booking", "Kort film til nettside og sosiale medier"],
        "For nye og etablerte kaféer, bakerier, barer og restauranter som vil se like gode ut som maten og stemningen de serverer.",
        extra, by_slug("java-mocca", "slice-pizza", "bacalao-bar"),
        [("Hva bør jeg starte med?", "For de fleste er Startpakken riktig: logo, designhåndbok og en presentasjon. Så kan kopper, meny og nettside komme når du er klar."),
         ("Lager du design til kopper og emballasje?", "Ja. Jeg har laget take-away-kopper for Java og Mocca og pizzaesker for Slice. Jeg leverer trykkfiler tilpasset leverandøren din."),
         ("Kan du lage nettside med meny og booking?", "Ja, som jeg gjorde for Bacalao Bar. Nettside koster fra 24 990 kr eks. mva."),
         ("Lager du film av restauranten?", "Ja. Jeg lager også film, og kan lage en kort film om stedet til nettside og sosiale medier. Pris etter avtale.")],
        "Startpakke", "Logo og profil for kafé og restaurant", 14990, ld_from=False)


SERVICES = [
    ("/logo-design", "Logo", "Logo med varianter og fargepalett.", "ek-logo"),
    ("/startpakke", "Startpakke", "Logo, designhåndbok og salgspresentasjon.", "ekpitch-mockup"),
    ("/visuell-profil", "Visuell profil", "Strategi, flere konsepter og full designmanual.", "roa-handbook"),
    ("/nettside", "Nettside", "Egen nettside som er lett å finne og enkel å bruke.", "bacalao-desk"),
    ("/grafisk-design", "Trykk og klær", "Visittkort, flyers, meny, emballasje og tøy.", "flyer"),
    ("/kafe-og-restaurant", "Kafé og restaurant", "Logo, profil og nettside for serveringssteder.", "slice-restaurant"),
]


def services_grid(c):
    out = "".join(
        f'''<a class="item svc" href="{h}"><div class="img">{c["pic"](img, t, "(max-width: 860px) 50vw, 33vw")}</div>
<div class="meta"><h3>{t}</h3><span class="arrow" aria-hidden="true">→</span></div><p class="svc-d">{d}</p></a>'''
        for h, t, d, img in SERVICES)
    return '<div class="work svcs">' + out + "</div>"


MINI = [
    ("/logo-design", "Logo", "fra 8 990 kr", "Logo med varianter og fargepalett."),
    ("/startpakke", "Startpakke", "14 990 kr", "Logo, designhåndbok og salgspresentasjon.", True),
    ("/visuell-profil", "Visuell profil", "fra 29 990 kr", "Strategi, flere konsepter og full designmanual."),
    ("/nettside", "Nettside", "fra 24 990 kr", "Opptil fem sider som gir henvendelser."),
    ("/grafisk-design", "Trykk og klær", "fra 3 990 kr", "Visittkort, flyers, meny og emballasje."),
    ("/kafe-og-restaurant", "Kafé og restaurant", "14 990 kr", "Logo og profil for serveringssteder."),
]


def mini_cards():
    out = []
    for m in MINI:
        rec = len(m) > 4
        badge = '<span class="mbadge">Mest valgt</span>' if rec else ""
        out.append(f'''<a class="mini{' rec' if rec else ''}" href="{m[0]}">{badge}<div class="mtop"><h3>{m[1]}</h3><span class="arrow" aria-hidden="true">→</span></div>
<div class="mprice">{m[2]}</div><p>{m[3]}</p></a>''')
    return '<div class="minis">' + "".join(out) + "</div>"


def priser(c):
    f_html, f_ld = faq([
        ("Er prisene med eller uten mva?", "Alle priser er eks. mva."),
        ("Hvorfor står det «fra»?", "Fordi omfanget kan variere. Du får alltid en fast pris før jeg begynner, så du vet nøyaktig hva det koster."),
        ("Hva om jeg trenger mer enn pakken?", "Da avtaler vi det før jeg fortsetter. Endringer og småjobber koster 1 150 kr i timen."),
        ("Kan jeg kombinere pakker?", "Ja. Profil + nettside koster fra 49 990 kr. Startpakke og nettside kan også kombineres."),
    ])
    crumbs = [("Forside", "/"), ("Priser", "/priser")]
    body = f'''<div class="wrap case-hero">
  {c["crumbs_html"](crumbs)}
  <span class="eyebrow">Tjenester og priser</span>
  <h1 class="h-xl">Priser på logo, profil og nettside.</h1>
  <p class="lede">Priser fra 8 990 kr, og fast pris avtalt før vi starter. Usikker på hva du trenger? <a class="textlink" href="/finn-riktig-pakke">Svar på fire spørsmål</a>, så får du et forslag.</p>
</div>
<section class="section tight"><div class="wrap">
  <div class="head"><span class="eyebrow">Tjenester</span><h2 class="h-l">Hva trenger du hjelp med?</h2></div>
  {services_grid(c)}
</div></section>
<section class="section" id="priser"><div class="wrap">
  <div class="head"><span class="eyebrow">Priser</span><h2 class="h-l">Velg pakke.</h2></div>{packages(c)}
  <div class="addons"><div class="addon"><b>Timepris</b><span>Endringer og småjobber.</span><span class="p">1 150 kr</span></div></div>
  <p class="small muted" style="margin-top:16px">Alle priser er eks. mva.</p>
</div></section>
<section class="section white"><div class="wrap">
  <div class="head"><span class="eyebrow">Sammenligning</span><h2 class="h-l">Logo, Startpakke eller Visuell profil?</h2></div>
  {compare_table()}
</div></section>
<section class="section"><div class="wrap">{assure()}</div></section>
<section class="section white"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Spørsmål og svar</span><h2 class="h-l">Om priser</h2></div>{f_html}
</div></section>
{c["cta_band"]()}'''
    return dict(path="/priser", id="priser", title="Priser på logo, visuell profil og nettside | noedesign",
                desc="Faste priser på design i Oslo: logo fra 8 990 kr, Startpakke 14 990 kr, visuell profil fra 29 990 kr og nettside fra 24 990 kr. Alle priser eks. mva.",
                body=body, ld=[f_ld, c["breadcrumbs_ld"](crumbs)])


def guide_page(c):
    crumbs = [("Forside", "/"), ("Finn riktig pakke", "/finn-riktig-pakke")]
    body = f'''<div class="wrap case-hero" style="max-width:840px">
  {c["crumbs_html"](crumbs)}
  <span class="eyebrow">Finn riktig pakke</span>
  <h1 class="h-xl">Hva trenger <em>du</em>?</h1>
  <p class="lede">Svar på fire korte spørsmål, så får du et forslag med pris og hva som er inkludert. Ingen forpliktelser.</p>
</div>
<section class="section tight" style="padding-top:0"><div class="wrap">
  <div class="guide">
    <div class="switch" role="group" aria-label="Velg guide">
      <button type="button" data-guide="pakke" aria-pressed="true">Logo og profil</button>
      <button type="button" data-guide="web" aria-pressed="false">Nettside</button>
    </div>
    <div id="guide-app" aria-live="polite"><noscript><p>Guiden krever JavaScript. Se <a class="textlink" href="/priser">alle priser</a> i stedet.</p></noscript></div>
    <form id="guide-form" class="form-card" name="pakkeguide" method="POST" action="/takk" data-netlify="true" netlify-honeypot="bot-field" hidden>
      <input type="hidden" name="form-name" value="pakkeguide">
      <input type="hidden" name="pakke"><input type="hidden" name="svar"><input type="hidden" name="guide">
      <p class="hp"><label>Ikke fyll ut dette feltet <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
      <h2 class="h-m">Få et konkret tilbud på <span data-pkg>pakken</span></h2>
      <p class="small muted">Svarene dine sendes med, så du slipper å forklare alt på nytt. Jeg svarer innen én arbeidsdag.</p>
      <div class="row2">
        <div class="field"><label for="g-navn">Navn</label><input id="g-navn" name="navn" required autocomplete="name"></div>
        <div class="field"><label for="g-epost">E-post</label><input id="g-epost" name="epost" type="email" required autocomplete="email"></div>
      </div>
      <div class="field"><label for="g-tel">Telefon <span class="valgfri">(valgfritt)</span></label><input id="g-tel" name="telefon" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="g-melding">Kort om prosjektet <span class="valgfri">(valgfritt)</span></label><textarea id="g-melding" name="melding" placeholder="Hva gjør bedriften, og når trenger du det?"></textarea></div>
      <div class="btns"><button class="btn" type="submit">Send forespørsel <span class="sq" aria-hidden="true"></span></button></div>
    </form>
  </div>
</div></section>
<section class="section white"><div class="wrap">{assure()}</div></section>'''
    return dict(path="/finn-riktig-pakke", id="guide", title="Finn riktig designpakke på ett minutt | noedesign",
                desc="Svar på fire spørsmål og få et forslag til logo, profil eller nettside med pris og innhold. Fast pris, ingen forpliktelser. Grafisk designer i Oslo.",
                body=body, ld=[c["breadcrumbs_ld"](crumbs)], scripts='<script src="/assets/guide.js?v=1" defer></script>')


def arbeid(c):
    crumbs = [("Forside", "/"), ("Arbeid", "/arbeid")]
    body = f'''<div class="wrap case-hero">
  {c["crumbs_html"](crumbs)}
  <span class="eyebrow">Arbeid</span>
  <h1 class="h-xl">Logoer, profiler og nettsider jeg har laget.</h1>
  <p class="lede">Et utvalg prosjekter for en vingård, kaféer, restauranter, overnatting og mitt eget klesmerke.</p>
</div>
<section class="section tight" style="padding-top:0"><div class="wrap">{work_grid(c)}</div></section>
<section class="section white"><div class="wrap">{logos_row()}</div></section>
{c["cta_band"]("Vil du ha noe lignende?")}'''
    return dict(path="/arbeid", id="arbeid", title="Arbeid: logo, profil og nettsider | noedesign",
                desc="Utvalgt arbeid fra noedesign: profil og nettside for vingården Roots of Alpicella, logo for Java & Mocca, identitet for Slice Pizza og nettsider i Lofoten.",
                body=body, ld=[c["breadcrumbs_ld"](crumbs)])


def case_page(c, cs, nxt):
    crumbs = [("Forside", "/"), ("Arbeid", "/arbeid"), (cs["name"], f"/arbeid/{cs['slug']}")]
    def fig(n, a, *opt):
        full = "full" in opt
        return f'<figure{" class=\"full\"" if full else ""}>{c["pic"](n, a, "(max-width: 640px) 100vw, 100vw" if full else "(max-width: 640px) 100vw, 50vw")}</figure>'
    imgs = "".join(fig(*im) for im in cs["images"])
    hv = cs.get("hero_video")
    if hv:
        poster = f"/img/{cs['cover'] if not hv.get('poster') else hv['poster']}-1280.webp"
        cover = (f'<figure class="case-cover"><video autoplay muted loop playsinline preload="metadata" poster="{poster}" data-autoplay aria-label="{cs["name"]}: showreel">'
                 f'<source src="{hv["mobile"]}" type="video/mp4" media="(max-width: 640px)"><source src="{hv["src"]}" type="video/mp4"></video></figure>')
    else:
        cover = f'<figure class="case-cover">{c["pic"](cs["cover"], cs["name"] + ": " + cs["lede"], "(max-width: 1320px) 100vw, 1280px", eager=True)}</figure>'
    fm = cs.get("film")
    film = (f'<section class="section tight" style="padding-top:0"><div class="wrap"><span class="eyebrow">{fm["eyebrow"]}</span>'
            f'<figure class="case-film"><video controls playsinline preload="none" poster="/img/{fm["poster"]}-1280.webp"><source src="{fm["src"]}" type="video/mp4"></video>'
            f'<figcaption class="small muted">{fm["caption"]}</figcaption></figure></div></section>') if fm else ""
    q = f'<section class="section white"><div class="wrap" style="max-width:860px"><span class="eyebrow">Hva kunden sier</span><div style="margin-top:20px">{quote_fig(cs["quote"])}</div></div></section>' if cs.get("quote") else ""
    link = f'<p><a class="textlink" href="{cs["link"][0]}" target="_blank" rel="noopener">Se {cs["link"][1]}</a></p>' if cs.get("link") else ""
    body = f'''<div class="wrap case-hero">
  {c["crumbs_html"](crumbs)}
  <span class="eyebrow">{cs["kind"]}</span>
  <h1 class="h-xl">{cs["name"]}</h1>
  <p class="lede">{cs["lede"]}</p>
  <div class="facts"><div><span>Kunde</span>{cs["name"]}</div><div><span>Bransje</span>{cs["kind"]}</div><div><span>Leveranse</span>{cs["tags"]}</div></div>
</div>
<div class="wrap">{cover}</div>
<section class="section"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Utfordringen</span><p class="lede">{cs["problem"]}</p></div>
  <div class="stack"><span class="eyebrow">Løsningen</span><div class="prose"><p>{cs["solution"]}</p></div>{checks(cs["deliver"])}{link}</div>
</div></section>
{film}
<section class="section tight" style="padding-top:0"><div class="wrap gallery">{imgs}</div></section>
{q}
<section class="section"><div class="wrap nextcase">
  <a class="textlink" href="/arbeid">Alt arbeid</a>
  <a class="btn ghost" href="/arbeid/{nxt["slug"]}">Neste: {nxt["name"]}</a>
</div></section>
{c["cta_band"]("Vil du ha noe lignende?")}'''
    ld = [c["breadcrumbs_ld"](crumbs), {"@context": "https://schema.org", "@type": "CreativeWork", "name": cs["title"],
          "description": cs["desc"], "creator": {"@id": c["SITE"] + "/#business"}, "image": c["SITE"] + f"/img/{cs['cover']}-1280.webp",
          "url": c["SITE"] + f"/arbeid/{cs['slug']}"}]
    return dict(path=f"/arbeid/{cs['slug']}", id="case", title=cs["title"] + (" | noedesign" if len(cs["title"]) < 50 else ""),
                desc=cs["desc"], body=body, ld=ld)


def om(c):
    crumbs = [("Forside", "/"), ("Om meg", "/om")]
    body = f'''<div class="wrap case-hero">
  {c["crumbs_html"](crumbs)}
  <span class="eyebrow">Om meg</span>
  <h1 class="h-xl">Hei, jeg er Marius. Du snakker med <em>meg</em> hele veien.</h1>
</div>
<section class="section tight" style="padding-top:0"><div class="wrap about">
  {c["pic"]("marius", "Portrett av Marius Moen", "(max-width: 760px) 260px, 320px", eager=True)}
  <div class="prose">
    <p class="lede">Jeg har drevet noedesign siden 2018. Jeg lager logoer, visuelle profiler og nettsider for små bedrifter og nyoppstartede, mest i Oslo, men også i Lofoten, der jeg er mye.</p>
    <p>Du får ikke en selger først og en designer etterpå. Du snakker med meg fra første prat til ferdig levering, og det er jeg som tegner, skriver og bygger.</p>
    <p>Jeg lager også film. Dokumentarene mine fra Lofoten og havet lager jeg gjennom <a class="textlink" href="https://stoyta.no" target="_blank" rel="noopener">Støyta</a>, og det samme blikket bruker jeg når en kafé, et hotell eller en butikk trenger en kort film til nettsiden.</p>
    <p>I tillegg setter jeg opp og kjører Google- og Meta-annonser, blant annet for Fluid i Oslo. Derfor tenker jeg alltid på hvordan det jeg lager skal gi deg kunder, ikke bare hvordan det ser ut.</p>
    <div class="btns" style="margin-top:8px"><a class="btn" href="{c["CAL"]}" target="_blank" rel="noopener">Book en gratis prat <span class="sq" aria-hidden="true"></span></a><a class="btn ghost" href="{c["LINKEDIN"]}" target="_blank" rel="noopener">LinkedIn</a></div>
  </div>
</div></section>
<div class="wrap"><figure class="wide-photo" style="margin:0 0 72px">{c["pic"]("sailing", "Marius på en seilbåt i kveldssol", "100vw")}<figcaption class="small muted" style="margin-top:10px">Når jeg ikke designer, er jeg ofte på havet, med kamera.</figcaption></figure></div>
<section class="section white"><div class="wrap">
  <div class="head"><span class="eyebrow">Hva jeg gjør</span><h2 class="h-l">Fire ting, fra én person</h2></div>
  <div class="grid g4">
    <div class="diff"><span class="n">01</span><h3>Logo og profil</h3><p><a class="textlink" href="/logo-design">Logo</a>, <a class="textlink" href="/startpakke">Startpakke</a> og <a class="textlink" href="/visuell-profil">visuell profil</a>.</p></div>
    <div class="diff"><span class="n">02</span><h3>Nettside</h3><p><a class="textlink" href="/nettside">Nettsider</a> som gir henvendelser.</p></div>
    <div class="diff"><span class="n">03</span><h3>Trykk og klær</h3><p><a class="textlink" href="/grafisk-design">Trykksaker</a>, emballasje og trykk på klær.</p></div>
    <div class="diff"><span class="n">04</span><h3>Film og annonser</h3><p>Korte filmer og annonser som sender folk til siden.</p></div>
  </div>
</div></section>
{c["cta_band"]()}'''
    return dict(path="/om", id="om", title="Om Marius Moen, grafisk designer i Oslo | noedesign",
                desc="Marius Moen har drevet noedesign siden 2018. Logo, profil, nettside og film for små bedrifter i Oslo og Lofoten, fra én person hele veien.",
                body=body, ld=[c["breadcrumbs_ld"](crumbs)])


def kontakt(c):
    crumbs = [("Forside", "/"), ("Kontakt", "/kontakt")]
    body = f'''<div class="wrap case-hero">
  {c["crumbs_html"](crumbs)}
  <span class="eyebrow">Kontakt</span>
  <h1 class="h-xl">La oss ta en prat.</h1>
  <p class="lede">Book 30 minutter på video eller telefon, ring, eller send en kort melding. Du får svar innen én arbeidsdag, og en fast pris før noe starter.</p>
</div>
<section class="section tight" style="padding-top:0"><div class="wrap cta-band">
  <div class="stack-l">
    <div class="contact-list">
      <a href="{c["CAL"]}" target="_blank" rel="noopener" id="book"><span>Book en gratis prat</span><b>30 minutter, video eller telefon</b></a>
      <a href="tel:{c["TEL"]}"><span>Ring</span><b>{c["TEL_SHOW"]}</b></a>
      <a href="mailto:{c["MAIL"]}"><span>E-post</span><b>{c["MAIL"]}</b></a>
      <a href="{c["LINKEDIN"]}" target="_blank" rel="noopener"><span>LinkedIn</span><b>noedesign</b></a>
    </div>
    <p class="muted">noedesign · Oslo<br>Jeg jobber også med bedrifter i Lofoten og resten av Norge.</p>
  </div>
  {c["contact_form"]("Send en melding")}
</div></section>
<section class="section white"><div class="wrap">{assure()}</div></section>'''
    return dict(path="/kontakt", id="kontakt", title="Kontakt noedesign – book en gratis prat i Oslo",
                desc="Ta kontakt med noedesign, grafisk designer i Oslo. Book en gratis prat på 30 minutter, ring 46 93 87 50 eller send en melding. Svar innen én arbeidsdag.",
                body=body, ld=[c["breadcrumbs_ld"](crumbs)])


def takk(c):
    body = f'''<div class="wrap case-hero" style="max-width:840px;padding-block:96px">
  <span class="eyebrow">Takk</span>
  <h1 class="h-xl">Takk! Jeg har fått meldingen din.</h1>
  <p class="lede">Jeg svarer innen én arbeidsdag, med et forslag og en fast pris. Vil du snakke med en gang, kan du booke en prat eller ringe meg.</p>
  <div class="btns"><a class="btn" href="{c["CAL"]}" target="_blank" rel="noopener">Book en gratis prat</a><a class="btn ghost" href="tel:{c["TEL"]}">Ring {c["TEL_SHOW"]}</a></div>
  <p><a class="textlink" href="/arbeid">Se arbeid mens du venter</a></p>
</div>'''
    return dict(path="/takk", id="takk", title="Takk for meldingen | noedesign",
                desc="Takk for at du tok kontakt med noedesign. Jeg svarer innen én arbeidsdag.", body=body, noindex=True)


def personvern(c):
    crumbs = [("Forside", "/"), ("Personvern", "/personvern")]
    body = f'''<div class="wrap case-hero" style="max-width:840px">
  {c["crumbs_html"](crumbs)}
  <h1 class="h-l">Personvern</h1>
  <div class="prose">
    <p>noedesign drives av Moen Design (enkeltpersonforetak, org.nr. 921 420 544) i Oslo. Her står det hvilke opplysninger jeg samler inn og hva de brukes til.</p>
    <h2 class="h-m">Skjemaer</h2>
    <p>Når du sender en melding eller bruker «Finn riktig pakke», lagrer jeg det du skriver inn: navn, e-post, eventuelt telefon og bedrift, og svarene dine. Opplysningene brukes bare til å svare deg og gi deg et tilbud. Skjemaene håndteres av Netlify, som drifter nettsiden.</p>
    <h2 class="h-m">Booking</h2>
    <p>Booking av samtale skjer hos Calendly. Da gjelder Calendly sine vilkår for opplysningene du gir der.</p>
    <h2 class="h-m">Informasjonskapsler og måling</h2>
    <p>Nettsiden bruker bare måling (Google Analytics og Google Ads) hvis du har godtatt det. Du kan når som helst trekke samtykket ved å slette informasjonskapslene for nettstedet i nettleseren din.</p>
    <h2 class="h-m">Dine rettigheter</h2>
    <p>Du kan be om innsyn, retting eller sletting av opplysningene dine ved å sende en e-post til <a class="textlink" href="mailto:{c["MAIL"]}">{c["MAIL"]}</a>.</p>
  </div>
</div>'''
    return dict(path="/personvern", id="personvern", title="Personvern og informasjonskapsler | noedesign",
                desc="Slik behandler noedesign opplysninger fra skjemaer, booking og måling på nettsiden, og hvordan du ber om innsyn, retting eller sletting.",
                body=body, ld=[c["breadcrumbs_ld"](crumbs)])


def notfound(c):
    body = '''<div class="wrap case-hero" style="max-width:840px;padding-block:96px">
  <span class="eyebrow">404</span>
  <h1 class="h-xl">Denne siden finnes ikke.</h1>
  <p class="lede">Kanskje den har flyttet. Prøv en av disse:</p>
  <div class="btns"><a class="btn" href="/">Til forsiden</a><a class="btn ghost" href="/priser">Priser</a><a class="btn ghost" href="/arbeid">Arbeid</a></div>
</div>'''
    return dict(path="/404.html", id="404", title="Fant ikke siden | noedesign", desc="Siden finnes ikke.", body=body, noindex=True)


def build_all(c):
    pages = [home(c), logo_page(c), startpakke(c), profil_page(c), nettside_page(c), grafisk_page(c), kafe_page(c),
             priser(c), guide_page(c), arbeid(c), om(c), kontakt(c), takk(c), personvern(c), notfound(c)]
    for i, cs in enumerate(CASES):
        pages.append(case_page(c, cs, CASES[(i + 1) % len(CASES)]))
    from guides import guide_pages
    pages += guide_pages(c)
    return pages
