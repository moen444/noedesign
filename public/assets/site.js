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
    // Konvertering på takkesiden
    if (document.body.dataset.page === "takk" && cfg.ADS_ID && cfg.ADS_LEAD_LABEL) {
      gtag("event", "conversion", { send_to: cfg.ADS_ID + "/" + cfg.ADS_LEAD_LABEL });
    }
    if (document.body.dataset.page === "takk" && cfg.GA4_ID) gtag("event", "generate_lead");
  }

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
    gtag("event", "kontakt_klikk", { metode: type });
  });
})();
