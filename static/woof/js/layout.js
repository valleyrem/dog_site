// Burger menu

const burger = document.getElementById("burger-btn");

if (burger) {
  const icon = document.getElementById("burger-icon");
  const sidebar = document.querySelector(".sidebar-nav");
  const body = document.body;

  const listIcon = burger.dataset.listIcon;
  const closeIcon = burger.dataset.closeIcon;

  function closeMenu() {
    sidebar.classList.remove("active");
    body.classList.remove("sidebar-open");

    icon.src = listIcon;
    icon.alt = "Menu";
  }

  burger.addEventListener("click", (e) => {
    e.stopPropagation();

    const isActive = sidebar.classList.toggle("active");

    body.classList.toggle("sidebar-open");

    icon.src = isActive ? closeIcon : listIcon;
    icon.alt = isActive ? "Close menu" : "Menu";
  });

  document.addEventListener("click", (e) => {
    if (sidebar && !sidebar.contains(e.target) && !burger.contains(e.target)) {
      closeMenu();
    }
  });
}

// Scroll to top button

document.addEventListener("DOMContentLoaded", function () {
  const scrollBtn = document.getElementById("scroll-top-button");

  if (!scrollBtn) return;

  function toggleButton() {
    scrollBtn.classList.toggle("show", window.scrollY > 190);
  }

  window.addEventListener("scroll", toggleButton, { passive: true });

  scrollBtn.addEventListener("click", function () {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  toggleButton();
});

// Reading progress bar under the header: fills to the right as the page
// scrolls down, retreats to the left on the way up — how much is left to read.
(function () {
  const bar = document.querySelector(".reading-progress");
  if (!bar) return;

  const fill = bar.querySelector(".reading-progress__fill");
  let ticking = false;

  function update() {
    const doc = document.documentElement;
    const footer = document.querySelector(".site-footer");
    // the bar completes when the footer enters the view, not after it
    const max =
      doc.scrollHeight -
      window.innerHeight -
      (footer ? footer.offsetHeight : 0);
    const y = window.scrollY || doc.scrollTop || 0;

    // no scrollable content — hide the strip
    if (max <= 4) {
      bar.classList.add("is-idle");
      fill.style.width = "0%";
      ticking = false;
      return;
    }

    bar.classList.remove("is-idle");
    const pct = Math.min(100, Math.max(0, (y / max) * 100));
    fill.style.width = pct.toFixed(2) + "%";
    ticking = false;
  }

  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    },
    { passive: true },
  );

  window.addEventListener("resize", update, { passive: true });
  update();
})();

// Reveal a breed card only once its lazy photo has loaded, so the title
// never appears before the image. The whole card fades in together (short,
// flat opacity). Cards without a photo reveal immediately; without JS the
// `.js` class is absent and cards render normally.
(function () {
  function reveal(card) {
    card.classList.add("is-loaded");
  }

  function init(scope) {
    (scope || document).querySelectorAll(".dog-card").forEach(function (card) {
      var img = card.querySelector(".dog-card__avatar");
      if (!img) {
        reveal(card); // nothing to wait for
        return;
      }
      if (img.complete) {
        reveal(card); // already cached (or errored) — show right away
      } else {
        img.addEventListener(
          "load",
          function () {
            reveal(card);
          },
          { once: true },
        );
        img.addEventListener(
          "error",
          function () {
            reveal(card);
          },
          { once: true },
        );
      }
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    init();
  });
})();
