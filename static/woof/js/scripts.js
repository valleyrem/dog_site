// Custom selects: the <option> list is rendered once by the server, and the
// visible list is built from it here — so the same 100+ breeds are not sent
// to the browser twice (and no thumbnails are fetched just for a dropdown).
// Touch screens show no scrollbar on a scrollable list until it is dragged
// (see the ::after fade in styles.css), so the hint has to be switched off
// as soon as the end of the list is reached.
function initListEndHint(list) {
  if (!list) return;

  const update = () => {
    if (!list.clientHeight) return; // still hidden — nothing to measure
    const atEnd = list.scrollTop + list.clientHeight >= list.scrollHeight - 2;
    list.classList.toggle("is-at-end", atEnd);
  };

  list.addEventListener("scroll", update, { passive: true });
  new MutationObserver(update).observe(list, {
    attributes: true,
    attributeFilter: ["hidden"],
  });
  update();
}

function fillListFromSelect(list, select) {
  if (!list || !select || list.children.length) return;

  initListEndHint(list);

  const frag = document.createDocumentFragment();

  Array.prototype.forEach.call(select.options, (option) => {
    if (!option.value) return;

    const item = document.createElement("li");
    item.className = "custom-select-item";
    item.setAttribute("role", "option");
    item.dataset.value = option.value;

    const label = document.createElement("span");
    label.textContent = option.textContent.trim();
    item.appendChild(label);

    frag.appendChild(item);
  });

  list.appendChild(frag);
}

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
  const nav = document.querySelector(".slider-nav");
  const dotsWrap = document.querySelector(".slider-dots");
  const pagination = document.querySelector(".slider-pagination");

  // Related / group-of-breeds blocks (post + category pages): on
  // tablets and desktops the slider turns into a grid with a "Show more"
  // button (4 columns on tablets, 5 on wide screens); phones keep the
  // arrows slider with swipe.
  const relatedBlock = track.closest(".related-block");
  const relatedPerRow = () => (window.innerWidth >= 1024 ? 5 : 4);
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
    if (window.innerWidth <= 912) return 2;
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

// Pause / play for the quotes marquee
// home.html
document.addEventListener("DOMContentLoaded", () => {
  const marquee = document.querySelector(".breed-marquee");
  const toggle = document.querySelector(".marquee-toggle");

  if (!marquee || !toggle) return;

  function setPaused(paused) {
    marquee.classList.toggle("is-paused", paused);
    toggle.setAttribute("aria-pressed", String(paused));

    const label = paused ? toggle.dataset.labelPlay : toggle.dataset.labelPause;

    if (label) {
      toggle.setAttribute("aria-label", label);
      toggle.setAttribute("title", label);
    }
  }

  toggle.addEventListener("click", () => {
    setPaused(!marquee.classList.contains("is-paused"));
  });
});

// Gallery / modal
// post.html

document.addEventListener("DOMContentLoaded", function () {
  const mainImage = document.querySelector(".post-main-image .post-image");
  // Only visible gallery images: the hidden .mini-gallery copy is skipped,
  // the thumbnails of the media block are used instead.
  const galleryImages = Array.from(
    document.querySelectorAll(".gallery-image"),
  ).filter((img) => img.offsetParent !== null);

  if (!mainImage) return;

  // the breed name lives in alt for screen readers; during a swap we clear
  // it so the loading frame never flashes the title as raw text
  const mainAlt = mainImage.alt;

  // IMAGES

  const images = [
    {
      src: mainImage.dataset.full || mainImage.src,
      author: mainImage.dataset.author || "",
    },
    ...galleryImages.map((img) => ({
      // thumbnails carry the large version in data-full
      src: img.dataset.full || img.src,
      author: img.dataset.author || "",
    })),
  ];

  let currentIndex = 0;
  let scrollY = 0;

  // Thumbnails (left column of the media block) switch the main photo.
  // Index 0 is the main photo, so the first thumbnail is 1.
  function setActiveThumb(index) {
    document.querySelectorAll(".post-thumb").forEach((thumb) => {
      thumb.classList.toggle(
        "is-active",
        parseInt(thumb.dataset.index, 10) === index,
      );
    });
    // dots under the photo
    document.querySelectorAll(".post-image-dot").forEach((dot, i) => {
      dot.classList.toggle("is-active", i === index);
    });
  }

  // Arrows stop at the ends: the first photo only offers "next", the last
  // only "prev" (no wrap-around). With a single photo both stay hidden.
  function updateArrows() {
    const prev = document.querySelector(".main-img-arrow.prev");
    const next = document.querySelector(".main-img-arrow.next");
    if (prev) prev.style.display = currentIndex === 0 ? "none" : "";
    if (next)
      next.style.display = currentIndex === images.length - 1 ? "none" : "";
  }

  updateArrows();

  document.querySelectorAll(".post-thumb").forEach((thumb) => {
    thumb.addEventListener("click", () => {
      const index = parseInt(thumb.dataset.index, 10);
      if (Number.isNaN(index) || !images[index]) return;
      // the photo already on screen: leave it be, no animation
      if (index === currentIndex) return;
      // an earlier thumbnail = going back, the animation mirrors
      const back = index < currentIndex;
      currentIndex = index;
      updateMainImage(back ? "back" : "forward");
      setActiveThumb(index);
      updateArrows();
    });
  });

  // The modal is optional: the thumbnails above work without it.
  const modal = document.getElementById("modal");

  if (!modal) return;

  const modalImg = document.getElementById("modal-img");
  const modalAuthor = document.getElementById("modal-author");

  const closeBtn = modal.querySelector(".close");
  const prevModalBtn = modal.querySelector(".modal-arrow.prev");
  const nextModalBtn = modal.querySelector(".modal-arrow.next");

  // MAIN IMAGE

  function updateMainImage(direction) {
    // forward: the strip moves left (new photo from the right);
    // back: mirrored — new photo from the left, old one exits right
    const back = direction === "back";
    const image = images[currentIndex];

    // Card-strip switch: a copy of the current photo slides out to the
    // left while the new one slides in from the right (see .is-leaving
    // and .is-entering in the CSS). The new photo is preloaded first, so
    // the strip never shows an empty frame.
    // same photo as the one on screen — nothing to animate
    if (mainImage.getAttribute("src") === image.src) return;

    const swap = () => {
      const viewport = mainImage.parentElement;

      const outgoing = mainImage.cloneNode(true);
      outgoing.removeAttribute("id");
      outgoing.classList.remove("is-entering", "is-entering-back");
      outgoing.classList.add(back ? "is-leaving-back" : "is-leaving");
      outgoing.addEventListener("animationend", () => outgoing.remove(), {
        once: true,
      });

      if (viewport) viewport.insertBefore(outgoing, mainImage);

      // clear the alt while the new photo decodes, then restore it — this
      // stops the breed name from flashing in the frame before the image
      // appears
      mainImage.alt = "";
      mainImage.src = image.src;
      mainImage.decode().then(
        () => {
          mainImage.alt = mainAlt;
        },
        () => {
          mainImage.alt = mainAlt;
        },
      );

      mainImage.classList.remove("is-entering", "is-entering-back");
      void mainImage.offsetWidth; // restart the animation
      mainImage.classList.add(back ? "is-entering-back" : "is-entering");

      // the credit changes together with the photo, never a moment
      // before it — otherwise the author name flashes over the old image
      mainImage.dataset.author = image.author || "";

      const postAuthor = document.getElementById("post-photo-author");

      if (postAuthor) {
        postAuthor.textContent = image.author || "";
      }
    };

    const preload = new Image();
    preload.src = image.src;
    // fully decode the new photo before swapping it in — otherwise the
    // <img> briefly shows its alt text while the browser decodes
    preload.decode().then(swap, swap);
  }

  mainImage.addEventListener("animationend", () => {
    mainImage.classList.remove("is-entering", "is-entering-back");
  });

  const prevMain = document.querySelector(".main-img-arrow.prev");

  const nextMain = document.querySelector(".main-img-arrow.next");

  prevMain?.addEventListener("click", function (e) {
    e.stopPropagation();
    if (currentIndex === 0) return;
    currentIndex -= 1;
    updateMainImage("back");
    setActiveThumb(currentIndex);
    updateArrows();
  });

  nextMain?.addEventListener("click", function (e) {
    e.stopPropagation();
    if (currentIndex === images.length - 1) return;
    currentIndex += 1;
    updateMainImage("forward");
    setActiveThumb(currentIndex);
    updateArrows();
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

  // Swipe the main photo (touch): left = next photo, right = previous.
  // The thumbnails, the small arrows and the modal arrows all keep working.
  const swipeViewport = mainImage.parentElement;
  let mainSwipe = null;
  let mainSwipeSuppress = 0;

  if (swipeViewport) {
    swipeViewport.addEventListener("pointerdown", (e) => {
      if (e.pointerType !== "touch") return;
      mainSwipe = { x: e.clientX, y: e.clientY };
      swipeViewport.setPointerCapture(e.pointerId);
    });

    swipeViewport.addEventListener("pointermove", (e) => {
      if (!mainSwipe) return;
      // only claim the gesture when it is clearly horizontal; a vertical
      // drag keeps scrolling the page (touch-action: pan-y in the CSS)
      if (
        Math.abs(e.clientX - mainSwipe.x) > Math.abs(e.clientY - mainSwipe.y)
      ) {
        e.preventDefault();
      }
    });

    const releaseMainSwipe = (e) => {
      if (!mainSwipe) return;
      const dx = e.clientX - mainSwipe.x;
      const dy = e.clientY - mainSwipe.y;
      mainSwipe = null;

      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
        mainSwipeSuppress = Date.now();
        currentIndex =
          (currentIndex + (dx < 0 ? 1 : -1) + images.length) % images.length;
        updateMainImage(dx < 0 ? "forward" : "back");
        setActiveThumb(currentIndex);
      }
    };

    swipeViewport.addEventListener("pointerup", releaseMainSwipe);
    swipeViewport.addEventListener("pointercancel", releaseMainSwipe);
  }

  // Main image → modal (thumbnails never open the modal; they only swap
  // the photo inside .post-main-image .post-image)

  mainImage.addEventListener("click", function () {
    // a swipe just happened — don't open the modal on the same gesture
    if (Date.now() - mainSwipeSuppress < 400) return;
    showModal(currentIndex);
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

// Copy-link icon on the breadcrumb row
// post.html
(() => {
  const btn = document.getElementById("shareBtn");
  if (!btn) return;

  const toast = btn.querySelector(".post-copy-toast");
  let timer = null;

  // Fallback for browsers without the async clipboard API
  const copyText = async (value) => {
    if (navigator.clipboard && window.isSecureContext) {
      try {
        await navigator.clipboard.writeText(value);
        return true;
      } catch (err) {
        console.error(err);
      }
    }
    const field = document.createElement("textarea");
    field.value = value;
    field.setAttribute("readonly", "");
    field.style.position = "fixed";
    field.style.top = "-1000px";
    document.body.appendChild(field);
    field.select();
    try {
      document.execCommand("copy");
    } catch (err) {
      console.error(err);
    }
    document.body.removeChild(field);
    return true;
  };

  const showCopied = () => {
    toast.textContent = btn.dataset.copied || "";
    btn.classList.add("is-copied");
    clearTimeout(timer);
    timer = setTimeout(() => btn.classList.remove("is-copied"), 1600);
  };

  const copyLink = () => {
    copyText(window.location.href)
      .then((ok) => {
        if (ok) showCopied();
      })
      .catch((err) => {
        console.error(err);
      });
  };

  // The button lives on the breadcrumb row now — it listens for itself
  btn.addEventListener("click", () => {
    const selection = window.getSelection();
    if (selection && selection.toString().trim().length) return;
    copyLink();
  });
})();

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

  // Custom select over the <select id="breedB"> options
  if (trigger && list && triggerText) {
    const placeholderText = triggerText.textContent;

    fillListFromSelect(list, selectB);

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
                ${row("↕️", wrapper.dataset.i18nHeight || "Height")}
                ${row("⚖️", wrapper.dataset.i18nWeight || "Weight")}
                ${row("🐩", wrapper.dataset.i18nCoatType || "Coat type")}
                ${row("🐩", wrapper.dataset.i18nCoatLength || "Coat length")}
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

        [breedA.height || "-", breedB.height || "-"],

        [breedA.weight || "-", breedB.weight || "-"],

        [breedA.coat_type || "-", breedB.coat_type || "-"],

        [breedA.coat_length || "-", breedB.coat_length || "-"],

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

    if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
      // When the photo modal is open, the arrows belong to the modal
      // (previous/next photo). Breed navigation must not hijack them.
      const imageModal = document.getElementById("modal");
      if (imageModal && imageModal.classList.contains("active")) {
        return;
      }
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
    const existing = readConsent();
    const data = {
      v: CONSENT_VERSION,
      // Stability of the ID across re-choices is intentional: Art. 7 GDPR
      // evidence works best as an event history under one consent ID.
      id: existing && existing.id ? existing.id : newConsentId(),
      analytics: !!analytics,
      ts: Date.now(),
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    return data;
  }

  function newConsentId() {
    if (window.crypto && typeof window.crypto.randomUUID === "function") {
      return window.crypto.randomUUID();
    }
    return (
      "c-" +
      Date.now().toString(36) +
      "-" +
      Math.random().toString(36).slice(2, 12)
    );
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

  function finish(analytics, action) {
    const data = saveConsent(analytics);
    applyConsent(data);
    hideBanner();
    showEditButton();
    updateConsentIdDisplay();
    reportConsent(action, analytics, data.id);
  }

  // Show the visitor's own consent ID on the Cookie Policy page.
  function updateConsentIdDisplay() {
    const line = document.getElementById("cookie-policy-consent-id");
    const code = document.getElementById("cookie-consent-id");
    if (!line || !code) return;
    const data = readConsent();
    if (data && data.id) {
      code.textContent = data.id;
      line.hidden = false;
    } else {
      line.hidden = true;
    }
  }

  // Consent decisions are reported to the site's Telegram chat. The payload
  // carries no cookies and no identifiers beyond the visitor's own consent
  // ID (Art. 7 GDPR evidence) — the decision, the analytics flag, the page
  // path and the notice version. Reporting must never break the banner.
  function reportConsent(action, analytics, consentId) {
    try {
      fetch("/consent-log/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: action,
          analytics: !!analytics,
          path: window.location.pathname,
          id: consentId || "",
          notice: CONSENT_VERSION,
        }),
        keepalive: true,
      }).catch(() => {});
    } catch (e) {
      /* ignore: reporting is best-effort */
    }
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
  updateConsentIdDisplay();

  // Buttons
  if (acceptBtn)
    acceptBtn.addEventListener("click", () => finish(true, "accepted_all"));
  if (declineBtn)
    declineBtn.addEventListener("click", () => finish(false, "declined"));

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

  // X button: on the very first visit (no choice stored yet) closing the
  // notice means declining analytics cookies — the refusal is recorded and
  // reported. When the banner was reopened to view or adjust preferences,
  // the X only dismisses it and must NOT overwrite the existing choice or
  // send a misleading report.
  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      if (readConsent()) {
        hideBanner();
      } else {
        finish(false, "closed");
      }
    });
  }

  if (saveBtn) {
    saveBtn.addEventListener("click", () =>
      finish(
        analyticsToggle ? analyticsToggle.checked : false,
        analyticsToggle && analyticsToggle.checked
          ? "saved_analytics"
          : "saved_necessary",
      ),
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
      doc.scrollHeight - window.innerHeight - (footer ? footer.offsetHeight : 0);
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

// Breeds page: filter buttons over the static card grid

document.addEventListener("DOMContentLoaded", () => {
  const filterBar = document.querySelector("[data-breeds-filter]");
  const grid = document.querySelector("[data-breeds-grid]");

  if (!filterBar || !grid) return;

  const buttons = [...filterBar.querySelectorAll(".filter-btn")];
  const cards = [...grid.querySelectorAll(".dog-card-link")];

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.filter;

      buttons.forEach((b) => b.classList.toggle("is-active", b === btn));

      cards.forEach((card) => {
        const keys = (card.dataset.filters || "").split(" ");
        card.hidden = !(key === "all" || keys.includes(key));
      });

      // on phones jump to the top of the filtered grid, like an anchor
      if (window.innerWidth <= 767) {
        grid.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });
});

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
        img.addEventListener("load", function () { reveal(card); }, { once: true });
        img.addEventListener("error", function () { reveal(card); }, { once: true });
      }
    });
  }

  document.addEventListener("DOMContentLoaded", function () { init(); });
})();

// Post photo and its thumbnails: the same short fade-in as the breed
// cards, so nothing is painted until the file has actually loaded.
// The gallery swap reuses the same <img> element and keeps the class, and
// the sliding clone copies it, so switching photos is unaffected.
(function () {
  var SELECTOR = ".post-image, .post-thumb-img";

  function reveal(img) {
    // next frame: if the file was already cached, the browser must paint
    // the transparent state first, otherwise there is nothing to fade from
    requestAnimationFrame(function () {
      img.classList.add("is-loaded");
    });
  }

  function init() {
    document.querySelectorAll(SELECTOR).forEach(function (img) {
      if (img.complete) {
        reveal(img);
        return;
      }
      img.addEventListener("load", function () { reveal(img); }, { once: true });
      img.addEventListener("error", function () { reveal(img); }, { once: true });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

// Photo-credit note: on phones and small tablets it sits directly under the
// photos, before the characteristics panel; on larger screens it stays under
// the whole media block. The same element is moved, never duplicated, so
// screen readers still meet the sentence once.
(function () {
  var rule = document.querySelector(".images-rule");
  var media = document.querySelector(".post-media");
  if (!rule || !media) return;

  var right = media.querySelector(".post-right");
  if (!right) return;

  var mq = window.matchMedia("(max-width: 767px)");

  function place() {
    if (mq.matches) {
      if (rule.parentNode !== media) media.insertBefore(rule, right);
    } else if (rule.previousElementSibling !== media) {
      media.parentNode.insertBefore(rule, media.nextSibling);
    }
  }

  place();

  if (mq.addEventListener) mq.addEventListener("change", place);
  else if (mq.addListener) mq.addListener(place); // older Safari
})();
