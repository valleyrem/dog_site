// Quotes slider, one quote at a time
// home.html
document.addEventListener("DOMContentLoaded", () => {
  const root = document.querySelector("[data-quote-slider]");
  if (!root) return;

  const slides = Array.from(root.querySelectorAll(".quote-slider__slide"));
  if (slides.length < 2) return;

  const dotsBox = root.querySelector("[data-quote-dots]");
  const dots = [];
  let current = 0;

  const show = (i) => {
    slides[current].classList.remove("is-active");
    dots[current].classList.remove("is-active");
    dots[current].removeAttribute("aria-current");
    current = (i + slides.length) % slides.length;
    slides[current].classList.add("is-active");
    dots[current].classList.add("is-active");
    dots[current].setAttribute("aria-current", "true");
    schedule();
  };

  // the quotes turn by themselves; any turn (also a manual one) restarts the wait
  let timer = null;
  let hovered = false;
  let visible = true;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function schedule() {
    clearTimeout(timer);
    if (reduce) return;
    timer = setTimeout(() => {
      if (document.hidden || hovered || !visible) schedule();
      else show(current + 1);
    }, 8000);
  }
  root.addEventListener("mouseenter", () => (hovered = true));
  root.addEventListener("mouseleave", () => (hovered = false));
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(
      (entries) => (visible = entries[0].isIntersecting),
    ).observe(root);
  }
  schedule();

  slides.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.type = "button";
    dot.className = "quote-slider__dot" + (i === 0 ? " is-active" : "");
    dot.setAttribute("aria-label", String(i + 1));
    if (i === 0) dot.setAttribute("aria-current", "true");
    dot.addEventListener("click", () => show(i));
    dotsBox.appendChild(dot);
    dots.push(dot);
  });

  // a swipe to the side turns the quote
  const stage = root.querySelector(".quote-slider__stage");
  let startX = 0;
  let startY = 0;
  stage.addEventListener(
    "touchstart",
    (e) => {
      startX = e.touches[0].clientX;
      startY = e.touches[0].clientY;
    },
    { passive: true },
  );
  stage.addEventListener(
    "touchend",
    (e) => {
      const dx = e.changedTouches[0].clientX - startX;
      const dy = e.changedTouches[0].clientY - startY;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy) * 1.5) {
        show(current + (dx < 0 ? 1 : -1));
      }
    },
    { passive: true },
  );
});

// Custom navigation selects (home: groups and breeds)
document.addEventListener("DOMContentLoaded", () => {
  function initNavSelect(cfg) {
    const custom = document.getElementById(cfg.customId);
    const trigger = document.getElementById(cfg.triggerId);
    const list = document.getElementById(cfg.listId);
    const select = document.getElementById(cfg.selectId);
    const triggerText = document.getElementById(cfg.triggerTextId);

    if (!custom || !trigger || !list || !select || !triggerText) return;

    fillListFromSelect(list, select);

    function closeList() {
      list.hidden = true;
      trigger.setAttribute("aria-expanded", "false");
    }

    trigger.addEventListener("click", (e) => {
      e.stopPropagation();
      const willOpen = list.hidden;
      list.hidden = !willOpen;
      trigger.setAttribute("aria-expanded", String(willOpen));
    });

    // Clicking anywhere outside a custom select closes all open lists.
    // Capture phase needed: stop-propagation on the trigger doesn't block
    // interception, and a click on another trigger closes the rest.
    document.addEventListener(
      "click",
      (e) => {
        const customEl = e.target.closest(".custom-select");
        document.querySelectorAll(".custom-select-list").forEach((openList) => {
          if (openList.hidden) return;
          if (customEl && customEl.contains(openList)) return;
          openList.hidden = true;
          const openTrigger = openList.parentElement.querySelector(
            ".custom-select-trigger",
          );
          if (openTrigger) openTrigger.setAttribute("aria-expanded", "false");
        });
      },
      true,
    );

    list.addEventListener("click", (e) => {
      const item = e.target.closest(".custom-select-item");
      if (!item) return;

      select.value = item.dataset.value;

      const span = item.querySelector("span");
      if (span) triggerText.textContent = span.textContent.trim();

      closeList();

      if (item.dataset.value) {
        window.location.href = item.dataset.value;
      }
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && list && !list.hidden) closeList();
    });

    // These selects are links: coming back to the page (Back button, swipe)
    // the browser may restore it as it was left, so the chosen name is put
    // back to the hint
    const hint = triggerText.textContent;
    window.addEventListener("pageshow", (e) => {
      if (!e.persisted) return;
      select.value = "";
      triggerText.textContent = hint;
      closeList();
    });
  }

  // Groups: as text, no photos
  initNavSelect({
    customId: "groupCustom",
    triggerId: "groupTrigger",
    listId: "groupList",
    selectId: "breed-select",
    triggerTextId: "groupTriggerText",
  });

  // Breeds
  initNavSelect({
    customId: "breedCustom",
    triggerId: "breedTrigger",
    listId: "breedList",
    selectId: "breed-select-1",
    triggerTextId: "breedTriggerText",
  });
});

// Homepage "breed of the day": the button swaps in another breed from the
// list the page carries as JSON (no request). Without JS the button stays
// hidden and the day's breed is just a plain block.
(function () {
  var root = document.querySelector("[data-breed-day]");
  var dataEl = document.getElementById("home-breeds");
  var next = root && root.querySelector("[data-breed-day-next]");
  if (!root || !dataEl || !next) return;

  var breeds;
  try {
    breeds = JSON.parse(dataEl.textContent);
  } catch (e) {
    return;
  }
  if (!breeds || breeds.length < 2) return;

  var current = root.dataset.current;
  var links = root.querySelectorAll("[data-day-link]");
  var photo = root.querySelector("[data-day-photo]");
  var set = function (sel, text) {
    var el = root.querySelector(sel);
    if (el) el.textContent = text;
  };

  next.hidden = false;
  next.addEventListener("click", function () {
    var pool = breeds.filter(function (b) {
      return b.u !== current;
    });
    var pick = pool[Math.floor(Math.random() * pool.length)];
    current = pick.u;
    links.forEach(function (a) {
      a.setAttribute("href", pick.u);
    });
    if (photo && pick.p) photo.setAttribute("src", pick.p);
    set("[data-day-group]", pick.g);
    set("[data-day-title]", pick.t);
    set("[data-day-sr]", " " + pick.t);
    set("[data-day-summary]", pick.s);
    set("[data-day-size]", pick.z || "");
    var weightEl = root.querySelector("[data-day-weight]");
    if (weightEl) setWithSexMarks(weightEl, pick.w || "");
    set("[data-day-life]", pick.l || "");
    set("[data-day-origin]", pick.o || "");
  });
})();

/* Enjoy photos: a click opens the photo large in a dialog; it closes with the
   cross, Esc or a click outside the photo. */
(function () {
  var dialog = document.querySelector("[data-enjoy-lightbox]");
  var frames = document.querySelectorAll(".enjoy-photo__frame");
  if (!dialog || !frames.length || typeof dialog.showModal !== "function")
    return;

  var img = dialog.querySelector("[data-enjoy-img]");
  var credit = dialog.querySelector("[data-enjoy-credit]");

  var largest = function (frame) {
    var source = frame.querySelector("source[srcset]");
    if (source) {
      var parts = source.getAttribute("srcset").split(",");
      var last = parts[parts.length - 1].trim().split(/\s+/)[0];
      if (last) return last;
    }
    return (
      frame.querySelector(".enjoy-slide__img") || frame.querySelector("img")
    ).currentSrc;
  };

  var opened = null;
  var byKey = false;

  var open = function (frame) {
    opened = frame;
    var photo =
      frame.querySelector(".enjoy-slide__img") || frame.querySelector("img");
    var author = frame.querySelector(".post-photo-author");
    img.src = largest(frame);
    img.alt = photo.alt;
    credit.textContent = author ? author.textContent : "";
    dialog.showModal();
  };

  frames.forEach(function (frame) {
    frame.setAttribute("role", "button");
    frame.setAttribute("tabindex", "0");
    frame.addEventListener("click", function () {
      byKey = false;
      open(frame);
    });
    frame.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        byKey = true;
        open(frame);
      }
    });
  });

  dialog
    .querySelector("[data-enjoy-close]")
    .addEventListener("click", function () {
      dialog.close();
    });
  dialog.addEventListener("click", function (e) {
    if (e.target === dialog) dialog.close();
  });
  // A swipe down closes the dialog on touch screens: the photo follows the
  // finger and goes if it was pulled far enough
  var startY = null;
  var pull = 0;
  var pulled = [img, credit];

  var drag = function (y) {
    pulled.forEach(function (el) {
      el.style.transition = "none";
      el.style.transform = y ? "translateY(" + y + "px)" : "";
      el.style.opacity = y ? String(Math.max(0.35, 1 - y / 400)) : "";
    });
  };

  var release = function () {
    pulled.forEach(function (el) {
      el.style.transition = "transform 0.2s ease, opacity 0.2s ease";
      el.style.transform = "";
      el.style.opacity = "";
    });
  };

  dialog.addEventListener(
    "touchstart",
    function (e) {
      startY = e.touches.length === 1 ? e.touches[0].clientY : null;
      pull = 0;
    },
    { passive: true },
  );

  dialog.addEventListener(
    "touchmove",
    function (e) {
      if (startY === null) return;
      pull = Math.max(0, e.touches[0].clientY - startY);
      drag(pull);
    },
    { passive: true },
  );

  dialog.addEventListener("touchend", function () {
    if (startY === null) return;
    var far = pull > 90;
    startY = null;
    pull = 0;
    if (far) {
      dialog.close();
    }
    release();
  });

  dialog.addEventListener("close", function () {
    img.removeAttribute("src");
    // after a tap or click the photo must not keep a focus ring
    if (opened && !byKey) opened.blur();
  });
})();
