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
