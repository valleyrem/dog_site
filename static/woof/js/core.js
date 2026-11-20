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
