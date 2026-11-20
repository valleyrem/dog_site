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
    modalImg.alt = image.alt || "";
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

// Copy-link icon: on the breadcrumb row, on phones next to the dates
// post.html
(() => {
  const btn = document.getElementById("shareBtn");
  if (!btn) return;

  const toast = btn.querySelector(".post-copy-toast");
  let timer = null;

  // On phones the button sits in the row with the dates instead of the crumbs
  const crumbs = btn.parentElement;
  const dates = document.querySelector(".post-container .page-dates");
  if (dates) {
    const phone = window.matchMedia("(max-width: 767px)");
    const place = () => (phone.matches ? dates : crumbs).appendChild(btn);
    place();
    phone.addEventListener("change", place);
  }

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

// Breed page: "Find a breed for me" opens the quiz right here; the answers are then
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
