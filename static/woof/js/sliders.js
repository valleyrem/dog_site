// Dog slider

document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector(".dog-slider-track");
  const items = [...document.querySelectorAll(".dog-card-link")];

  if (!track || !items.length) return;

  const prev = document.querySelector(".slider-prev");
  const next = document.querySelector(".slider-next");
  const nav = document.querySelector(".slider-nav");
  const dotsWrap = document.querySelector(".slider-dots");
  const pagination = document.querySelector(".slider-pagination");

  // Related / group-of-breeds blocks (post + category pages): on
  // tablets and desktops the slider turns into a grid with a "Show more"
  // button (4 columns); phones keep the
  // arrows slider with swipe.
  const relatedBlock = track.closest(".related-block");
  // group pages (data-initial-*) open with two rows: 5x2 on desktops, 4x2 on tablets
  const relatedPerRow = () => {
    const key = window.innerWidth < 1024 ? "initialTablet" : "initialDesktop";
    const fallback = window.innerWidth < 1024 ? 4 : 5;
    return (
      (relatedBlock && parseInt(relatedBlock.dataset[key], 10)) || fallback
    );
  };
  let relatedShown = relatedPerRow();
  const showMoreBtn = document.querySelector(".slider-showmore");
  const moreLabel = showMoreBtn ? showMoreBtn.dataset.labelMore : "";
  const lessLabel = showMoreBtn ? showMoreBtn.dataset.labelLess : "";

  // Above this page count we stop adding dots and group them
  // (on the home page with all breeds there are only ~9).
  const MAX_DOTS = 9;

  function dotCount() {
    return Math.min(getPages(), MAX_DOTS);
  }

  function dotForPage(page) {
    const pages = getPages();
    if (pages <= MAX_DOTS) return page;
    return Math.round((page * (MAX_DOTS - 1)) / (pages - 1));
  }

  function pageForDot(dot) {
    const pages = getPages();
    if (pages <= MAX_DOTS) return dot;
    return Math.round((dot * (pages - 1)) / (MAX_DOTS - 1));
  }

  let page = 0;
  let holdInterval = null;

  function getPerPage() {
    // phones and small tablets show two cards per view — flip by pairs;
    // the desktop grid lays out five columns, so flip full pages of five.
    if (window.innerWidth <= 767) return 2;
    if (window.innerWidth >= 1024) return 5;
    return 4;
  }

  function getPages() {
    return Math.ceil(items.length / getPerPage());
  }

  function renderDots() {
    if (!dotsWrap) return;

    // Dots: one per page when there are few;
    // on the home page (many pages) — cap at ~9 dots,
    // each standing for a range of pages.
    const count = dotCount();

    if (dotsWrap.children.length !== count) {
      dotsWrap.innerHTML = "";

      for (let i = 0; i < count; i++) {
        const dot = document.createElement("button");
        dot.type = "button";
        dot.className = "slider-dot";
        dot.setAttribute("aria-label", `Page ${i + 1}`);
        dot.addEventListener("click", () => {
          page = pageForDot(i);
          update();
        });
        dotsWrap.appendChild(dot);
      }
    }
  }

  function updateDots() {
    if (!dotsWrap) return;

    const active = dotForPage(page);

    [...dotsWrap.children].forEach((dot, i) => {
      dot.classList.toggle("is-active", i === active);
    });
  }

  function update() {
    const gridMode = !!relatedBlock && window.innerWidth > 767;

    if (gridMode) {
      track.style.transform = "";
      track.classList.remove("is-single");
      if (pagination) pagination.style.display = "none";
      if (dotsWrap) dotsWrap.style.display = "none";
      items.forEach((card, index) => {
        card.classList.toggle("is-more-hidden", index >= relatedShown);
      });
      const arrows = document.querySelectorAll(".slider-nav .slider-arrow");
      arrows.forEach((a) => a.classList.add("is-hidden"));
      // no arrows above the cards -> the reserved strip is not needed
      if (nav) nav.classList.add("no-controls");
      if (showMoreBtn) {
        const expandable = items.length > relatedPerRow();
        const allShown = relatedShown >= items.length;
        showMoreBtn.hidden = !expandable;
        // the same button becomes "Show less" when every card is open
        showMoreBtn.textContent = allShown ? lessLabel : moreLabel;
        showMoreBtn.classList.toggle("is-showless", allShown);
      }
      return;
    }

    const perPage = getPerPage();

    // A single card in the slider (e.g. a group with one breed):
    // center it instead of the left position.
    track.classList.toggle("is-single", items.length === 1);

    page = Math.max(0, Math.min(page, getPages() - 1));

    const gap = parseFloat(getComputedStyle(track).gap) || 0;
    const itemWidth = items[0].getBoundingClientRect().width + gap;
    // never slide past the last card: on an uneven count the final page
    // stops flush with the tail of the track
    const maxShift = Math.max(0, (items.length - perPage) * itemWidth);
    const shift = Math.min(page * perPage * itemWidth, maxShift);

    track.style.transform = `translateX(-${shift}px)`;

    renderDots();
    updateDots();

    const currentNum = document.querySelector(".slider-current");
    const totalNum = document.querySelector(".slider-total");

    if (currentNum) currentNum.textContent = page + 1;
    if (totalNum) totalNum.textContent = getPages();

    prev.classList.toggle("disabled", page === 0);
    next.classList.toggle("disabled", page >= getPages() - 1);

    const hideControls =
      (window.innerWidth > 912 && items.length <= 3) ||
      (window.innerWidth <= 767 && items.length <= 1) ||
      (window.innerWidth <= 912 && items.length <= 2);

    if (pagination) {
      pagination.style.display = hideControls ? "none" : "";
    }

    if (dotsWrap) {
      dotsWrap.style.display = hideControls ? "none" : "";
    }

    const arrows = document.querySelectorAll(".slider-nav .slider-arrow");
    // We do not fully hide arrows (display:none), only make them invisible:
    // they keep their place in the row, so the slider area does not
    // widen and a single card keeps its normal width.
    arrows.forEach((a) => {
      a.classList.toggle("is-hidden", hideControls);
    });

    // With nothing to click (a group with one breed) the strip reserved
    // above the cards for the arrows is empty space — collapse it.
    if (nav) nav.classList.toggle("no-controls", hideControls);
  }

  function startHold(direction) {
    stopHold();

    holdInterval = setInterval(() => {
      const maxPage = getPages() - 1;

      if (direction === "next" && page < maxPage) {
        page++;
        update();
      }

      if (direction === "prev" && page > 0) {
        page--;
        update();
      }
    }, 180);
  }

  function stopHold() {
    if (holdInterval) {
      clearInterval(holdInterval);
      holdInterval = null;
    }
  }

  next.addEventListener("click", () => {
    if (holdInterval) return;

    if (page < getPages() - 1) {
      page++;
      update();
    }
  });

  if (showMoreBtn) {
    showMoreBtn.addEventListener("click", () => {
      if (showMoreBtn.classList.contains("is-showless")) {
        // collapse back to the initial row
        relatedShown = relatedPerRow();
        update();
        track.scrollIntoView({ behavior: "smooth", block: "start" });
      } else {
        relatedShown += relatedPerRow();
        update();
      }
    });
  }

  prev.addEventListener("click", () => {
    if (holdInterval) return;

    if (page > 0) {
      page--;
      update();
    }
  });

  next.addEventListener("mousedown", () => startHold("next"));
  next.addEventListener("touchstart", () => startHold("next"), {
    passive: true,
  });

  next.addEventListener("mouseup", stopHold);
  next.addEventListener("mouseleave", stopHold);
  next.addEventListener("touchend", stopHold);
  next.addEventListener("touchcancel", stopHold);

  prev.addEventListener("mousedown", () => startHold("prev"));
  prev.addEventListener("touchstart", () => startHold("prev"), {
    passive: true,
  });

  prev.addEventListener("mouseup", stopHold);
  prev.addEventListener("mouseleave", stopHold);
  prev.addEventListener("touchend", stopHold);
  prev.addEventListener("touchcancel", stopHold);

  // Swipe on the track (touch): page through; arrows and swipe don't conflict
  const viewport = document.querySelector(".dog-slider");
  let swipe = null;
  let swipeClickSuppress = 0;

  function swipeBase() {
    const m = track.style.transform.match(/-?\d+(\.\d+)?/);
    return m ? parseFloat(m[0]) : 0;
  }

  if (viewport) {
    viewport.addEventListener("pointerdown", (e) => {
      if (e.pointerType !== "touch") return;
      swipe = { x: e.clientX, y: e.clientY, base: swipeBase() };
      track.style.transition = "none";
      viewport.setPointerCapture(e.pointerId);
    });

    viewport.addEventListener("pointermove", (e) => {
      if (!swipe) return;
      const dx = e.clientX - swipe.x;
      const dy = e.clientY - swipe.y;
      if (Math.abs(dx) > Math.abs(dy)) {
        track.style.transform = `translateX(${swipe.base + dx}px)`;
      }
    });

    const releaseSwipe = (e) => {
      if (!swipe) return;
      const dx = e.clientX - swipe.x;
      const dy = e.clientY - swipe.y;
      swipe = null;
      track.style.transition = "";
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
        swipeClickSuppress = Date.now();
        if (dx < 0 && page < getPages() - 1) page++;
        else if (dx > 0 && page > 0) page--;
      }
      update();
    };

    viewport.addEventListener("pointerup", releaseSwipe);
    viewport.addEventListener("pointercancel", releaseSwipe);

    // after a swipe, don't let a tap on the card act as navigation
    track.addEventListener(
      "click",
      (e) => {
        if (Date.now() - swipeClickSuppress < 400) {
          e.preventDefault();
          e.stopPropagation();
        }
      },
      true,
    );
  }
  let resizeTimeout;

  window.addEventListener("resize", () => {
    clearTimeout(resizeTimeout);

    resizeTimeout = setTimeout(update, 100);
  });

  update();
});

// Explore groups slider script
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".group-item").forEach((group) => {
    const list = group.querySelector(".group-dogs");
    const prev = group.querySelector(".group-arrow-left");
    const next = group.querySelector(".group-arrow-right");

    let page = 0;

    function setupSlider() {
      const itemsPerPage = 4;

      const totalItems = list.children.length;
      const totalPages = Math.ceil(totalItems / itemsPerPage);

      if (page >= totalPages) {
        page = Math.max(0, totalPages - 1);
      }

      /*
       * Each page is one column
       * containing 4 dog breeds.
       */
      list.style.width = `${totalPages * 100}%`;

      list.style.gridTemplateColumns = `repeat(${totalPages}, minmax(0, 1fr))`;

      list.style.gridTemplateRows = `repeat(${itemsPerPage}, auto)`;

      const offset = page * (100 / totalPages);

      list.style.transform = `translateX(-${offset}%)`;

      prev.disabled = page === 0;
      next.disabled = page === totalPages - 1;

      if (totalPages <= 1) {
        prev.style.visibility = "hidden";
        next.style.visibility = "hidden";
      } else {
        prev.style.visibility = "visible";
        next.style.visibility = "visible";
      }

      group.sliderTotalPages = totalPages;

      list.classList.remove("slider-loading");
    }

    prev.addEventListener("click", function () {
      if (page > 0) {
        page--;

        setupSlider();
      }
    });

    next.addEventListener("click", function () {
      if (page < group.sliderTotalPages - 1) {
        page++;

        setupSlider();
      }
    });

    window.addEventListener("resize", function () {
      setupSlider();
    });

    setupSlider();
  });
});

// Mobile category scroll script

document.addEventListener("DOMContentLoaded", () => {
  if (window.innerWidth > 768) return;

  const active = document.querySelector(".category-chip.active");

  if (!active) return;

  active.scrollIntoView({
    behavior: "auto",
    inline: "center",
    block: "nearest",
  });
});
