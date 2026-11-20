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

    // the thumbnail's address travels on the <option>; the browser fetches
    // the picture only when the list is opened (loading="lazy")
    if (option.dataset.thumb) {
      const img = document.createElement("img");
      img.className = "custom-select-opt-img";
      img.src = option.dataset.thumb;
      img.alt = "";
      img.width = 34;
      img.height = 34;
      img.loading = "lazy";
      img.decoding = "async";
      item.appendChild(img);
    }

    const label = document.createElement("span");
    label.textContent = option.textContent.trim();
    item.appendChild(label);

    frag.appendChild(item);
  });

  list.appendChild(frag);
  initListSearch(list);
}

// A search line at the top of a long drop-down list: it narrows the items as
// the visitor types (accents and case ignored, a plural ending is forgiven)
function initListSearch(list) {
  if (
    !list ||
    !list.dataset.listSearch ||
    list.querySelector(".custom-select-search")
  )
    return;

  const norm = (text) =>
    (text || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/[^\p{L}\p{N}]+/gu, " ")
      .trim();

  const row = document.createElement("li");
  row.className = "custom-select-search";
  const input = document.createElement("input");
  input.type = "search";
  input.className = "custom-select-search__input";
  input.placeholder = list.dataset.listSearch;
  input.setAttribute("aria-label", list.dataset.listSearch);
  input.autocomplete = "off";
  row.appendChild(input);
  list.insertBefore(row, list.firstChild);

  const none = document.createElement("li");
  none.className = "custom-select-none";
  none.textContent = list.dataset.listEmpty || "";
  none.hidden = true;
  list.appendChild(none);

  // the search line stays at the top; only the breeds under it scroll, and
  // they end at its lower edge
  const scroller = document.createElement("div");
  scroller.className = "custom-select-scroll";
  list.classList.add("custom-select-list--search");
  [...list.querySelectorAll(".custom-select-item")].forEach((el) =>
    scroller.appendChild(el),
  );
  scroller.appendChild(none);
  list.appendChild(scroller);
  initListEndHint(scroller);

  const items = [...scroller.querySelectorAll(".custom-select-item")].map(
    (el) => ({
      el,
      text: norm(el.textContent),
    }),
  );

  const filter = () => {
    const tokens = norm(input.value).split(" ").filter(Boolean);
    let shown = 0;
    items.forEach((item) => {
      const ok = tokens.every(
        (t) =>
          item.text.includes(t) ||
          (t.length >= 5 && item.text.includes(t.slice(0, -1))),
      );
      item.el.hidden = !ok;
      if (ok) shown += 1;
    });
    none.hidden = shown > 0;
    scroller.scrollTop = 0;
    // a short list has nothing below it: switch the fade at the bottom off
    scroller.dispatchEvent(new Event("scroll"));
  };

  input.addEventListener("input", filter);
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      const first = items.find((item) => !item.el.hidden);
      if (first) first.el.click();
    }
  });

  // every opening starts with an empty line; a keyboard (not a phone) gets the cursor
  new MutationObserver(() => {
    if (list.hidden) return;
    input.value = "";
    filter();
    if (window.matchMedia("(hover: hover)").matches)
      input.focus({ preventScroll: true });
  }).observe(list, { attributes: true, attributeFilter: ["hidden"] });
}

// The comparison table of the dialog (breeds page and a breed page): a photo
// and name for every breed in the header, then one row for every parameter.
// The labels come from data-i18n-* of the container.
function renderCompareTable(container, breeds) {
  const d = container.dataset;
  const years = d.i18nYears || "years";
  const rows = [
    ["varieties", d.i18nVarieties, (b) => b.varieties],
    ["origin", d.i18nOrigin, (b) => b.country],
    ["size", d.i18nSize, (b) => b.size],
    ["height", d.i18nHeight, (b) => b.height],
    ["weight", d.i18nWeight, (b) => b.weight],
    ["cointype", d.i18nCoatType, (b) => b.coat_type],
    ["coatlen", d.i18nCoatLength, (b) => b.coat_length],
    ["life", d.i18nLife, (b) => (b.life ? `${b.life} ${years}` : "")],
    ["training", d.i18nTrainability, (b) => b.trainability],
    ["activity", d.i18nActivity, (b) => b.activity],
    ["barking", d.i18nBarking, (b) => b.barking],
    ["shedding", d.i18nAllergy, (b) => b.hypoallergenic],
    ["family", d.i18nFamily, (b) => b.family_friendliness],
  ];

  const cell = (tag, text) => {
    const c = document.createElement(tag);
    setWithSexMarks(c, text || "-");
    return c;
  };

  const table = document.createElement("table");
  table.className = "bc-table";

  const head = document.createElement("tr");
  head.appendChild(document.createElement("th"));
  breeds.forEach((b) => {
    // photo box and two-line name have a fixed size, so the header is
    // equally tall for every breed
    const th = document.createElement("th");
    const box = document.createElement("div");
    box.className = "bc-head";
    const pic = document.createElement("span");
    pic.className = "bc-head__photo";
    if (b.photo) {
      const img = document.createElement("img");
      img.src = b.photo;
      img.alt = "";
      img.loading = "lazy";
      pic.appendChild(img);
    }
    const a = document.createElement("a");
    a.href = b.url;
    a.textContent = b.title;
    box.append(pic, a);
    th.appendChild(box);
    head.appendChild(th);
  });
  table.appendChild(head);

  rows.forEach(([icon, label, get]) => {
    const tr = document.createElement("tr");
    const th = document.createElement("th");
    const mark = document.createElement("span");
    mark.className = `bc-param__icon pi pi--${icon}`;
    mark.setAttribute("aria-hidden", "true");
    const name = document.createElement("span");
    name.textContent = label;
    const wrap = document.createElement("span");
    wrap.className = "bc-param";
    wrap.append(mark, name);
    th.appendChild(wrap);
    tr.appendChild(th);
    breeds.forEach((b) => tr.appendChild(cell("td", get(b))));
    table.appendChild(tr);
  });

  container.replaceChildren(table);
}

// A dialog taller than the screen: the fade at its bottom (styles.css) goes
// away when the end is reached
function initDialogFade(dialog) {
  if (!dialog) return;
  const update = () => {
    const atEnd =
      dialog.scrollTop + dialog.clientHeight >= dialog.scrollHeight - 2;
    dialog.classList.toggle("is-at-end", atEnd);
  };
  dialog.addEventListener("scroll", update, { passive: true });
  new MutationObserver(update).observe(dialog, {
    childList: true,
    subtree: true,
  });
  new MutationObserver(update).observe(dialog, {
    attributes: true,
    attributeFilter: ["open"],
  });
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

// Gallery / modal
// post.html

document.addEventListener("DOMContentLoaded", function () {
  const mainImage = document.querySelector(".post-main-image .post-image");
  // The photos are the thumbnails of the media block, picked by structure:
  // asking "is it visible" gave a different count depending on when the
  // layout was ready.
  const galleryImages = Array.from(
    document.querySelectorAll(".post-thumb .gallery-image"),
  );

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
  // Warming up: a swap waits for the large file to arrive and decode, which
  // on a phone is the whole "delay" you feel. Fetching the neighbours in the
  // background — and the one under the finger a moment before it is needed —
  // makes a swipe or a thumbnail tap land almost immediately.
  const warmed = new Map();

  function warm(index) {
    const image = images[index];
    if (!image || warmed.has(image.src)) return;
    const pre = new Image();
    pre.decoding = "async";
    pre.src = image.src;
    warmed.set(image.src, pre);
    if (pre.decode) pre.decode().catch(function () {});
  }

  function warmNeighbours() {
    const count = images.length;
    if (count < 2) return;
    // the same wrap the swipe uses: from the first photo one step back
    // is the last one
    warm((currentIndex + 1) % count);
    warm((currentIndex - 1 + count) % count);
  }

  function setActiveThumb(index) {
    document.querySelectorAll(".post-thumb").forEach((thumb) => {
      thumb.classList.toggle(
        "is-active",
        parseInt(thumb.dataset.index, 10) === index,
      );
    });

    // a scrolling strip of thumbnails follows the active one; only the strip
    // moves, never the page
    const active = document.querySelector(".post-thumb.is-active");
    const strip = active && active.parentElement;
    if (strip) {
      const a = active.getBoundingClientRect();
      const b = strip.getBoundingClientRect();
      if (strip.scrollWidth > strip.clientWidth + 1) {
        strip.scrollLeft += a.left - b.left - (b.width - a.width) / 2;
      }
      if (strip.scrollHeight > strip.clientHeight + 1) {
        strip.scrollTop += a.top - b.top - (b.height - a.height) / 2;
      }
    }
    warmNeighbours();
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

  // "3 / 8" on the photo, so a visitor can see there are more of them
  const counter = document.createElement("span");
  counter.className = "post-photo-count";
  counter.setAttribute("aria-hidden", "true");
  function setCount(index) {
    counter.textContent = index + 1 + " / " + images.length;
  }
  if (images.length > 1 && mainImage.parentElement) {
    setCount(0);
    mainImage.parentElement.appendChild(counter);
  }

  updateArrows();

  document.querySelectorAll(".post-thumb").forEach((thumb) => {
    // touch or mouse down: a few hundred milliseconds before the click
    thumb.addEventListener("pointerdown", () => {
      warm(parseInt(thumb.dataset.index, 10));
    });

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
    // "instant": the photo is replaced in place, with no slide (used when the
    // modal closes, so nothing moves on a page that is already in view)
    const instant = direction === "instant";
    const image = images[currentIndex];

    // Card-strip switch: a copy of the current photo slides out to the
    // left while the new one slides in from the right (see .is-leaving
    // and .is-entering in the CSS). The new photo is preloaded first, so
    // the strip never shows an empty frame.
    // same photo as the one on screen — nothing to animate
    if (mainImage.getAttribute("src") === image.src) return;
    setCount(currentIndex);

    const swap = () => {
      if (instant) {
        mainImage.src = image.src;
        mainImage.dataset.author = image.author || "";
        const author = document.getElementById("post-photo-author");
        if (author) author.textContent = image.author || "";
        return;
      }

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

    // A warmed image is the same file and is already decoded, so its
    // decode() resolves at once and the swap happens right away.
    const preload = warmed.get(image.src) || new Image();
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

  // Once the page has settled, warm the first pair so the very first swipe
  // does not wait for the network.
  const onIdle = window.requestIdleCallback || ((fn) => setTimeout(fn, 1500));

  onIdle(warmNeighbours);

  // MODAL

  // The phone's Back button closes the modal instead of leaving the page: an
  // entry is pushed when the modal opens and taken off when it closes.
  let modalHistory = false;

  function showModal(index) {
    if (!modal.classList.contains("active") && !modalHistory) {
      history.pushState({ modal: true }, "");
      modalHistory = true;
    }

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

    if (modalHistory) {
      modalHistory = false;
      history.back();
    }

    document.documentElement.classList.remove("no-scroll");
    document.body.classList.remove("no-scroll");

    resetZoom();

    window.scrollTo({
      top: scrollY,
      behavior: "auto",
    });

    // the photo the modal stopped on becomes the one on the page and the
    // active thumbnail (a no-op when the modal ended on the same photo)
    updateMainImage("instant");
    setActiveThumb(currentIndex);
    updateArrows();
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
      warmNeighbours();
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

  window.addEventListener("popstate", function () {
    if (!modal.classList.contains("active")) return;
    modalHistory = false;
    closeModal();
  });

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
// post.html: the other breed is chosen in a select, the button opens the same
// dialog as on the breeds page
document.addEventListener("DOMContentLoaded", () => {
  const breedA = document.getElementById("breedA");
  const selectB = document.getElementById("breedB");
  const customSelect = document.getElementById("breedBCustom");
  const trigger = document.getElementById("breedBTrigger");
  const list = document.getElementById("breedBList");
  const triggerImg = document.getElementById("breedBTriggerImg");
  const triggerText = document.getElementById("breedBTriggerText");
  const openBtn = document.querySelector("[data-compare-open]");
  const dialog = document.querySelector("[data-bc-dialog]");
  const table = document.querySelector("[data-bc-table]");

  if (
    !breedA ||
    !selectB ||
    !trigger ||
    !list ||
    !triggerText ||
    !openBtn ||
    !dialog ||
    !table
  )
    return;

  const clearBtn = document.getElementById("breedBClear");
  const placeholder = triggerText.textContent;

  fillListFromSelect(list, selectB);
  initDialogFade(dialog);

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
    // the chosen breed, with its photo, stays in the select
    const thumb = item.querySelector(".custom-select-opt-img");
    if (triggerImg) {
      triggerImg.hidden = !thumb;
      if (thumb) triggerImg.src = thumb.src;
    }
    triggerText.textContent = item.textContent.trim();
    openBtn.disabled = !selectB.value;
    if (clearBtn) clearBtn.hidden = !selectB.value;
    customSelect.classList.toggle("has-value", !!selectB.value);
    closeList();
  });

  // the cross puts the select back to "Select breed"
  if (clearBtn) {
    clearBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      selectB.value = "";
      if (triggerImg) triggerImg.hidden = true;
      triggerText.textContent = placeholder;
      openBtn.disabled = true;
      clearBtn.hidden = true;
      customSelect.classList.remove("has-value");
      closeList();
    });
  }

  document.addEventListener("click", (e) => {
    if (customSelect && !e.target.closest("#breedBCustom")) closeList();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !list.hidden) closeList();
  });

  const lang = document.documentElement.lang || "en";
  const prefix = lang === "en" ? "" : `/${lang}`;
  const load = (id) =>
    fetch(`${prefix}/api/breed/${id}/`).then((r) => r.json());

  openBtn.addEventListener("click", () => {
    if (!selectB.value) return;
    table.replaceChildren();
    dialog.showModal();
    dialog.focus({ preventScroll: true });
    Promise.all([load(breedA.dataset.id), load(selectB.value)])
      .then((breeds) => renderCompareTable(table, breeds))
      .catch(() => dialog.close());
  });

  dialog
    .querySelector("[data-bc-close]")
    .addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (e) => {
    if (e.target === dialog) dialog.close();
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

// Cookie consent (custom banner).
// Nothing is loaded before consent: GTM (and with it Google Analytics)
// is injected ONLY after the visitor grants analytics consent.

(function () {
  const STORAGE_KEY = "woof_consent";
  const CONSENT_VERSION = 1;
  // Garante guidance: ask again after about six months.
  const CONSENT_MAX_AGE_MS = 183 * 24 * 60 * 60 * 1000;
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

  function readConsent(ignoreAge) {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      const data = JSON.parse(raw);
      if (!data || data.v !== CONSENT_VERSION) return null;
      if (!ignoreAge && !(Date.now() - data.ts < CONSENT_MAX_AGE_MS))
        return null;
      return data;
    } catch (e) {
      return null;
    }
  }

  function saveConsent(analytics) {
    const existing = readConsent(true);
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

// Breeds page: filters, search, comparison and the "Find my breed" quiz over
// the static card grid.
// Filters come in groups (size, coat, activity...): a group allows one choice
// and different groups add up. Everything is decided in the browser from the
// keys in each card's data-filters, so no request is needed to narrow the
// list. The state lives in the address (?filter=a,b&q=text), which makes a
// selection shareable and survives the back button.

document.addEventListener("DOMContentLoaded", () => {
  const bar = document.querySelector("[data-breeds-filters]");
  const grid = document.querySelector("[data-breeds-grid]");

  if (!bar || !grid) return;

  const emptyNote = document.querySelector("[data-breeds-empty]");
  const countNote = document.querySelector("[data-breeds-count]");
  const search = document.querySelector("[data-breeds-search]");
  const moreToggle = document.querySelector("[data-breeds-more-toggle]");
  const morePanel = document.querySelector("[data-breeds-more]");
  const resetBtns = [...document.querySelectorAll("[data-breeds-reset]")];
  const buttons = [...bar.querySelectorAll(".filter-btn")];
  const allBtn = buttons.find((b) => b.dataset.filter === "all");
  const filterBtns = buttons.filter((b) => b.dataset.filter !== "all");
  const selects = [...document.querySelectorAll("[data-breeds-select]")];
  const chosenBox = document.querySelector("[data-breeds-chosen]");

  // accents, case and punctuation do not matter: "Bichon Frise" is found by
  // "bichon-frise" and "Dogue de Bordeaux" by "dogue bordeaux"
  const norm = (text) =>
    (text || "")
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .toLowerCase()
      .replace(/[^\p{L}\p{N}]+/gu, " ")
      .trim();

  const items = [...grid.querySelectorAll(".dog-card-link")].map((el) => ({
    el,
    keys: new Set((el.dataset.filters || "").split(" ").filter(Boolean)),
    text: norm(el.dataset.search || el.title),
  }));

  // which group every key belongs to (buttons and drop-down options)
  const groupOfKey = {};
  filterBtns.forEach((b) => (groupOfKey[b.dataset.filter] = b.dataset.group));
  selects.forEach((sel) =>
    [...sel.options].forEach((o) => {
      if (o.value) groupOfKey[o.value] = sel.dataset.group;
      o.dataset.base = o.textContent;
    }),
  );

  // the drop-downs are the site's own custom selects; the <select> stays
  // hidden and keeps the value, the list only shows and sets it
  const customs = selects.map((sel) => {
    const box = sel.closest("[data-breeds-custom]");
    const list = box.querySelector("[data-breeds-list]");
    const trigger = box.querySelector(".custom-select-trigger");
    fillListFromSelect(list, sel);
    const close = () => {
      list.hidden = true;
      trigger.setAttribute("aria-expanded", "false");
    };
    trigger.addEventListener("click", (e) => {
      e.stopPropagation();
      const willOpen = list.hidden;
      customs.forEach((c) => c && c.close());
      list.hidden = !willOpen;
      trigger.setAttribute("aria-expanded", String(willOpen));
    });
    list.addEventListener("click", (e) => {
      const item = e.target.closest(".custom-select-item");
      if (!item || item.classList.contains("is-disabled")) return;
      sel.value = item.dataset.value;
      sel.dispatchEvent(new Event("change"));
      close();
    });
    return {
      sel,
      box,
      list,
      close,
      text: box.querySelector("[data-breeds-trigger-text]"),
    };
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest("[data-breeds-custom]"))
      customs.forEach((c) => c.close());
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") customs.forEach((c) => c.close());
  });

  // the shown value, the counts and the unavailable options follow the <select>
  function syncCustoms() {
    customs.forEach((c) => {
      const chosenOpt = c.sel.selectedOptions[0];
      c.text.textContent = c.sel.value
        ? chosenOpt.dataset.base
        : c.sel.options[0].textContent;
      c.box.classList.toggle("has-value", !!c.sel.value);
      c.list.querySelectorAll(".custom-select-item").forEach((li) => {
        const o = [...c.sel.options].find((x) => x.value === li.dataset.value);
        if (!o) return;
        let count = li.querySelector(".custom-select-count");
        if (!count) {
          count = document.createElement("span");
          count.className = "custom-select-count";
          li.appendChild(count);
        }
        count.textContent = o.textContent.slice(o.dataset.base.length).trim();
        li.classList.toggle("is-disabled", o.disabled);
        li.classList.toggle("is-selected", o.value === c.sel.value);
        li.setAttribute("aria-selected", String(o.value === c.sel.value));
      });
    });
  }

  // the name of every filter, for the line of chosen filters under the count
  const titleOfKey = {};
  filterBtns.forEach(
    (b) => (titleOfKey[b.dataset.filter] = b.childNodes[0].textContent.trim()),
  );
  selects.forEach((sel) =>
    [...sel.options].forEach((o) => {
      if (o.value) titleOfKey[o.value] = o.dataset.base;
    }),
  );

  let chosen = {}; // group -> key
  let tokens = [];
  let query = "";

  function fits(item, choice, skipGroup, extraKey) {
    for (const g in choice) {
      if (g !== skipGroup && !item.keys.has(choice[g])) return false;
    }
    if (extraKey && !item.keys.has(extraKey)) return false;
    // a word also matches without its last letter, so "таксы" finds "такса"
    // and "dachshunds" finds "dachshund"
    return tokens.every(
      (t) =>
        item.text.includes(t) ||
        (t.length >= 5 && item.text.includes(t.slice(0, -1))),
    );
  }

  // typo help: the closest breed names to what was typed
  const suggestBox = document.querySelector("[data-breeds-suggest]");

  function distance(a, b) {
    const prev = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) {
      let diag = prev[0];
      prev[0] = i;
      for (let j = 1; j <= b.length; j++) {
        const keep = prev[j];
        prev[j] = Math.min(
          prev[j] + 1,
          prev[j - 1] + 1,
          diag + (a[i - 1] === b[j - 1] ? 0 : 1),
        );
        diag = keep;
      }
    }
    return prev[b.length];
  }

  function suggest() {
    if (!suggestBox) return;
    suggestBox.textContent = "";
    const q = tokens.join(" ");
    if (q.length < 3) {
      suggestBox.hidden = true;
      return;
    }
    const allowed = q.length >= 7 ? 2 : 1;
    const found = [];
    items.forEach((item) => {
      let best = Infinity;
      (item.el.dataset.names || item.el.title).split("|").forEach((name) => {
        const n = norm(name);
        best = Math.min(best, distance(q, n));
        // one word of the query against one word of the name
        if (tokens.length === 1) {
          n.split(" ").forEach((w) => {
            if (w.length >= 3) best = Math.min(best, distance(q, w));
          });
        }
      });
      if (best > 0 && best <= allowed) found.push({ item, best });
    });
    found.sort((a, b) => a.best - b.best);
    const top = found.slice(0, 3);
    if (!top.length) {
      suggestBox.hidden = true;
      return;
    }
    suggestBox.append(suggestBox.dataset.label + " ");
    top.forEach(({ item }, i) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "breeds-suggest__btn";
      b.textContent = item.el.title;
      b.addEventListener("click", () => {
        if (search) search.value = item.el.title;
        setQuery(item.el.title);
        syncClear();
        apply();
      });
      suggestBox.append(b);
      if (i < top.length - 1) suggestBox.append(", ");
    });
    suggestBox.hidden = false;
  }

  function writeUrl() {
    const url = new URL(window.location.href);
    const keys = Object.values(chosen);
    if (keys.length) url.searchParams.set("filter", keys.join(","));
    else url.searchParams.delete("filter");
    if (query) url.searchParams.set("q", query);
    else url.searchParams.delete("q");
    try {
      history.replaceState(null, "", url);
    } catch (e) {
      /* the page works without the address */
    }
  }

  function apply(scroll) {
    let shown = 0;

    items.forEach((item) => {
      const visible = fits(item, chosen);
      item.el.hidden = !visible;
      if (visible) shown += 1;
    });

    // the number next to a button: what the list would be if it were chosen
    filterBtns.forEach((btn) => {
      const g = btn.dataset.group;
      const key = btn.dataset.filter;
      const on = chosen[g] === key;
      const n = items.filter((i) => fits(i, chosen, g, key)).length;
      const slot = btn.querySelector("[data-count]");
      if (slot) slot.textContent = n;
      btn.disabled = n === 0 && !on;
      btn.classList.toggle("is-active", on);
      btn.setAttribute("aria-pressed", String(on));
    });

    selects.forEach((sel) => {
      const g = sel.dataset.group;
      sel.value = chosen[g] || "";
      const clearBtn = sel
        .closest("[data-breeds-custom]")
        .querySelector("[data-breeds-select-clear]");
      if (clearBtn) clearBtn.hidden = !sel.value;
      [...sel.options].forEach((o) => {
        if (!o.value) return;
        const n = items.filter((i) => fits(i, chosen, g, o.value)).length;
        o.textContent = `${o.dataset.base} (${n})`;
        o.disabled = n === 0 && chosen[g] !== o.value;
      });
    });
    syncCustoms();

    const any = Object.keys(chosen).length > 0;
    if (allBtn) {
      allBtn.classList.toggle("is-active", !any);
      allBtn.setAttribute("aria-pressed", String(!any));
    }
    // the reset under the list (phones) only helps when the list is long
    resetBtns.forEach((b) => {
      const below = b.closest(".breeds-reset-bottom");
      b.hidden = (!any && !query) || (below && shown <= 8);
    });

    // chosen filters in one line, each with a cross to take it off
    if (chosenBox) {
      chosenBox.textContent = "";
      // the word in the search is a chip too, the first one
      if (query) {
        const shownWord =
          query.length > 24 ? query.slice(0, 24).trim() + "…" : query;
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "chosen-chip chosen-chip--query";
        chip.setAttribute("aria-label", query);
        chip.appendChild(document.createTextNode(`“${shownWord}”`));
        const cross = document.createElement("span");
        cross.setAttribute("aria-hidden", "true");
        cross.textContent = "×";
        chip.appendChild(cross);
        chip.addEventListener("click", () => {
          setQuery("");
          if (search) search.value = "";
          syncClear();
          apply(false);
        });
        chosenBox.appendChild(chip);
      }
      Object.keys(chosen).forEach((g) => {
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "chosen-chip";
        chip.setAttribute("aria-label", titleOfKey[chosen[g]]);
        chip.appendChild(document.createTextNode(titleOfKey[chosen[g]]));
        const cross = document.createElement("span");
        cross.setAttribute("aria-hidden", "true");
        cross.textContent = "×";
        chip.appendChild(cross);
        chip.addEventListener("click", () => {
          choose("", g, false);
          // the last chip is gone: the filters fold back
          if (
            !Object.keys(chosen).length &&
            morePanel &&
            moreToggle &&
            !morePanel.hidden
          ) {
            moreToggle.click();
          }
          // phones: back up to the search line
          if (
            !Object.keys(chosen).length &&
            window.matchMedia("(max-width: 767px)").matches
          ) {
            const top = document.querySelector(".breeds-search");
            if (top) {
              const margin =
                parseFloat(getComputedStyle(top).scrollMarginTop) || 0;
              window.scrollTo(
                0,
                Math.max(
                  0,
                  top.getBoundingClientRect().top + window.scrollY - margin,
                ),
              );
            }
          }
        });
        chosenBox.appendChild(chip);
      });
      chosenBox.hidden = !any && !query;
    }

    // screen readers hear the result, and an empty grid gets an explanation
    if (emptyNote) emptyNote.hidden = shown > 0;
    if (shown > 0 && suggestBox) suggestBox.hidden = true;
    else suggest();
    if (countNote && countNote.dataset.template) {
      countNote.textContent = countNote.dataset.template
        .replace("{shown}", shown)
        .replace("{total}", items.length);
    }

    writeUrl();

    // on phones the grid sits well below the buttons: glide to the line
    // "Showing ... breeds" just above it (never on load, only after a real
    // click)
    if (scroll && window.innerWidth <= 767) {
      const reduce = window.matchMedia(
        "(prefers-reduced-motion: reduce)",
      ).matches;
      (countNote || grid).scrollIntoView({
        behavior: reduce ? "auto" : "smooth",
        block: "start",
      });
    }
  }

  function choose(key, group, scroll) {
    if (key) chosen[group] = key;
    else delete chosen[group];
    apply(scroll);
  }

  function resetFilters() {
    chosen = {};
  }

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const g = btn.dataset.group;
      const key = btn.dataset.filter;
      // a second click on the active button clears its group
      const clears = chosen[g] === key;
      choose(clears ? "" : key, g, false);
    });
  });

  if (allBtn) {
    allBtn.addEventListener("click", () => {
      resetFilters();
      apply(false);
    });
  }

  selects.forEach((sel) =>
    sel.addEventListener("change", () =>
      choose(sel.value, sel.dataset.group, false),
    ),
  );

  // the cross next to a drop-down puts it back to "Any ..." without opening it
  document.querySelectorAll("[data-breeds-select-clear]").forEach((btn) =>
    btn.addEventListener("click", () => {
      const sel = btn
        .closest("[data-breeds-custom]")
        .querySelector("[data-breeds-select]");
      if (sel) choose("", sel.dataset.group, false);
    }),
  );

  resetBtns.forEach((btn) =>
    btn.addEventListener("click", () => {
      resetFilters();
      setQuery("");
      if (search) search.value = "";
      syncClear();
      apply(false);
      // reset also folds the filter panel back
      if (morePanel && moreToggle && !morePanel.hidden) moreToggle.click();
      // the reset under the list takes the visitor back to the top of the page
      if (btn.closest(".breeds-reset-bottom")) {
        const reduce = window.matchMedia(
          "(prefers-reduced-motion: reduce)",
        ).matches;
        window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
      }
    }),
  );

  if (moreToggle && morePanel) {
    moreToggle.addEventListener("click", () => {
      const open = morePanel.hidden;
      morePanel.hidden = !open;
      moreToggle.setAttribute("aria-expanded", String(open));
      moreToggle.textContent = open
        ? moreToggle.dataset.labelLess
        : moreToggle.dataset.labelMore;
    });
  }

  function setQuery(value) {
    query = value.trim();
    tokens = norm(query).split(" ").filter(Boolean);
  }

  const clear = document.querySelector("[data-breeds-search-clear]");
  // the cross shows only while there is something to clear
  function syncClear() {
    if (clear && search) clear.hidden = search.value.length === 0;
  }

  if (search) {
    search.addEventListener("input", () => {
      setQuery(search.value);
      apply(false);
      syncClear();
    });

    // on Enter (the search key of a phone keyboard) glide down to the results;
    // typing itself never moves the page
    search.addEventListener("keydown", (e) => {
      if (e.key !== "Enter") return;
      e.preventDefault();
      apply(true);
      search.blur();
    });

    if (clear) {
      clear.addEventListener("click", () => {
        search.value = "";
        setQuery("");
        apply(false);
        syncClear();
        search.focus();
      });
    }
  }

  // ---- comparison ----------------------------------------------------
  const MAX_COMPARE = 3;
  const picked = [];
  const cmpBar = document.querySelector("[data-bc-bar]");
  const cmpText = document.querySelector("[data-bc-text]");
  const cmpOpen = document.querySelector("[data-bc-open]");
  const cmpClear = document.querySelector("[data-bc-clear]");
  const cmpDialog = document.querySelector("[data-bc-dialog]");
  const cmpTable = document.querySelector("[data-bc-table]");
  const canDialog = typeof HTMLDialogElement === "function";

  function syncCompare() {
    items.forEach((item) => {
      const btn = item.el.querySelector(".bc-toggle");
      if (!btn) return;
      const on = picked.includes(item.el.dataset.id);
      btn.classList.toggle("is-on", on);
      btn.setAttribute("aria-pressed", String(on));
      btn.title = on ? grid.dataset.compareRemove : grid.dataset.compareAdd;
      if (!btn.firstChild) {
        // both labels sit in one grid cell, so the button keeps one size
        const add = document.createElement("span");
        add.className = "bc-toggle__add";
        add.textContent = "+ " + grid.dataset.compareLabel;
        const done = document.createElement("span");
        done.className = "bc-toggle__done";
        const mark = document.createElement("span");
        mark.className = "pi pi--check";
        mark.setAttribute("aria-hidden", "true");
        done.append(mark, " " + grid.dataset.compareAdded);
        btn.append(add, done);
      }
      btn.disabled = !on && picked.length >= MAX_COMPARE;
    });
    if (!cmpBar) return;
    cmpBar.hidden = picked.length === 0;
    document.body.classList.toggle("has-compare-bar", picked.length > 0);
    const base = cmpText.dataset.template.replace("{n}", picked.length);
    cmpText.textContent =
      picked.length < 2 ? `${base} · ${cmpText.dataset.hint}` : base;
    cmpOpen.disabled = picked.length < 2;
  }

  if (canDialog && cmpBar && cmpDialog && cmpTable) {
    initDialogFade(cmpDialog);
    items.forEach((item) => {
      const host = item.el.querySelector(".dog-card");
      if (!host) return;
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "bc-toggle";
      btn.addEventListener("click", (e) => {
        // the card is a link: the button must not open the breed
        e.preventDefault();
        e.stopPropagation();
        const id = item.el.dataset.id;
        const at = picked.indexOf(id);
        if (at >= 0) picked.splice(at, 1);
        else if (picked.length < MAX_COMPARE) picked.push(id);
        syncCompare();
      });
      host.appendChild(btn);
    });

    cmpClear.addEventListener("click", () => {
      picked.length = 0;
      syncCompare();
    });

    const lang = document.documentElement.lang || "en";
    const prefix = lang === "en" ? "" : `/${lang}`;

    async function showCompare() {
      const breeds = await Promise.all(
        picked.map((id) =>
          fetch(`${prefix}/api/breed/${id}/`).then((r) => r.json()),
        ),
      );
      renderCompareTable(cmpTable, breeds);
    }

    cmpOpen.addEventListener("click", () => {
      if (picked.length < 2) return;
      cmpTable.replaceChildren();
      cmpDialog.showModal();
      cmpDialog.focus({ preventScroll: true });
      showCompare().catch(() => cmpDialog.close());
    });
    cmpDialog
      .querySelector("[data-bc-close]")
      .addEventListener("click", () => cmpDialog.close());
    cmpDialog.addEventListener("click", (e) => {
      if (e.target === cmpDialog) cmpDialog.close();
    });
  }

  // ---- "Find my breed" -----------------------------------------------
  const quizOpen = document.querySelector("[data-breeds-quiz-open]");
  const quizDialog = document.querySelector("[data-quiz-dialog]");
  const quizForm = document.querySelector("[data-quiz-form]");
  const quizNone = document.querySelector("[data-quiz-none]");

  if (quizOpen && quizDialog && quizForm && canDialog) {
    quizOpen.addEventListener("click", () => {
      if (quizNone) quizNone.hidden = true;
      quizDialog.showModal();
      quizDialog.focus({ preventScroll: true });
    });
    quizDialog
      .querySelector("[data-quiz-close]")
      .addEventListener("click", () => quizDialog.close());
    quizDialog.addEventListener("click", (e) => {
      if (e.target === quizDialog) quizDialog.close();
    });
    // a breed page links here with ?quiz=1
    if (new URLSearchParams(location.search).has("quiz")) quizOpen.click();

    quizForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const answer = {};
      new FormData(quizForm).forEach((value) => {
        if (value && groupOfKey[value]) answer[groupOfKey[value]] = value;
      });
      // strict answers can leave nothing: say so instead of an empty page
      const left = items.filter((i) =>
        Object.values(answer).every((k) => i.keys.has(k)),
      );
      if (!left.length) {
        if (quizNone) quizNone.hidden = false;
        return;
      }
      chosen = answer;
      setQuery("");
      if (search) search.value = "";
      syncClear();
      quizDialog.close();
      apply(true);
    });
  } else if (quizOpen) {
    quizOpen.hidden = true;
  }

  // ---- start: take the state from the address -------------------------
  const params = new URLSearchParams(window.location.search);
  (params.get("filter") || "")
    .split(",")
    .filter((k) => groupOfKey[k])
    .forEach((k) => (chosen[groupOfKey[k]] = k));
  setQuery(params.get("q") || "");
  if (search) search.value = query;
  syncClear();
  apply(false);
  syncCompare();
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
      img.addEventListener(
        "load",
        function () {
          reveal(img);
        },
        { once: true },
      );
      img.addEventListener(
        "error",
        function () {
          reveal(img);
        },
        { once: true },
      );
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

// Photo-credit note: on phones and tablets (where the photos and the
// characteristics panel are stacked) it sits directly under the photos; on
// larger screens it stays under the whole media block. The same element is moved, never duplicated, so
// screen readers still meet the sentence once.
(function () {
  var rule = document.querySelector(".images-rule");
  var media = document.querySelector(".post-media");
  if (!rule || !media) return;

  var right = media.querySelector(".post-right");
  if (!right) return;

  var mq = window.matchMedia("(max-width: 1032px)");

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

// Guides: the contents list is built from the section titles already on the
// page, so it can never drift away from the text. Five entries first (four on
// a breed page), the rest behind the switch.
(function () {
  var nav = document.querySelector(".guide-toc");
  if (!nav) return;

  var list = nav.querySelector("[data-guide-toc-list]");
  var toggle = nav.querySelector("[data-guide-toc-toggle]");
  var heads = [].slice
    .call(
      document.querySelectorAll(
        ".post-container .section-title, .policy-container .section-title, #group-breeds",
      ),
    )
    .filter(function (head) {
      return !head.closest("[hidden]");
    });
  // legal pages (guide-toc--all) always list every section
  var limit = nav.classList.contains("guide-toc--all")
    ? Infinity
    : nav.classList.contains("guide-toc--short")
      ? 4
      : 5;

  if (!list || heads.length < 2) {
    nav.remove();
    return;
  }

  heads.forEach(function (head, index) {
    if (!head.id) head.id = "guide-section-" + (index + 1);
    var link = document.createElement("a");
    link.href = "#" + head.id;
    link.textContent = head.textContent.trim();
    list.appendChild(link);
  });

  if (heads.length <= limit) {
    nav.classList.remove("is-collapsed");
    return;
  }

  toggle.hidden = false;
  toggle.addEventListener("click", function () {
    var open = nav.classList.toggle("is-open");
    nav.classList.toggle("is-collapsed", !open);
    toggle.setAttribute("aria-expanded", String(open));
  });
})();

// Breed page: the strip of breeds seen earlier in this tab.
(function () {
  // Recently viewed: this tab only (sessionStorage), nothing is kept after
  // the tab is closed.
  var page = document.querySelector("[data-recent-url]");
  var block = document.getElementById("recent-block");
  var grid = document.getElementById("recent-grid");
  if (!page || !block || !grid) return;

  var KEY = "woof_recent_" + (document.documentElement.lang || "en");
  var here = {
    u: page.dataset.recentUrl,
    t: page.dataset.recentTitle,
    i: page.dataset.recentImg || "",
  };
  var seen = [];
  try {
    seen = JSON.parse(sessionStorage.getItem(KEY) || "[]");
    if (!Array.isArray(seen)) seen = [];
  } catch (err) {
    seen = [];
  }

  var others = seen.filter(function (item) {
    return item && item.u && item.u !== here.u;
  });

  try {
    sessionStorage.setItem(
      KEY,
      JSON.stringify([here].concat(others).slice(0, 9)),
    );
  } catch (err) {}

  // eight on a computer; the phone layout hides the last two in CSS
  others = others.slice(0, 8);
  if (!others.length) return;

  others.forEach(function (item) {
    var a = document.createElement("a");
    a.className = "recent-card";
    a.href = item.u;
    if (item.i) {
      var img = document.createElement("img");
      img.src = item.i;
      img.alt = "";
      img.loading = "lazy";
      img.decoding = "async";
      a.appendChild(img);
    }
    var name = document.createElement("span");
    name.textContent = item.t;
    a.appendChild(name);
    grid.appendChild(a);
  });

  block.hidden = false;
})();

// Breed page: "Find my breed" opens the quiz right here; the answers are then
// carried to the Breeds page as filters.
(function () {
  var open = document.querySelector("[data-post-quiz-open]");
  var dialog = document.querySelector("[data-quiz-dialog]");
  var form = document.querySelector("[data-quiz-form]");
  if (!open || !dialog || !form || !dialog.showModal) return;
  if (document.querySelector("[data-breeds-grid]")) return;

  open.addEventListener("click", function (e) {
    e.preventDefault();
    dialog.showModal();
    dialog.focus({ preventScroll: true });
  });
  dialog
    .querySelector("[data-quiz-close]")
    .addEventListener("click", function () {
      dialog.close();
    });
  dialog.addEventListener("click", function (e) {
    if (e.target === dialog) dialog.close();
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var keys = [];
    new FormData(form).forEach(function (value) {
      if (value) keys.push(value);
    });
    var target = dialog.dataset.quizTarget || "/breeds/";
    window.location.href = keys.length
      ? target +
        "?filter=" +
        encodeURIComponent(keys.join(",")).replace(/%2C/g, ",")
      : target;
  });
})();

// Breed page: the compare panel opens from a quiet button instead of sitting open
(function () {
  const toggle = document.querySelector("[data-compare-toggle]");
  const panel = document.getElementById("compare");
  if (!toggle || !panel) return;

  function setOpen(open) {
    panel.hidden = !open;
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.classList.toggle("is-open", open);
  }

  toggle.addEventListener("click", () => setOpen(panel.hidden));
  if (location.hash === "#compare") setOpen(true);
})();

// A link or #hash that points into a closed FAQ item opens it
(function () {
  function openFor(id) {
    var el = id && document.getElementById(id);
    var item = el && el.closest("details");
    if (item) item.open = true;
  }
  openFor(location.hash.slice(1));
  window.addEventListener("hashchange", function () {
    openFor(location.hash.slice(1));
  });
})();

// FAQ: opening one question closes the one that was open
(function () {
  var items = [].slice.call(
    document.querySelectorAll("details.post-faq__item"),
  );
  if (items.length < 2) return;

  items.forEach(function (item) {
    item.addEventListener("toggle", function () {
      if (!item.open) return;
      items.forEach(function (other) {
        if (other !== item) other.open = false;
      });
    });
  });
})();

// Group page: on phones the description is shortened to whole sentences (about
// 300 characters) with a switch for the rest. Cutting at a full stop instead of
// by lines leaves no ellipsis for the browser to draw over the text.
(function () {
  var box = document.querySelector(".group-intro");
  if (!box) return;

  var desc = box.querySelector("[data-group-intro-desc]");
  var toggle = box.querySelector("[data-group-intro-toggle]");
  if (!desc || !toggle) return;

  var LIMIT = 300;
  var phone = window.matchMedia("(max-width: 767px)");
  var full = desc.textContent.trim();
  var short = full;
  var rest = document.createElement("span");
  rest.className = "group-intro__rest";
  rest.hidden = true;
  desc.parentNode.insertBefore(rest, desc.nextSibling);

  var ends = [];
  full.replace(/[.!?…](?=\s|$)/g, function (m, at) {
    ends.push(at + 1);
    return m;
  });
  var fit = ends.filter(function (at) {
    return at <= LIMIT;
  });
  var cut = fit.length ? fit[fit.length - 1] : ends[0];
  if (cut && cut < full.length) short = full.slice(0, cut);
  var tail = full.slice(short.length).trim();

  // the visible part ends its paragraph and the rest is a paragraph of its own;
  // on a phone that second paragraph waits behind the button, elsewhere it is
  // simply shown
  function render() {
    var open = box.classList.contains("is-open");
    var split = short !== full;
    var cutOn = phone.matches && split;
    desc.textContent = split ? short : full;
    rest.textContent = split ? tail : "";
    rest.hidden = !split || (cutOn && !open);
    box.classList.toggle("is-cut", cutOn);
  }

  toggle.hidden = false;
  toggle.addEventListener("click", function () {
    var open = box.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(open));
    render();
  });

  render();
  if (phone.addEventListener) phone.addEventListener("change", render);
})();

// Groups page: on phones only the first paragraph is shown, the rest sits
// behind the same "Read in full" switch as on a group page.
(function () {
  var box = document.querySelector(".groups-intro");
  var toggle = box && box.querySelector("[data-groups-intro-toggle]");
  if (!toggle) return;

  toggle.addEventListener("click", function () {
    var open = box.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(open));
  });
})();

// Height and weight come as "♂ 68–72 cm, ♀ 63–68 cm": the two signs go into
// their own spans so the CSS can line them up with the digits.
function setWithSexMarks(el, text) {
  el.textContent = "";
  String(text)
    .split(/([♂♀])/)
    .forEach(function (part) {
      if (!part) return;
      if (part === "♂" || part === "♀") {
        var mark = document.createElement("span");
        mark.className =
          "sex-mark " + (part === "♂" ? "sex-mark--m" : "sex-mark--f");
        mark.textContent = part;
        el.appendChild(mark);
      } else {
        el.appendChild(document.createTextNode(part));
      }
    });
}

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
