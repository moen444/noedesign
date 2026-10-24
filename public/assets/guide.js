/* Finn riktig pakke – fire spørsmål gir anbefalt pakke med pris. */
(function () {
  var CAL = "https://calendly.com/noedesign-info/30min";
  function nok(n) { return n.toLocaleString("nb-NO").replace(/ /g, " "); }
  var PKG = {
    logo: { name: "Logo", price: 8990, from: true, url: "/logo-design", for: "Deg som bare trenger en logo.",
      inc: ["Logo i 2 konsepter", "Én runde revisjon", "Varianter: liggende, stående og symbol", "Farger", "Filer som SVG og PNG, i mørk og lys variant, for skjerm og trykk"] },
    start: { name: "Startpakke", price: 14990, from: false, url: "/startpakke", for: "Deg som skal komme raskt i gang og selge.",
      inc: ["Logo med varianter og fargepalett", "Designhåndbok (PDF)", "Salgspresentasjon, 10–15 sider", "Én runde revisjon"] },
    profil: { name: "Visuell profil", price: 29990, from: true, url: "/visuell-profil", for: "Deg som vil bygge en merkevare som holder over tid.",
      inc: ["Oppstartsmøte og strategi", "Logo i 2–3 konsepter, to runder revisjon", "Farger, typografi og grafiske elementer", "Bildestil og fullstendig designmanual", "Maler: visittkort, brev, presentasjon, e-postsignatur og sosiale medier"] },
    web: { name: "Nettside", price: 24990, from: true, url: "/nettside", for: "Deg som har profilen på plass og trenger en side som gir henvendelser.",
      inc: ["Opptil 5 sider", "Tilpasset mobil", "SEO-grunnoppsett", "Kontaktskjema"] },
    profilweb: { name: "Profil + nettside", price: 49990, from: true, url: "/priser", for: "Deg som vil ha alt på plass, samlet.",
      inc: ["Alt i Visuell profil", "Nettside med opptil 5 sider", "Tilpasset mobil og SEO-grunnoppsett", "Kontaktskjema"] },
    startweb: { name: "Startpakke + nettside", price: 39980, from: true, url: "/priser", for: "Deg som vil i gang med logo og nettside uten full profil.",
      inc: ["Alt i Startpakken", "Nettside med opptil 5 sider", "Tilpasset mobil og SEO-grunnoppsett", "Kontaktskjema"] }
  };
  var LADDER = ["logo", "start", "profil", "profilweb"];
  var GUIDES = {
    pakke: [
      { id: "fase", q: "Hvor er bedriften din nå?", opts: [["ny", "Vi starter opp", "Ny bedrift, eller rett før lansering"], ["fornye", "Vi vil fornye oss", "Har drevet en stund, men uttrykket henger etter"], ["etablert", "Vi er etablert", "Vil bygge en sterkere merkevare"]] },
      { id: "behov", q: "Hva trenger du?", opts: [["logo", "Bare en logo", "Resten fikser vi selv"], ["selge", "Logo og materiell for å selge", "Designhåndbok og presentasjon"], ["profil", "Hele profilen", "Strategi, system og maler vi kan bruke"], ["web", "Profil og nettside", "Alt på plass, samlet"]] },
      { id: "tid", q: "Når trenger du det?", opts: [["snart", "Så fort som mulig", "Innen et par uker"], ["mnd", "Innen 1–2 måneder", ""], ["rolig", "Ingen hast", "Vi vil gjøre det riktig"]] },
      { id: "budsjett", q: "Omtrent hvilket budsjett ser du for deg?", opts: [["10", "Under 10 000 kr", ""], ["20", "10 000–20 000 kr", ""], ["40", "20 000–40 000 kr", ""], ["40+", "Over 40 000 kr", ""]] }
    ],
    web: [
      { id: "maal", q: "Hva skal nettsiden gjøre for deg?", opts: [["vise", "Vise hvem vi er", "En ryddig side som gir tillit"], ["leads", "Gi oss henvendelser", "Folk skal ta kontakt eller booke"], ["selge", "Selge produkter", "Nettbutikk"]] },
      { id: "profil", q: "Har du logo og visuell profil fra før?", opts: [["ja", "Ja, den er på plass", ""], ["delvis", "Delvis", "Logo, men ikke stort mer"], ["nei", "Nei", "Vi trenger det også"]] },
      { id: "selv", q: "Vil du oppdatere siden selv?", opts: [["ja", "Ja, jeg vil endre tekst og bilder selv", ""], ["nei", "Nei, jeg vil helst at du gjør det", "Endringer etter timepris, 1 150 kr"]] },
      { id: "sider", q: "Omtrent hvor mange sider trenger du?", opts: [["1-3", "1–3 sider", "For eksempel forside, tjenester og kontakt"], ["4-5", "4–5 sider", ""], ["6+", "6 eller flere", ""]] }
    ]
  };

  var root = document.getElementById("guide-app");
  if (!root) return;
  var form = document.getElementById("guide-form");
  var guide = "pakke", step = 0, answers = {}, shown = null;

  function el(tag, attrs) {
    var n = document.createElement(tag);
    attrs = attrs || {};
    Object.keys(attrs).forEach(function (k) {
      var v = attrs[k];
      if (k === "class") n.className = v;
      else if (k === "text") n.textContent = v;
      else if (k.indexOf("on") === 0) n.addEventListener(k.slice(2), v);
      else n.setAttribute(k, v);
    });
    for (var i = 2; i < arguments.length; i++) if (arguments[i] != null) n.append(arguments[i]);
    return n;
  }
  function label(qid, val) {
    var q = GUIDES[guide].filter(function (x) { return x.id === qid; })[0];
    var o = q && q.opts.filter(function (x) { return x[0] === val; })[0];
    return o ? o[1] : "";
  }

  function recommend() {
    var a = answers, key, why = "", notes = [], down = null, up = null;
    if (guide === "pakke") {
      key = { logo: "logo", selge: "start", profil: "profil", web: "profilweb" }[a.behov];
      why = {
        logo: "Du trenger bare en logo, og da er Logo-pakken riktig.",
        selge: "Du trenger mer enn en logo for å komme i gang og selge. Startpakken gir deg designhåndbok og salgspresentasjon i tillegg.",
        profil: "Du vil ha et helt system som brukes overalt, ikke bare en logo. Det er det Visuell profil er laget for.",
        web: "Du vil ha både profil og nettside. Samlet blir det rimeligere og mer helhetlig."
      }[a.behov];
      if (a.behov === "logo" && a.fase === "etablert") notes.push("Siden dere er etablert, kan det lønne seg å se på Visuell profil. Da får logoen et system rundt seg.");
      var cap = { "10": 10000, "20": 20000, "40": 40000, "40+": Infinity }[a.budsjett];
      if (a.behov === "web" && PKG.profilweb.price > cap) {
        if (cap >= PKG.startweb.price) { key = "startweb"; down = "start"; up = "profilweb"; notes.push("Budsjettet ditt er litt under Profil + nettside. Startpakke + nettside gir deg logo, grunnlag og en side som gir henvendelser."); }
        else { key = "start"; down = "logo"; up = "startweb"; notes.push("Med dette budsjettet anbefaler jeg å starte med Startpakken, og ta nettsiden når dere er klare."); }
      } else if (PKG[key].price > cap) {
        var i = LADDER.indexOf(key);
        while (i > 0 && PKG[LADDER[i]].price > cap) i--;
        if (LADDER[i] !== key) { notes.push("Budsjettet ditt er under denne pakken. Vi kan starte med " + PKG[LADDER[i]].name + " og bygge videre senere."); key = LADDER[i]; }
      }
      if (a.tid === "snart") notes.push(key === "logo" || key === "start" ? "Denne pakken kan leveres raskt. Si fra om fristen når vi snakker." : "Med kort frist planlegger vi leveransen i faser, så du får det viktigste først.");
      if (!down && !up) { var j = LADDER.indexOf(key); down = j > 0 ? LADDER[j - 1] : null; up = j < LADDER.length - 1 ? LADDER[j + 1] : null; }
    } else {
      if (a.profil === "nei") { key = "profilweb"; why = "Du mangler profil, og da bør den komme først. Samlet blir nettsiden bedre og billigere."; down = "startweb"; }
      else if (a.profil === "delvis") { key = "startweb"; why = "Du har logo, men lite mer. Startpakken gir deg grunnlaget nettsiden trenger."; down = "web"; up = "profilweb"; }
      else { key = "web"; why = "Profilen er på plass, så vi kan gå rett på en nettside som gir henvendelser."; up = "profilweb"; }
      if (a.maal === "selge") notes.push("Nettbutikk tilpasses hver gang, så fra-prisen gjelder ikke helt. Vi tar en kort prat om produkter og betaling.");
      if (a.maal === "leads") notes.push("Siden bygges for henvendelser: tydelige knapper, kort skjema og booking.");
      if (a.sider === "6+") notes.push("Flere enn 5 sider prises etter avtale i tillegg.");
      if (a.selv === "nei") notes.push("Endringer gjør jeg etter timepris, 1 150 kr.");
    }
    return { key: key, why: why, notes: notes, down: down, up: up };
  }

  function summary(key) {
    var p = PKG[key];
    var lines = GUIDES[guide].map(function (q) { return q.q + " " + label(q.id, answers[q.id]); });
    return lines.join("\n") + "\nForslag: " + p.name + " (" + (p.from ? "fra " : "") + nok(p.price) + " kr eks. mva)";
  }

  function fillForm(key) {
    if (!form) return;
    form.hidden = false;
    form.querySelector("[name=pakke]").value = PKG[key].name;
    form.querySelector("[name=svar]").value = summary(key);
    form.querySelector("[name=guide]").value = guide === "pakke" ? "Logo og profil" : "Nettside";
    var t = form.querySelector("[data-pkg]");
    if (t) t.textContent = PKG[key].name;
  }

  function renderQuestion() {
    if (form) form.hidden = true;
    var qs = GUIDES[guide], q = qs[step];
    var prog = el("div", { class: "progress", "aria-hidden": "true" });
    qs.forEach(function (_, i) { prog.append(el("span", { class: i <= step ? "on" : "" })); });
    var opts = el("div", { class: "opts", role: "group", "aria-label": q.q });
    q.opts.forEach(function (o) {
      opts.append(el("button", { type: "button", class: "opt", "aria-pressed": String(answers[q.id] === o[0]),
        onclick: function () { answers[q.id] = o[0]; step++; render(true); } },
        el("span", { text: o[1] }), o[2] ? el("small", { text: o[2] }) : null));
    });
    var back = el("button", { type: "button", class: "btn ghost", text: "Tilbake", onclick: function () { step--; render(true); } });
    if (step === 0) back.disabled = true;
    root.replaceChildren(el("div", { class: "gcard" }, prog,
      el("div", { class: "gmeta" }, el("span", { text: "Spørsmål " + (step + 1) + " av " + qs.length }), el("span", { text: guide === "pakke" ? "Logo og profil" : "Nettside" })),
      el("h2", { class: "gq", text: q.q, tabindex: "-1" }), opts,
      el("div", { class: "gnav" }, back, el("span", { class: "small muted", text: "Velg ett svar" }))));
  }

  function altBtn(lbl, key) {
    if (!key) return null;
    var p = PKG[key];
    return el("button", { type: "button", class: "alt", onclick: function () { shown = key; render(true); } },
      el("span", { class: "lbl", text: lbl }), el("b", { text: p.name }), el("span", { text: (p.from ? "fra " : "") + nok(p.price) + " kr" }));
  }

  function renderResult() {
    var rec = recommend(), key = shown || rec.key, p = PKG[key], isRec = key === rec.key;
    var inc = el("ul", { class: "checks" });
    p.inc.forEach(function (t) { inc.append(el("li", { text: t })); });
    var card = el("div", { class: "gcard" },
      el("span", { class: "gtag", text: isRec ? "Anbefalt for deg" : "Alternativ" }),
      el("h2", { class: "h-l", text: p.name, tabindex: "-1" }),
      el("p", { class: "muted", text: p.for }),
      el("div", { class: "gprice" }, el("b", { text: (p.from ? "fra " : "") + nok(p.price) + " kr" }), el("span", { text: "eks. mva" })),
      isRec && rec.why ? el("div", { class: "why" }, el("strong", { text: "Hvorfor denne?" }), el("span", { text: rec.why })) : null,
      inc);
    if (isRec) rec.notes.forEach(function (n) { card.append(el("p", { class: "small muted", text: n })); });
    card.append(el("p", { class: "small muted", text: "Endelig pris avtaler vi etter en kort prat, før jeg starter." }));
    card.append(el("div", { class: "btns" },
      el("a", { class: "btn", href: CAL, target: "_blank", rel: "noopener", text: "Book en gratis prat" }),
      el("a", { class: "btn ghost", href: "#guide-form", text: "Få et konkret tilbud" }),
      el("a", { class: "textlink", href: p.url, text: "Les mer om " + p.name })));
    if (isRec) {
      var alts = el("div", { class: "alts" }, altBtn("Rimeligere", rec.down), altBtn("Mer komplett", rec.up));
      if (alts.children.length) card.append(alts);
    } else {
      card.append(el("button", { type: "button", class: "btn ghost", text: "Tilbake til anbefalingen", onclick: function () { shown = null; render(true); } }));
    }
    card.append(el("div", { class: "gnav" },
      el("button", { type: "button", class: "btn ghost", text: "Endre svar", onclick: function () { step = GUIDES[guide].length - 1; shown = null; render(true); } }),
      el("button", { type: "button", class: "btn ghost", text: "Start på nytt", onclick: function () { answers = {}; step = 0; shown = null; render(true); } })));
    root.replaceChildren(card);
    fillForm(key);
  }

  function render(focus) {
    if (step >= GUIDES[guide].length) renderResult(); else renderQuestion();
    if (focus) { var h = root.querySelector("[tabindex='-1']"); if (h) h.focus({ preventScroll: false }); }
  }
  function setGuide(g) {
    guide = g; step = 0; answers = {}; shown = null;
    document.querySelectorAll("[data-guide]").forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.guide === g)); });
    render(false);
  }
  document.querySelectorAll("[data-guide]").forEach(function (b) { b.addEventListener("click", function () { setGuide(b.dataset.guide); }); });
  if (location.hash === "#nettside") setGuide("web"); else render(false);
})();
