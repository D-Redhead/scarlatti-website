/* Restaurant Scarlatti — gedrag. Werkt zonder frameworks; zonder JS blijft alles bruikbaar. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  /* ---------- Openingstijden (één bron) ---------- */
  // 0 = zondag … 6 = zaterdag. Tijden in Europe/Amsterdam.
  var HOURS = {
    0: ["10:30", "21:30"], 1: ["11:30", "21:30"], 2: ["10:30", "21:30"],
    3: ["10:30", "21:30"], 4: ["10:30", "21:30"], 5: ["10:30", "21:30"], 6: ["10:30", "21:30"]
  };

  function nowInLeiden() {
    var parts = new Intl.DateTimeFormat("en-GB", {
      timeZone: "Europe/Amsterdam", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false
    }).formatToParts(new Date());
    var get = function (t) { return (parts.find(function (p) { return p.type === t; }) || {}).value; };
    var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    return { day: days[get("weekday")], minutes: parseInt(get("hour"), 10) % 24 * 60 + parseInt(get("minute"), 10) };
  }
  function toMin(t) { var p = t.split(":"); return +p[0] * 60 + +p[1]; }

  var now = nowInLeiden();
  var today = HOURS[now.day];

  document.querySelectorAll("[data-open-status]").forEach(function (el) {
    var open = today && now.minutes >= toMin(today[0]) && now.minutes < toMin(today[1]);
    if (open) {
      el.textContent = "Nu open · tot " + today[1];
      el.classList.add("is-open");
    } else if (today && now.minutes < toMin(today[0])) {
      el.textContent = "Vandaag open vanaf " + today[0];
    } else {
      var next = HOURS[(now.day + 1) % 7];
      el.textContent = "Gesloten · morgen vanaf " + next[0];
    }
  });

  document.querySelectorAll(".hours tr[data-days]").forEach(function (tr) {
    if (tr.getAttribute("data-days").split(",").indexOf(String(now.day)) > -1) {
      tr.classList.add("is-today");
      tr.querySelector("th").insertAdjacentHTML("beforeend", ' <span class="visually-hidden">(vandaag)</span>');
    }
  });

  /* ---------- Navigatie ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  function setNav(open) {
    toggle.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
  }
  if (toggle && nav) {
    toggle.addEventListener("click", function () { setNav(toggle.getAttribute("aria-expanded") !== "true"); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) { setNav(false); toggle.focus(); }
    });
    nav.addEventListener("click", function (e) { if (e.target.closest("a")) setNav(false); });
  }

  /* ---------- Reserveren: Guestplan in één tik ---------- */
  // Valt terug op de link (contactpagina met telefoonnummer) als de widget niet geladen is.
  document.addEventListener("click", function (e) {
    var trigger = e.target.closest("[data-book]");
    if (!trigger) return;
    var gp = window._gstpln;
    if (gp && typeof gp.openBookingWidget === "function") {
      e.preventDefault();
      try { gp.openBookingWidget(); } catch (err) { window.location.href = trigger.href; }
    }
  });

  /* ---------- Subnavigatie menukaart ---------- */
  var subLinks = document.querySelectorAll(".subnav a");
  if (subLinks.length && "IntersectionObserver" in window) {
    var map = {};
    subLinks.forEach(function (a) { map[a.hash.slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && map[en.target.id]) {
          subLinks.forEach(function (a) { a.classList.remove("is-active"); a.removeAttribute("aria-current"); });
          map[en.target.id].classList.add("is-active");
          map[en.target.id].setAttribute("aria-current", "true");
        }
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    document.querySelectorAll(".menu-section").forEach(function (s) { spy.observe(s); });
  }

  /* ---------- Reveal ---------- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var reveals = document.querySelectorAll(".reveal");
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---------- Formulieren → e-mail (geen server nodig) ---------- */
  var MAIL = "info@scarlatti-leiden.nl";

  function validate(form) {
    var firstBad = null;
    form.querySelectorAll("[required]").forEach(function (f) {
      var err = document.getElementById(f.id + "-error");
      var bad = !f.value.trim() || (f.type === "email" && !/^\S+@\S+\.\S+$/.test(f.value));
      f.setAttribute("aria-invalid", String(bad));
      if (err) err.textContent = bad ? (f.dataset.error || "Vul dit veld in.") : "";
      if (bad && !firstBad) firstBad = f;
    });
    if (firstBad) firstBad.focus();
    return !firstBad;
  }

  document.querySelectorAll("form[data-mailform]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(form)) return;
      var lines = [];
      form.querySelectorAll("[name]").forEach(function (f) {
        if (f.value.trim()) lines.push(f.dataset.label + ": " + f.value.trim());
      });
      var subject = form.dataset.subject;
      var date = form.querySelector("[name=datum]");
      var size = form.querySelector("[name=personen]");
      if (date && date.value) subject += " · " + date.value;
      if (size && size.value) subject += " · " + size.value + " pers.";
      var href = "mailto:" + MAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
      var status = form.querySelector(".form-status");
      status.hidden = false;
      status.innerHTML = "Je mailprogramma opent met je aanvraag. Opent er niets? Mail naar <strong>" + MAIL +
        "</strong> of bel <strong>071 512 21 14</strong>.";
      status.focus();
      window.location.href = href;
    });
  });
})();
