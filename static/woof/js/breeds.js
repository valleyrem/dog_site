// Breeds page: filters, search, comparison and the "Find a breed for me" quiz over
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

  // ---- "Find a breed for me" -----------------------------------------------
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
