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

  window.addEventListener("scroll", toggleButton);

  scrollBtn.addEventListener("click", function () {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  toggleButton();
});

// Dog slider

document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector(".dog-slider-track");
  const items = [...document.querySelectorAll(".dog-card-link")];

  if (!track || !items.length) return;

  const prev = document.querySelector(".slider-prev");
  const next = document.querySelector(".slider-next");
  const dotsWrap = document.querySelector(".slider-dots");

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
    if (window.innerWidth <= 767) return 1;
    if (window.innerWidth <= 912) return 2;
    return 3;
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
    const perPage = getPerPage();

    // A single card in the slider (e.g. a group with one breed):
    // center it instead of the left position.
    track.classList.toggle("is-single", items.length === 1);

    page = Math.max(0, Math.min(page, getPages() - 1));

    const gap = parseFloat(getComputedStyle(track).gap) || 0;
    const itemWidth = items[0].getBoundingClientRect().width + gap;
    const shift = page * perPage * itemWidth;

    track.style.transform = `translateX(-${shift}px)`;

    renderDots();
    updateDots();

    const currentNum = document.querySelector(".slider-current");
    const totalNum = document.querySelector(".slider-total");

    if (currentNum) currentNum.textContent = page + 1;
    if (totalNum) totalNum.textContent = getPages();

    prev.classList.toggle("disabled", page === 0);
    next.classList.toggle("disabled", page >= getPages() - 1);

    const pagination = document.querySelector(".slider-pagination");

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

// Gallery / modal
// post.html

document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("modal");

  if (!modal) return;

  const modalImg = document.getElementById("modal-img");
  const modalAuthor = document.getElementById("modal-author");

  const closeBtn = modal.querySelector(".close");
  const prevModalBtn = modal.querySelector(".modal-arrow.prev");
  const nextModalBtn = modal.querySelector(".modal-arrow.next");

  const mainImage = document.querySelector(".post-image");
  const galleryImages = Array.from(document.querySelectorAll(".gallery-image"));

  if (!mainImage) return;

  // IMAGES

  const images = [
    {
      src: mainImage.src,
      author: mainImage.dataset.author || "",
    },
    ...galleryImages.map((img) => ({
      src: img.src,
      author: img.dataset.author || "",
    })),
  ];

  let currentIndex = 0;
  let scrollY = 0;

  // MAIN IMAGE

  function updateMainImage() {
    const image = images[currentIndex];

    mainImage.src = image.src;
    mainImage.dataset.author = image.author || "";

    const postAuthor = document.getElementById("post-photo-author");

    if (postAuthor) {
      postAuthor.textContent = image.author || "";
    }
  }

  const prevMain = document.querySelector(".main-img-arrow.prev");

  const nextMain = document.querySelector(".main-img-arrow.next");

  prevMain?.addEventListener("click", function (e) {
    e.stopPropagation();

    currentIndex = (currentIndex - 1 + images.length) % images.length;

    updateMainImage();
  });

  nextMain?.addEventListener("click", function (e) {
    e.stopPropagation();

    currentIndex = (currentIndex + 1) % images.length;

    updateMainImage();
  });

  // MODAL

  function showModal(index) {
    currentIndex = index;

    const image = images[currentIndex];

    scrollY = window.scrollY;

    modal.classList.add("active");

    modalImg.src = image.src;
    modalAuthor.textContent = image.author || "";

    document.documentElement.classList.add("no-scroll");
    document.body.classList.add("no-scroll");

    resetZoom();
  }

  function closeModal() {
    modal.classList.remove("active");

    document.documentElement.classList.remove("no-scroll");
    document.body.classList.remove("no-scroll");

    resetZoom();

    window.scrollTo({
      top: scrollY,
      behavior: "auto",
    });
  }

  // Main image → modal

  mainImage.addEventListener("click", function () {
    showModal(currentIndex);
  });

  // Gallery images → modal

  galleryImages.forEach(function (img, index) {
    img.addEventListener("click", function () {
      showModal(index + 1);
    });
  });

  // Modal arrows

  prevModalBtn?.addEventListener("click", function (e) {
    e.stopPropagation();

    showModal((currentIndex - 1 + images.length) % images.length);
  });

  nextModalBtn?.addEventListener("click", function (e) {
    e.stopPropagation();

    showModal((currentIndex + 1) % images.length);
  });

  // Close

  closeBtn?.addEventListener("click", closeModal);

  modal.addEventListener("click", function (e) {
    if (e.target === modal) {
      closeModal();
    }
  });

  // =========================
  // KEYBOARD
  // =========================

  document.addEventListener("keydown", function (e) {
    if (!modal.classList.contains("active")) return;

    if (e.key === "ArrowLeft") {
      showModal((currentIndex - 1 + images.length) % images.length);
    }

    if (e.key === "ArrowRight") {
      showModal((currentIndex + 1) % images.length);
    }

    if (e.key === "Escape") {
      closeModal();
    }
  });

  // =========================
  // ZOOM: mouse wheel + drag + pinch
  // =========================

  const zoomLevelEl = document.getElementById("modal-zoom");

  const MIN_SCALE = 1;
  const MAX_SCALE = 5;

  let scale = 1;
  let tx = 0;
  let ty = 0;

  const zoomPointers = new Map();
  let pinchStartDist = 0;
  let pinchStartScale = 1;
  let pinchMid = null;
  let pinchStartTx = 0;
  let pinchStartTy = 0;
  let dragStart = null;
  let wasDragged = false;
  let zoomWasActive = false;

  function clampZoomValue(v) {
    return Math.max(MIN_SCALE, Math.min(MAX_SCALE, v));
  }

  function clampPan() {
    const rect = modalImg.getBoundingClientRect();
    const vw = modal.clientWidth - 64;
    const vh = modal.clientHeight - 64;

    const maxX = Math.max(0, (rect.width - vw) / 2);
    const maxY = Math.max(0, (rect.height - vh) / 2);

    tx = Math.max(-maxX, Math.min(maxX, tx));
    ty = Math.max(-maxY, Math.min(maxY, ty));
  }

  function applyZoom() {
    modalImg.style.transform = `translate(${tx}px, ${ty}px) scale(${scale})`;

    const zoomed = scale > 1;

    if (zoomLevelEl) {
      zoomLevelEl.textContent = `${Math.round(scale * 100)}%`;
      zoomLevelEl.classList.toggle("show", zoomed);
    }

    // when zoomed, hide the navigation arrows
    // so they don't get confused with panning
    modal.querySelectorAll(".modal-arrow").forEach((a) => {
      a.style.opacity = zoomed ? "0" : "";
      a.style.pointerEvents = zoomed ? "none" : "";
    });
  }

  function resetZoom() {
    scale = 1;
    tx = 0;
    ty = 0;

    modalImg.style.transform = "";
    modalImg.style.transition = "";

    if (zoomLevelEl) {
      zoomLevelEl.textContent = "100%";
      zoomLevelEl.classList.remove("show");
    }

    modal.querySelectorAll(".modal-arrow").forEach((a) => {
      a.style.opacity = "";
      a.style.pointerEvents = "";
    });
  }

  // Double tap/click zoom: zoom to the touch point
  function zoomInAt(clientX, clientY) {
    const rect = modalImg.getBoundingClientRect();

    const imgX = clientX - rect.left;
    const imgY = clientY - rect.top;

    scale = 2;
    tx = imgX * (1 - scale);
    ty = imgY * (1 - scale);

    clampPan();
    applyZoom();
  }

  // Double press: at scale 1 — zoom in,
  // when zoomed — back to original
  function toggleZoom(clientX, clientY) {
    if (scale > 1) {
      resetZoom();
    } else {
      zoomInAt(clientX, clientY);
    }
  }

  // Mouse wheel — zoom to the point under the cursor

  modalImg.addEventListener(
    "wheel",
    (e) => {
      e.preventDefault();

      const rect = modalImg.getBoundingClientRect();
      const px = e.clientX - rect.left;
      const py = e.clientY - rect.top;

      const factor = e.deltaY < 0 ? 1.12 : 1 / 1.12;
      const nextScale = clampZoomValue(scale * factor);

      if (nextScale === scale) return;

      const k = nextScale / scale;

      tx = px - (px - tx) * k;
      ty = py - (py - ty) * k;

      scale = nextScale;

      modalImg.style.transition = "none";
      clampPan();
      applyZoom();
      requestAnimationFrame(() => {
        modalImg.style.transition = "";
      });
    },
    { passive: false },
  );

  // Drag with mouse / finger + two-finger pinch

  modalImg.addEventListener("pointerdown", (e) => {
    zoomPointers.set(e.pointerId, { x: e.clientX, y: e.clientY });

    try {
      modalImg.setPointerCapture(e.pointerId);
    } catch (err) {
      /* ignore */
    }

    modalImg.style.transition = "none";

    if (zoomPointers.size === 1) {
      dragStart = { x: e.clientX, y: e.clientY, tx, ty };
      wasDragged = false;
      zoomWasActive = scale > 1;
    }

    if (zoomPointers.size === 2) {
      const [a, b] = [...zoomPointers.values()];
      pinchStartDist = Math.hypot(a.x - b.x, a.y - b.y);
      pinchStartScale = scale;
      pinchStartTx = tx;
      pinchStartTy = ty;
      pinchMid = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
      dragStart = null;
    }

    e.preventDefault();
  });

  modalImg.addEventListener("pointermove", (e) => {
    if (!zoomPointers.has(e.pointerId)) return;

    zoomPointers.set(e.pointerId, { x: e.clientX, y: e.clientY });

    // One active finger/mouse — panning on a zoomed image
    if (zoomPointers.size === 1 && dragStart && zoomWasActive) {
      const dx = e.clientX - dragStart.x;
      const dy = e.clientY - dragStart.y;

      if (Math.abs(dx) + Math.abs(dy) > 2) wasDragged = true;

      tx = dragStart.tx + dx;
      ty = dragStart.ty + dy;

      clampPan();
      applyZoom();
      return;
    }

    // Two fingers — pinch-zoom to the gesture middle + pan
    if (zoomPointers.size === 2 && pinchStartDist > 0) {
      const [a, b] = [...zoomPointers.values()];
      const dist = Math.hypot(a.x - b.x, a.y - b.y);
      const mid = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };

      scale = clampZoomValue(pinchStartScale * (dist / pinchStartDist));
      tx = pinchStartTx + (mid.x - pinchMid.x);
      ty = pinchStartTy + (mid.y - pinchMid.y);

      if (scale > 1) {
        zoomWasActive = true;
      }

      clampPan();
      applyZoom();
    }
  });

  modalImg.addEventListener("pointerup", (e) => {
    zoomPointers.delete(e.pointerId);
    modalImg.style.transition = "";
    dragStart = null;
  });

  modalImg.addEventListener("pointercancel", (e) => {
    zoomPointers.delete(e.pointerId);
    modalImg.style.transition = "";
    dragStart = null;
  });

  // Double click / double tap — reset to original

  modalImg.addEventListener("dblclick", (e) => {
    toggleZoom(e.clientX, e.clientY);
  });

  // =========================
  // TOUCH / SWIPE
  // =========================

  let startX = 0;
  let startY = 0;

  // for double tap on mobile
  let lastTap = { t: 0, x: 0, y: 0 };

  modal.addEventListener(
    "touchstart",
    function (e) {
      startX = e.touches[0].clientX;
      startY = e.touches[0].clientY;
    },
    { passive: true },
  );

  modal.addEventListener(
    "touchend",
    function (e) {
      const now = Date.now();
      const tapX = e.changedTouches[0].clientX;
      const tapY = e.changedTouches[0].clientY;

      // Double tap on photo — zoom in / restore original size
      if (
        now - lastTap.t < 300 &&
        Math.abs(tapX - lastTap.x) < 25 &&
        Math.abs(tapY - lastTap.y) < 25
      ) {
        toggleZoom(tapX, tapY);
        lastTap = { t: 0, x: 0, y: 0 };
        return;
      }

      lastTap = { t: now, x: tapX, y: tapY };

      // When zoomed, swipe is panning, not paging/closing
      if (scale > 1) return;

      const endX = e.changedTouches[0].clientX;
      const endY = e.changedTouches[0].clientY;

      const diffX = endX - startX;
      const diffY = endY - startY;

      // Horizontal swipe

      if (Math.abs(diffX) > Math.abs(diffY)) {
        if (Math.abs(diffX) > 50) {
          if (diffX > 0) {
            showModal((currentIndex - 1 + images.length) % images.length);
          } else {
            showModal((currentIndex + 1) % images.length);
          }
        }
      }

      // Swipe down → close
      else {
        if (diffY > 80) {
          closeModal();
        }
      }
    },
    { passive: true },
  );

  // Initial state

  currentIndex = 0;
});

// Post share script
// post.html
const btn = document.getElementById("shareBtn");

if (btn) {
  btn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);

      const text = btn.querySelector(".share-text");
      const icon = btn.querySelector(".share-icon");

      text.textContent = "Copied";
      icon.textContent = "✔";

      setTimeout(() => {
        text.textContent = text.dataset.default;
        icon.textContent = icon.dataset.default;
      }, 1500);
    } catch (err) {
      console.error(err);
    }
  });
}

// Compare breeds
// post.html
document.addEventListener("DOMContentLoaded", () => {
  const panel = document.getElementById("comparePanel");
  const selectA = document.getElementById("breedA");
  const selectB = document.getElementById("breedB");
  const wrapper = document.getElementById("compareTableWrapper");
  const customSelect = document.getElementById("breedBCustom");
  const trigger = document.getElementById("breedBTrigger");
  const list = document.getElementById("breedBList");
  const triggerImg = document.getElementById("breedBTriggerImg");
  const triggerText = document.getElementById("breedBTriggerText");

  if (!selectA || !selectB || !wrapper) return;

  let breedA = null;
  let breedB = null;

  // Custom select with photos
  if (trigger && list && triggerText) {
    const placeholderText = triggerText.textContent;

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

    list.addEventListener("click", (e) => {
      const item = e.target.closest(".custom-select-item");
      if (!item) return;
      selectB.value = item.dataset.value;
      closeList();
      selectB.dispatchEvent(new Event("change", { bubbles: true }));
    });

    document.addEventListener("click", (e) => {
      if (customSelect && !e.target.closest("#breedBCustom")) {
        closeList();
      }
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && list && !list.hidden) closeList();
    });

    // reset the trigger
    window.__resetBreedB = function () {
      selectB.value = "";
      triggerImg.hidden = true;
      triggerImg.removeAttribute("src");
      triggerText.textContent = placeholderText;
    };
  }

  async function loadBreed(id) {
    const lang = document.documentElement.lang || "en";
    const prefix = lang === "en" ? "" : `/${lang}`;
    const res = await fetch(`${prefix}/api/breed/${id}/`);
    return await res.json();
  }

  function row(icon, label) {
    return `
        <tr class="value-row">
            <td class="param-name">
                <span class="param-title">
                    <span class="param-icon">${icon}</span>
                    ${label}
                </span>
            </td>
            <td class="value-a">-</td>
            <td class="value-b">-</td>
        </tr>
    `;
  }

  function createTable() {
    wrapper.innerHTML = `
            <div class="compare-table-header">
                <button id="compareCloseBtn"
                        class="compare-close-btn">
                    <svg width="15" height="15" viewBox="0 0 15 15"
                         fill="none" aria-hidden="true">
                        <path d="M1.5 1.5 L13.5 13.5 M13.5 1.5 L1.5 13.5"
                              stroke="currentColor" stroke-width="1.1"
                              stroke-linecap="round"/>
                    </svg>
                </button>
            </div>

            <table class="compare-table">

                <tr class="header-row">

    <th class="parameter-header"></th>

    <th>
        <div class="compare-breed-head">

            <div class="compare-breed-info">

                <a class="compare-breed-link breed-a-link"></a>

            </div>

        </div>
    </th>

    <th>
        <div class="compare-breed-head">

            <div class="compare-breed-info">

                <a class="compare-breed-link breed-b-link"></a>

            </div>

        </div>
    </th>

</tr>

                ${row("🧬", wrapper.dataset.i18nVarieties || "Varieties")}
                ${row("🌍", wrapper.dataset.i18nOrigin || "Origin")}
                ${row("🐕", wrapper.dataset.i18nSize || "Size")}
                ${row("📏", wrapper.dataset.i18nHeightWeight || "Height / Weight")}
                ${row("🐩", wrapper.dataset.i18nCoat || "Coat")}
                ${row("❤️", wrapper.dataset.i18nLife || "Life expectancy")}
                ${row("💡", wrapper.dataset.i18nTrainability || "Trainability")}
                ${row("🚀", wrapper.dataset.i18nActivity || "Activity")}
                ${row("📢", wrapper.dataset.i18nBarking || "Barking")}
                ${row("🌱", wrapper.dataset.i18nAllergy || "Allergy-Friendly")}
                ${row("🏡", wrapper.dataset.i18nFamily || "Family friendly")}

            </table>
        `;

    document.getElementById("compareCloseBtn").addEventListener("click", () => {
      wrapper.classList.add("is-changing");

      setTimeout(() => {
        wrapper.innerHTML = "";
        if (window.__resetBreedB) window.__resetBreedB();
      }, 180);
    });
  }

  function updateTable() {
    wrapper.classList.add("is-changing");

    setTimeout(() => {
      // HEADER

      document.querySelector(".breed-a-link").textContent = breedA.title;

      document.querySelector(".breed-a-link").href = breedA.url;

      document.querySelector(".breed-b-link").textContent = breedB.title;

      document.querySelector(".breed-b-link").href = breedB.url;

      // Select TRIGGER: photo + name of the chosen breed

      triggerImg.src = breedB.photo;
      triggerImg.alt = breedB.title;
      triggerImg.hidden = false;
      triggerText.textContent = breedB.title;

      // VALUES

      const rows = document.querySelectorAll(".value-row");

      const values = [
        [breedA.varieties, breedB.varieties],

        [breedA.country, breedB.country],

        [breedA.size, breedB.size],

        [
          `${breedA.height || "-"} cm / ${breedA.weight || "-"} kg`,
          `${breedB.height || "-"} cm / ${breedB.weight || "-"} kg`,
        ],
        [
          `${(breedA.coat_length || "").replaceAll(",", "/")}${
            breedA.coat_length && breedA.coat_type ? ", " : ""
          }${(breedA.coat_type || "").replaceAll(",", "/")}`.trim() || "-",

          `${(breedB.coat_length || "").replaceAll(",", "/")}${
            breedB.coat_length && breedB.coat_type ? ", " : ""
          }${(breedB.coat_type || "").replaceAll(",", "/")}`.trim() || "-",
        ],

        [
          `${breedA.life} ${wrapper.dataset.i18nYears || "years"}`,
          `${breedB.life} ${wrapper.dataset.i18nYears || "years"}`,
        ],

        [breedA.trainability, breedB.trainability],

        [breedA.activity, breedB.activity],

        [breedA.barking || "-", breedB.barking || "-"],

        [breedA.hypoallergenic || "-", breedB.hypoallergenic || "-"],

        [breedA.family_friendliness || "-", breedB.family_friendliness || "-"],
      ];

      rows.forEach((row, index) => {
        row.querySelector(".value-a").textContent = values[index][0];

        row.querySelector(".value-b").textContent = values[index][1];
      });

      wrapper.classList.remove("is-changing");
    }, 120);
  }

  selectB.addEventListener("change", async () => {
    const idA = selectA.dataset.id;
    const idB = selectB.value;

    if (!idA || !idB) {
      wrapper.classList.add("is-changing");

      setTimeout(() => {
        wrapper.innerHTML = "";
      }, 180);

      return;
    }

    if (!wrapper.querySelector(".compare-table")) {
      createTable();
    }

    const [a, b] = await Promise.all([loadBreed(idA), loadBreed(idB)]);

    breedA = a;
    breedB = b;

    updateTable();
  });
});

// Keyboard navigation (posts)
document.addEventListener("DOMContentLoaded", function () {
  document.addEventListener("keydown", function (event) {
    if (
      event.target.tagName === "INPUT" ||
      event.target.tagName === "TEXTAREA" ||
      event.target.tagName === "SELECT" ||
      event.target.isContentEditable
    ) {
      return;
    }

    if (event.key === "ArrowLeft") {
      const prev = document.querySelector(".post-media-prev");

      if (prev) {
        event.preventDefault();
        window.location.href = prev.href;
      }
    }

    if (event.key === "ArrowRight") {
      const next = document.querySelector(".post-media-next");

      if (next) {
        event.preventDefault();
        window.location.href = next.href;
      }
    }
  });
});

// Custom navigation selects (home: groups and breeds)
document.addEventListener("DOMContentLoaded", () => {
  function initNavSelect(cfg) {
    const custom = document.getElementById(cfg.customId);
    const trigger = document.getElementById(cfg.triggerId);
    const list = document.getElementById(cfg.listId);
    const select = document.getElementById(cfg.selectId);
    const triggerText = document.getElementById(cfg.triggerTextId);
    const triggerImg = cfg.triggerImgId
      ? document.getElementById(cfg.triggerImgId)
      : null;

    if (!custom || !trigger || !list || !select || !triggerText) return;

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

      if (triggerImg) {
        const img = item.querySelector(".custom-select-opt-img");
        if (img) {
          triggerImg.src = img.src;
          triggerImg.alt = span ? span.textContent.trim() : "";
          triggerImg.hidden = false;
        }
      }

      closeList();

      if (item.dataset.value) {
        window.location.href = item.dataset.value;
      }
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && list && !list.hidden) closeList();
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

  // Breeds: with photos, like in compare
  initNavSelect({
    customId: "breedCustom",
    triggerId: "breedTrigger",
    listId: "breedList",
    selectId: "breed-select-1",
    triggerTextId: "breedTriggerText",
    triggerImgId: "breedTriggerImg",
  });
});

// Cookie consent (custom banner).
// Nothing is loaded before consent: GTM (and with it Google Analytics)
// is injected ONLY after the visitor grants analytics consent.

(function () {
  const STORAGE_KEY = "woof_consent";
  const CONSENT_VERSION = 1;
  const GTM_ID = "GTM-NJCSC592";

  const banner = document.getElementById("cookie-banner");
  const editBtn = document.getElementById("cookie-edit");
  const layerFirst = document.getElementById("cookie-banner-first");
  const layerDetails = document.getElementById("cookie-banner-details");
  const acceptBtn = document.getElementById("cookie-accept-all");
  const declineBtn = document.getElementById("cookie-decline-all");
  const openDetailsBtn = document.getElementById("cookie-open-details");
  const saveBtn = document.getElementById("cookie-save");
  const backBtn = document.getElementById("cookie-back");
  const closeBtn = document.getElementById("cookie-close");
  const analyticsToggle = document.getElementById("cookie-analytics-toggle");

  function readConsent() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      const data = JSON.parse(raw);
      if (!data || data.v !== CONSENT_VERSION) return null;
      return data;
    } catch (e) {
      return null;
    }
  }

  function saveConsent(analytics) {
    const data = {
      v: CONSENT_VERSION,
      analytics: !!analytics,
      ts: Date.now(),
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    return data;
  }

  function gtmLoaded() {
    return !!document.querySelector("script[data-consent-gtm]");
  }

  function loadGTM(analyticsGranted) {
    if (gtmLoaded()) return;

    window.dataLayer = window.dataLayer || [];

    // Consent Mode v2 signals: Google tags must respect the choice.
    window.dataLayer.push({
      consent: "default",
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
      analytics_storage: analyticsGranted ? "granted" : "denied",
    });

    window.dataLayer.push({
      "gtm.start": new Date().getTime(),
      event: "gtm.js",
    });

    const s = document.createElement("script");
    s.async = true;
    s.dataset.consentGtm = "1";
    s.src = "https://www.googletagmanager.com/gtm.js?id=" + GTM_ID;
    document.head.appendChild(s);
  }

  function applyConsent(data) {
    if (data && data.analytics) loadGTM(true);
  }

  function showBanner() {
    if (!banner) return;
    layerFirst.hidden = false;
    layerDetails.hidden = true;
    banner.hidden = false;
  }

  function hideBanner() {
    if (banner) banner.hidden = true;
  }

  function showEditButton() {
    if (editBtn) editBtn.hidden = !readConsent();
  }

  function setToggleFromConsent() {
    if (!analyticsToggle) return;
    const data = readConsent();
    analyticsToggle.checked = data ? data.analytics : false;
  }

  function finish(analytics) {
    const data = saveConsent(analytics);
    applyConsent(data);
    hideBanner();
    showEditButton();
  }

  // Initial state
  const saved = readConsent();
  if (saved) {
    hideBanner();
    showEditButton();
    applyConsent(saved);
  } else {
    showBanner();
    showEditButton();
  }

  // Buttons
  if (acceptBtn) acceptBtn.addEventListener("click", () => finish(true));
  if (declineBtn) declineBtn.addEventListener("click", () => finish(false));

  if (openDetailsBtn) {
    openDetailsBtn.addEventListener("click", () => {
      setToggleFromConsent();
      layerFirst.hidden = true;
      layerDetails.hidden = false;
    });
  }

  if (backBtn) {
    backBtn.addEventListener("click", () => {
      layerDetails.hidden = true;
      layerFirst.hidden = false;
    });
  }

  // X button: closing the notice = declining analytics cookies.
  if (closeBtn) {
    closeBtn.addEventListener("click", () => finish(false));
  }

  if (saveBtn) {
    saveBtn.addEventListener("click", () =>
      finish(analyticsToggle ? analyticsToggle.checked : false),
    );
  }

  if (editBtn) {
    editBtn.addEventListener("click", () => {
      setToggleFromConsent();
      showBanner();
    });
  }

  // Button on the Cookie Policy page: reopen the same consent window
  const policyOpenBtn = document.getElementById("cookie-policy-open");
  if (policyOpenBtn) {
    policyOpenBtn.addEventListener("click", () => {
      setToggleFromConsent();
      showBanner();
    });
  }
})();
