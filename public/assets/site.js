/* noedesign.no – felles skript: header, samtykke og sporing. */
(function () {
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  }

  /* Sporing: fyll inn ID-er i /assets/config.js. Uten ID-er lastes ingenting og banneret vises ikke. */
  var cfg = window.NOEDESIGN_CONFIG || {};
  var hasTracking = Boolean(cfg.GA4_ID || cfg.ADS_ID);
  var KEY = "nd-consent";
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;

  /* Hendelser går via track(). Før samtykkevalget er lastet, venter de i kø, slik at
     consent-innstillingen alltid kommer først. Ingen personopplysninger sendes. */
  var ready = false, queue = [];
  function track(name, params) {
    if (!hasTracking) return;
    if (ready) gtag("event", name, params || {});
    else queue.push([name, params || {}]);
  }
  window.ndTrack = track;

  /* En innsending lagres i sessionStorage når skjemaet sendes, og brukes én gang på /takk.
     Oppdatering av takkesiden eller direkte besøk gir derfor ingen ny konvertering. */
  var LEAD = "nd-lead";
  function takeLead() {
    try {
      var raw = sessionStorage.getItem(LEAD);
      if (!raw) return null;
      sessionStorage.removeItem(LEAD);
      var d = JSON.parse(raw);
      return d && d.t && Date.now() - d.t < 30 * 60 * 1000 ? d : null;
    } catch (e) { return null; }
  }

  function loadTags(granted) {
    if (!hasTracking) return;
    gtag("consent", "default", {
      ad_storage: granted ? "granted" : "denied",
      ad_user_data: granted ? "granted" : "denied",
      ad_personalization: granted ? "granted" : "denied",
      analytics_storage: granted ? "granted" : "denied"
    });
    var id = cfg.GA4_ID || cfg.ADS_ID;
    var s = document.createElement("script");
    s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
    document.head.appendChild(s);
    gtag("js", new Date());
    if (cfg.GA4_ID) gtag("config", cfg.GA4_ID);
    if (cfg.ADS_ID) gtag("config", cfg.ADS_ID);
    ready = true;
    queue.forEach(function (q) { gtag("event", q[0], q[1]); });
    queue = [];
    // Konvertering på takkesiden: bare når det finnes en innsending fra denne økten
    if (document.body.dataset.page === "takk") {
      var lead = takeLead();
      if (lead) {
        if (cfg.ADS_ID && cfg.ADS_LEAD_LABEL) gtag("event", "conversion", { send_to: cfg.ADS_ID + "/" + cfg.ADS_LEAD_LABEL });
        if (cfg.GA4_ID) {
          var p = { skjema: lead.skjema, side: lead.side };
          if (lead.pakke) p.pakke = lead.pakke;
          if (lead.tjeneste) p.tjeneste = lead.tjeneste;
          gtag("event", "generate_lead", p);
        }
      }
    }
  }

  /* Husk hvilket skjema som ble sendt (bare skjemanavn, side og valgt pakke eller tjeneste).
     submit utløses først når nettleserens validering er bestått. */
  document.addEventListener("submit", function (e) {
    var f = e.target, name = f && f.getAttribute && f.getAttribute("name");
    if (!hasTracking || (name !== "kontakt" && name !== "pakkeguide")) return;
    var d = { skjema: name, side: location.pathname, t: Date.now() };
    var pk = f.querySelector("[name=pakke]"), tj = f.querySelector("[name=tjeneste]");
    if (name === "pakkeguide" && pk && pk.value) d.pakke = pk.value;
    if (name === "kontakt" && tj && tj.value) d.tjeneste = tj.value;
    try { sessionStorage.setItem(LEAD, JSON.stringify(d)); } catch (err) {}
  }, true);

  function stored() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function store(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  if (hasTracking) {
    var choice = stored();
    if (choice) { loadTags(choice === "yes"); }
    else {
      var box = document.createElement("div");
      box.className = "consent"; box.setAttribute("role", "dialog"); box.setAttribute("aria-label", "Informasjonskapsler");
      box.innerHTML = '<p>Jeg bruker informasjonskapsler for å se hvilke sider som fungerer og måle annonser. Du velger selv. <a class="textlink" href="/personvern">Les mer</a></p>' +
        '<div class="btns"><button class="btn" type="button" data-c="yes">Godta</button><button class="btn ghost" type="button" data-c="no">Bare nødvendige</button></div>';
      document.body.appendChild(box);
      box.addEventListener("click", function (e) {
        var v = e.target.getAttribute && e.target.getAttribute("data-c");
        if (!v) return;
        store(v); box.remove(); loadTags(v === "yes");
      });
    }
  }

  /* Bildeserie i toppen av forsiden: bytter hvert 5. sekund, pauser ved hover/fokus og når fanen er skjult */
  var rot = document.querySelector(".rotator");
  if (rot) {
    var imgs = rot.querySelectorAll(".slides img"), caps = rot.querySelectorAll(".cap"), link = rot.querySelector(".slides");
    var i = 0, held = false, reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var show = function (n) {
      imgs[i].classList.remove("on"); caps[i].classList.remove("on");
      i = n; imgs[i].classList.add("on"); caps[i].classList.add("on");
      link.setAttribute("href", caps[i].getAttribute("href"));
    };
    if (imgs.length > 1 && !reduce) {
      rot.addEventListener("mouseenter", function () { held = true; });
      rot.addEventListener("mouseleave", function () { held = false; });
      rot.addEventListener("focusin", function () { held = true; });
      rot.addEventListener("focusout", function () { held = false; });
      setInterval(function () { if (!held && !document.hidden) show((i + 1) % imgs.length); }, 5000);
    }
  }

  /* Bevegelige case-videoer stoppes for dem som har bedt om mindre bevegelse */
  if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.querySelectorAll("video[data-autoplay]").forEach(function (v) { v.removeAttribute("autoplay"); v.pause(); });
  }

  /* Klikk på telefon og e-post som sekundære konverteringer */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href^='tel:'], a[href^='mailto:'], a[href*='calendly.com']");
    if (!a || !hasTracking) return;
    var type = a.href.indexOf("tel:") === 0 ? "ring" : a.href.indexOf("mailto:") === 0 ? "epost" : "booking";
    track("kontakt_klikk", { metode: type, side: location.pathname });
  });
})();
