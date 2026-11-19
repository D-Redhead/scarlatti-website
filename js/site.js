/* Scarlatti – gedeeld script: mobiel menu, Guestplan, vandaag-open. Geen dependencies. */
(function () {
  "use strict";
  var lang = document.documentElement.lang === "en" ? "en" : "nl";

  /* ---------- mobiel menu ---------- */
  var toggle = document.querySelector(".menu-toggle");
  var menu = document.getElementById("mobile-menu");
  if (toggle && menu) {
    var label = toggle.querySelector(".menu-label");
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      menu.hidden = !open;
      document.body.classList.toggle("menu-open", open);
      if (label) label.textContent = open ? (lang === "en" ? "Close" : "Sluiten") : "Menu";
      if (open) { var first = menu.querySelector("a"); if (first) first.focus(); }
    };
    toggle.addEventListener("click", function () { setOpen(toggle.getAttribute("aria-expanded") !== "true"); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") { setOpen(false); toggle.focus(); }
    });
    menu.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
    window.matchMedia("(min-width: 1024px)").addEventListener("change", function (m) { if (m.matches) setOpen(false); });
  }

  /* ---------- Guestplan (bestaande widget van scarlatti-leiden.nl) ---------- */
  window._gstpln = { accessKey: "7c2392649f8fa83f25bfa3c863830cfff7a9980a", open: false, locale: lang, useNewsletterSubscription: false };
  var gp = document.createElement("script");
  gp.async = true; gp.src = "https://cdn.guestplan.com/widget.js";
  document.head.appendChild(gp);
  // Guestplan zet een eigen zwevende knop neer; die verbergen we, want elke pagina heeft al
  // een eigen reserveerknop (header + mobiele balk). Lukt dit niet, dan blijft die knop gewoon werken.
  var hideFab = function () {
    var host = document.getElementById("gstpln-widget-host");
    if (!host || !host.shadowRoot) return false;
    if (!host.shadowRoot.getElementById("scar-hide-fab")) {
      var st = document.createElement("style");
      st.id = "scar-hide-fab";
      st.textContent = ".gp-widget--fab{display:none!important}";
      host.shadowRoot.appendChild(st);
    }
    return true;
  };
  var tries = 0;
  var fabTimer = setInterval(function () { if (hideFab() || ++tries > 40) clearInterval(fabTimer); }, 250);
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-reserve]");
    if (!a) return;
    if (window._gstpln && typeof window._gstpln.openWidget === "function") {
      e.preventDefault();
      window._gstpln.openWidget();
    } /* anders: gewone link naar de reserveerinfo (telefoon) */
  });

  /* ---------- vandaag open ---------- */
  // 0 = zondag. Tijden in minuten na middernacht; sluiting na middernacht = > 1440.
  var HOURS = { 0: [630, 1440], 1: null, 2: [630, 1440], 3: [630, 1440], 4: [630, 1440], 5: [630, 1500], 6: [630, 1500] };
  var KITCHEN = [660, 1320];
  var DAYS = lang === "en"
    ? ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    : ["zondag", "maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag"];
  function fmt(m) { m = m % 1440; var h = Math.floor(m / 60), mm = m % 60; return (h < 10 ? "0" : "") + h + ":" + (mm < 10 ? "0" : "") + mm; }
  function nowInLeiden() {
    try {
      var parts = new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Amsterdam", weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23" }).formatToParts(new Date());
      var map = {}; parts.forEach(function (p) { map[p.type] = p.value; });
      var wd = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(map.weekday);
      return { day: wd, min: parseInt(map.hour, 10) * 60 + parseInt(map.minute, 10) };
    } catch (err) { var d = new Date(); return { day: d.getDay(), min: d.getHours() * 60 + d.getMinutes() }; }
  }
  function nextOpenDay(day) { for (var i = 1; i <= 7; i++) { var d = (day + i) % 7; if (HOURS[d]) return d; } return day; }
  function statusText() {
    var n = nowInLeiden(), day = n.day, min = n.min;
    var prev = HOURS[(day + 6) % 7];
    if (prev && prev[1] > 1440 && min < prev[1] - 1440) {
      return { open: true, text: lang === "en" ? "Open now until " + fmt(prev[1]) : "Nu open tot " + fmt(prev[1]) };
    }
    var h = HOURS[day];
    if (!h) {
      var nd = nextOpenDay(day);
      return { open: false, text: lang === "en" ? "Closed today · open again " + DAYS[nd] + " from " + fmt(HOURS[nd][0]) : "Vandaag gesloten · " + DAYS[nd] + " weer open vanaf " + fmt(HOURS[nd][0]) };
    }
    if (min < h[0]) {
      return { open: false, text: lang === "en" ? "Open today " + fmt(h[0]) + "–" + fmt(h[1]) + " · kitchen " + fmt(KITCHEN[0]) + "–" + fmt(KITCHEN[1]) : "Vandaag open " + fmt(h[0]) + "–" + fmt(h[1]) + " · keuken " + fmt(KITCHEN[0]) + "–" + fmt(KITCHEN[1]) };
    }
    if (min < h[1]) {
      var k = min < KITCHEN[0] ? (lang === "en" ? " · kitchen opens at " + fmt(KITCHEN[0]) : " · keuken open vanaf " + fmt(KITCHEN[0]))
        : min < KITCHEN[1] ? (lang === "en" ? " · kitchen until " + fmt(KITCHEN[1]) : " · keuken tot " + fmt(KITCHEN[1]))
        : (lang === "en" ? " · kitchen closed" : " · keuken is dicht");
      return { open: true, text: (lang === "en" ? "Open now until " : "Nu open tot ") + fmt(h[1]) + k };
    }
    var nd2 = nextOpenDay(day);
    return { open: false, text: lang === "en" ? "Closed now · open again " + DAYS[nd2] + " from " + fmt(HOURS[nd2][0]) : "Nu gesloten · " + DAYS[nd2] + " weer open vanaf " + fmt(HOURS[nd2][0]) };
  }
  var s = statusText();
  document.querySelectorAll("[data-today]").forEach(function (el) {
    el.textContent = s.text;
    el.setAttribute("data-state", s.open ? "open" : "closed");
  });
  var today = nowInLeiden().day;
  document.querySelectorAll(".hours tr[data-day]").forEach(function (tr) {
    if (parseInt(tr.getAttribute("data-day"), 10) === today) { tr.classList.add("is-today"); tr.setAttribute("aria-current", "date"); }
  });

  /* ---------- formulieren (Formspree) ---------- */
  var T = lang === "en"
    ? { req: "Please fill in this field.", email: "Please enter a valid email address, like name@example.com.", match: "The email addresses do not match.", check: "Please tick this box to continue.", num: "Please enter a number between 1 and 70.", sending: "Sending…", ok: "Thank you! We have received your message and will get back to you as soon as possible.", fail: "Sending failed. Please try again or call us on 071 512 21 14.", notLinked: "This form is not connected yet (Formspree endpoint missing). Please call 071 512 21 14 or email info@scarlatti-leiden.nl.", fix: "Please check the highlighted fields." }
    : { req: "Vul dit veld in.", email: "Vul een geldig e-mailadres in, zoals naam@voorbeeld.nl.", match: "De e-mailadressen zijn niet hetzelfde.", check: "Vink dit vakje aan om verder te gaan.", num: "Vul een aantal in tussen 1 en 70.", sending: "Bezig met versturen…", ok: "Bedankt! We hebben je bericht ontvangen en nemen zo snel mogelijk contact met je op.", fail: "Versturen is niet gelukt. Probeer het opnieuw of bel ons op 071 512 21 14.", notLinked: "Dit formulier is nog niet gekoppeld (Formspree-endpoint ontbreekt). Bel 071 512 21 14 of mail info@scarlatti-leiden.nl.", fix: "Controleer de gemarkeerde velden." };
  function fieldMsg(el) {
    var v = el.validity;
    if (el.type === "checkbox" && !el.checked && el.required) return T.check;
    if (v.valueMissing) return T.req;
    if (v.typeMismatch && el.type === "email") return T.email;
    if (v.rangeUnderflow || v.rangeOverflow || v.badInput) return T.num;
    if (el.dataset.match) { var o = document.getElementById(el.dataset.match); if (o && o.value.trim().toLowerCase() !== el.value.trim().toLowerCase()) return T.match; }
    return "";
  }
  function showErr(el, msg) {
    var err = document.getElementById(el.id + "-err");
    el.setAttribute("aria-invalid", msg ? "true" : "false");
    if (err) { err.textContent = msg; err.hidden = !msg; }
  }
  document.querySelectorAll("form[data-formspree]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    var ctrls = form.querySelectorAll("input:not([type=hidden]), select, textarea");
    ctrls.forEach(function (el) {
      var ev = el.tagName === "SELECT" || el.type === "checkbox" ? "change" : "blur";
      el.addEventListener(ev, function () { if (el.getAttribute("aria-invalid") === "true" || el.value) showErr(el, fieldMsg(el)); });
      el.addEventListener("input", function () { if (el.getAttribute("aria-invalid") === "true") showErr(el, fieldMsg(el)); });
    });
    // arrangement voorinvullen vanuit ?arrangement=
    var sel = form.querySelector("select[name=arrangement]");
    var q = new URLSearchParams(location.search).get("arrangement");
    if (sel && q && sel.querySelector('option[value="' + q + '"]')) sel.value = q;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var first = null;
      ctrls.forEach(function (el) { var m = fieldMsg(el); showErr(el, m); if (m && !first) first = el; });
      if (first) { status.textContent = T.fix; first.focus(); return; }
      if (form.action.indexOf("AANVULLEN") !== -1) { status.textContent = T.notLinked; return; }
      var btn = form.querySelector("button[type=submit]");
      btn.disabled = true; status.textContent = T.sending;
      fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); status.textContent = T.ok; })
        .catch(function () { status.textContent = T.fail; })
        .then(function () { btn.disabled = false; });
    });
  });

  /* ---------- jaartal footer ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
