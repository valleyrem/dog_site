// Burger menu

const burger = document.getElementById('burger-btn');

if (burger) {

    const icon = document.getElementById('burger-icon');
    const sidebar = document.querySelector('.sidebar-nav');
    const body = document.body;

    const listIcon = burger.dataset.listIcon;
    const closeIcon = burger.dataset.closeIcon;


    function closeMenu() {

        sidebar.classList.remove('active');
        body.classList.remove('sidebar-open');

        icon.src = listIcon;
        icon.alt = 'Menu';
    }


    burger.addEventListener('click', (e) => {

        e.stopPropagation();

        const isActive =
            sidebar.classList.toggle('active');

        body.classList.toggle('sidebar-open');

        icon.src = isActive ? closeIcon : listIcon;
        icon.alt = isActive ? 'Close menu' : 'Menu';

    });


    document.addEventListener('click', (e) => {

        if (
            sidebar &&
            !sidebar.contains(e.target) &&
            !burger.contains(e.target)
        ) {
            closeMenu();
        }

    });

}

// Scroll to top button

document.addEventListener('DOMContentLoaded', function () {

    const scrollBtn = document.getElementById('scroll-top-button');

    if (!scrollBtn) return;

    function toggleButton() {
        scrollBtn.classList.toggle('show', window.scrollY > 190);
    }

    window.addEventListener('scroll', toggleButton);

    scrollBtn.addEventListener('click', function () {

        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });

    });

    toggleButton();

});


// Dog slider

document.addEventListener('DOMContentLoaded', () => {

    const track = document.querySelector('.dog-slider-track');
    const items = [...document.querySelectorAll('.dog-card-link')];

    if (!track || !items.length) return;

    const prev = document.querySelector('.slider-prev');
    const next = document.querySelector('.slider-next');
    const dotsWrap = document.querySelector('.slider-dots');

    let page = 0;
    let holdInterval = null;


    function getPerPage() {
        if (window.innerWidth <= 767) return 1;
        if (window.innerWidth <= 853) return 2;
        if (window.innerWidth <= 1329) return 3;
        return 4;
    }


    function getPages() {
        return Math.ceil(items.length / getPerPage());
    }


    function renderDots() {

        // Точки пересоздаются, когда число страниц изменилось
        // (после изменения ширины окна или числа карточек).
        if (dotsWrap && dotsWrap.children.length !== getPages()) {
            dotsWrap.innerHTML = '';

            for (let i = 0; i < getPages(); i++) {
                const dot = document.createElement('button');
                dot.type = 'button';
                dot.className = 'slider-dot';
                dot.setAttribute('aria-label', `Page ${i + 1}`);
                dot.addEventListener('click', () => {
                    page = i;
                    update();
                });
                dotsWrap.appendChild(dot);
            }
        }
    }


    function updateDots() {

        if (!dotsWrap) return;

        [...dotsWrap.children].forEach((dot, i) => {
            dot.classList.toggle('is-active', i === page);
        });
    }


    function update() {

        const perPage = getPerPage();

        page = Math.max(0, Math.min(page, getPages() - 1));

        const gap = parseFloat(getComputedStyle(track).gap) || 0;
        const itemWidth = items[0].getBoundingClientRect().width + gap;
        const shift = page * perPage * itemWidth;

        track.style.transform = `translateX(-${shift}px)`;

        renderDots();
        updateDots();

        prev.classList.toggle('disabled', page === 0);
        next.classList.toggle('disabled', page >= getPages() - 1);


        const pagination = document.querySelector('.slider-pagination');
        const navigation = document.querySelector('.slider-nav');

        const hideControls =
            (window.innerWidth > 1329 && items.length <= 4) ||
            (window.innerWidth <= 767 && items.length <= 1) ||
            (window.innerWidth <= 853 && items.length <= 2) ||
            (window.innerWidth <= 1329 && items.length <= 3);

        if (pagination) {
            pagination.style.display = hideControls ? 'none' : '';
        }

        if (dotsWrap) {
            dotsWrap.style.display = hideControls ? 'none' : '';
        }

        if (navigation) {
            navigation.style.display = hideControls ? 'none' : '';
        }

    }


    function startHold(direction) {

        stopHold();

        holdInterval = setInterval(() => {

            const maxPage = getPages() - 1;

            if (direction === 'next' && page < maxPage) {
                page++;
                update();
            }

            if (direction === 'prev' && page > 0) {
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


    next.addEventListener('click', () => {

        if (holdInterval) return;

        if (page < getPages() - 1) {
            page++;
            update();
        }

    });


    prev.addEventListener('click', () => {

        if (holdInterval) return;

        if (page > 0) {
            page--;
            update();
        }

    });

    next.addEventListener('mousedown', () => startHold('next'));
    next.addEventListener('touchstart', () => startHold('next'), { passive: true });

    next.addEventListener('mouseup', stopHold);
    next.addEventListener('mouseleave', stopHold);
    next.addEventListener('touchend', stopHold);
    next.addEventListener('touchcancel', stopHold);

    prev.addEventListener('mousedown', () => startHold('prev'));
    prev.addEventListener('touchstart', () => startHold('prev'), { passive: true });

    prev.addEventListener('mouseup', stopHold);
    prev.addEventListener('mouseleave', stopHold);
    prev.addEventListener('touchend', stopHold);
    prev.addEventListener('touchcancel', stopHold);

    let resizeTimeout;

    window.addEventListener('resize', () => {

        clearTimeout(resizeTimeout);

        resizeTimeout = setTimeout(update, 100);

    });


    update();

});

// Explore groups slider script
document.addEventListener('DOMContentLoaded', function () {

    document.querySelectorAll('.group-item').forEach(group => {

        const list = group.querySelector('.group-dogs');
        const prev = group.querySelector('.group-arrow-left');
        const next = group.querySelector('.group-arrow-right');

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

            list.style.gridTemplateColumns =
                `repeat(${totalPages}, minmax(0, 1fr))`;

            list.style.gridTemplateRows =
                `repeat(${itemsPerPage}, auto)`;


            const offset = page * (100 / totalPages);

            list.style.transform =
                `translateX(-${offset}%)`;


            prev.disabled = page === 0;
            next.disabled = page === totalPages - 1;


            if (totalPages <= 1) {

                prev.style.visibility = 'hidden';
                next.style.visibility = 'hidden';

            } else {

                prev.style.visibility = 'visible';
                next.style.visibility = 'visible';

            }


            group.sliderTotalPages = totalPages;

            list.classList.remove('slider-loading');
        }


        prev.addEventListener('click', function () {

            if (page > 0) {

                page--;

                setupSlider();
            }

        });


        next.addEventListener('click', function () {

            if (page < group.sliderTotalPages - 1) {

                page++;

                setupSlider();
            }

        });


        window.addEventListener('resize', function () {

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
        block: "nearest"
    });

});

// Gallery / modal
// post.html

document.addEventListener('DOMContentLoaded', function () {

    const modal = document.getElementById('modal');

    if (!modal) return;

    const modalImg = document.getElementById('modal-img');
    const modalAuthor = document.getElementById('modal-author');

    const closeBtn = modal.querySelector('.close');
    const prevModalBtn = modal.querySelector('.modal-arrow.prev');
    const nextModalBtn = modal.querySelector('.modal-arrow.next');

    const mainImage = document.querySelector('.post-image');
    const galleryImages = Array.from(
        document.querySelectorAll('.gallery-image')
    );

    if (!mainImage) return;

    // IMAGES

    const images = [
        {
            src: mainImage.src,
            author: mainImage.dataset.author || ''
        },
        ...galleryImages.map(img => ({
            src: img.src,
            author: img.dataset.author || ''
        }))
    ];


    let currentIndex = 0;
    let scrollY = 0;

    // MAIN IMAGE

    function updateMainImage() {
    const image = images[currentIndex];

    mainImage.src = image.src;
    mainImage.dataset.author = image.author || '';

    const postAuthor =
        document.getElementById('post-photo-author');

    if (postAuthor) {
        postAuthor.textContent = image.author || '';
    }
}


    const prevMain =
        document.querySelector('.main-img-arrow.prev');

    const nextMain =
        document.querySelector('.main-img-arrow.next');


    prevMain?.addEventListener('click', function (e) {

        e.stopPropagation();

        currentIndex =
            (currentIndex - 1 + images.length) % images.length;

        updateMainImage();
    });


    nextMain?.addEventListener('click', function (e) {

        e.stopPropagation();

        currentIndex =
            (currentIndex + 1) % images.length;

        updateMainImage();
    });

    // MODAL

    function showModal(index) {

        currentIndex = index;

        const image = images[currentIndex];

        scrollY = window.scrollY;

        modal.classList.add('active');

        modalImg.src = image.src;
        modalAuthor.textContent = image.author || '';

        document.documentElement.classList.add('no-scroll');
        document.body.classList.add('no-scroll');

        resetZoom();
    }


    function closeModal() {

        modal.classList.remove('active');

        document.documentElement.classList.remove('no-scroll');
        document.body.classList.remove('no-scroll');

        resetZoom();

        window.scrollTo({
            top: scrollY,
            behavior: 'auto'
        });
    }


    // Main image → modal

    mainImage.addEventListener('click', function () {
        showModal(currentIndex);
    });


    // Gallery images → modal

    galleryImages.forEach(function (img, index) {

        img.addEventListener('click', function () {

            showModal(index + 1);

        });

    });


    // Modal arrows

    prevModalBtn?.addEventListener('click', function (e) {

        e.stopPropagation();

        showModal(
            (currentIndex - 1 + images.length) % images.length
        );
    });


    nextModalBtn?.addEventListener('click', function (e) {

        e.stopPropagation();

        showModal(
            (currentIndex + 1) % images.length
        );
    });


    // Close

    closeBtn?.addEventListener('click', closeModal);


    modal.addEventListener('click', function (e) {

        if (e.target === modal) {
            closeModal();
        }

    });


    // =========================
    // KEYBOARD
    // =========================

    document.addEventListener('keydown', function (e) {

        if (!modal.classList.contains('active')) return;

        if (e.key === 'ArrowLeft') {

            showModal(
                (currentIndex - 1 + images.length) % images.length
            );

        }

        if (e.key === 'ArrowRight') {

            showModal(
                (currentIndex + 1) % images.length
            );

        }

        if (e.key === 'Escape') {

            closeModal();

        }

    });


    // =========================
    // ZOOM: колесо мыши + перетаскивание + pinch
    // =========================

    const zoomLevelEl = document.getElementById('modal-zoom');

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
            zoomLevelEl.classList.toggle('show', zoomed);
        }

        // при увеличении стрелки навигации прячем,
        // чтобы не путать с панорамой
        modal.querySelectorAll('.modal-arrow').forEach(a => {
            a.style.opacity = zoomed ? '0' : '';
            a.style.pointerEvents = zoomed ? 'none' : '';
        });
    }

    function resetZoom() {

        scale = 1;
        tx = 0;
        ty = 0;

        modalImg.style.transform = '';
        modalImg.style.transition = '';

        if (zoomLevelEl) {
            zoomLevelEl.textContent = '100%';
            zoomLevelEl.classList.remove('show');
        }

        modal.querySelectorAll('.modal-arrow').forEach(a => {
            a.style.opacity = '';
            a.style.pointerEvents = '';
        });
    }

    // Колесо мыши — зум к точке под курсором

    modalImg.addEventListener('wheel', (e) => {

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

        modalImg.style.transition = 'none';
        clampPan();
        applyZoom();
        requestAnimationFrame(() => {
            modalImg.style.transition = '';
        });
    }, { passive: false });

    // Перетаскивание мышью / пальцем + pinch двумя пальцами

    modalImg.addEventListener('pointerdown', (e) => {

        zoomPointers.set(e.pointerId, { x: e.clientX, y: e.clientY });

        try {
            modalImg.setPointerCapture(e.pointerId);
        } catch (err) { /* ignore */ }

        modalImg.style.transition = 'none';

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

    modalImg.addEventListener('pointermove', (e) => {

        if (!zoomPointers.has(e.pointerId)) return;

        zoomPointers.set(e.pointerId, { x: e.clientX, y: e.clientY });

        // Один активный палец/мышь — панорама по увеличенной картинке
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

        // Два пальца — pinch-зум к середине жеста + перемещение
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

    modalImg.addEventListener('pointerup', (e) => {
        zoomPointers.delete(e.pointerId);
        modalImg.style.transition = '';
        dragStart = null;
    });

    modalImg.addEventListener('pointercancel', (e) => {
        zoomPointers.delete(e.pointerId);
        modalImg.style.transition = '';
        dragStart = null;
    });

    // Двойной клик / двойной тап — сброс до оригинала

    modalImg.addEventListener('dblclick', () => {
        resetZoom();
    });

    // =========================
    // TOUCH / SWIPE
    // =========================

    let startX = 0;
    let startY = 0;


    modal.addEventListener('touchstart', function (e) {

        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;

    }, { passive: true });


    modal.addEventListener('touchend', function (e) {

        const endX = e.changedTouches[0].clientX;
        const endY = e.changedTouches[0].clientY;

        const diffX = endX - startX;
        const diffY = endY - startY;


        // Horizontal swipe

        if (Math.abs(diffX) > Math.abs(diffY)) {

            if (Math.abs(diffX) > 50) {

                if (diffX > 0) {

                    showModal(
                        (currentIndex - 1 + images.length)
                        % images.length
                    );

                } else {

                    showModal(
                        (currentIndex + 1)
                        % images.length
                    );

                }

            }

        }

        // Swipe down → close

        else {

            if (diffY > 80) {
                closeModal();
            }

        }

    }, { passive: true });


    // Initial state

    currentIndex = 0;

});



// Post share script
// post.html
const btn = document.getElementById('shareBtn');

if (btn) {
    btn.addEventListener('click', async () => {
        try {
            await navigator.clipboard.writeText(window.location.href);

            const text = btn.querySelector('.share-text');
            const icon = btn.querySelector('.share-icon');

            text.textContent = 'Copied';
            icon.textContent = '✔';

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

    // Кастомный селект с фото
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

        // сброс триггера
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
                    ✕
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

        document.getElementById("compareCloseBtn")
            .addEventListener("click", () => {

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

            document.querySelector(".breed-a-link").textContent =
                breedA.title;

            document.querySelector(".breed-a-link").href =
                breedA.url;

            document.querySelector(".breed-b-link").textContent =
                breedB.title;

            document.querySelector(".breed-b-link").href =
                breedB.url;

            // TRIGGER селекта: фото + имя выбранной породы

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
                    `${breedB.height || "-"} cm / ${breedB.weight || "-"} kg`
                ],
                [
                    `${(breedA.coat_length || "").replaceAll(",", "/")}${
                        breedA.coat_length && breedA.coat_type ? ", " : ""
                    }${(breedA.coat_type || "").replaceAll(",", "/")}`.trim() || "-",

                    `${(breedB.coat_length || "").replaceAll(",", "/")}${
                        breedB.coat_length && breedB.coat_type ? ", " : ""
                    }${(breedB.coat_type || "").replaceAll(",", "/")}`.trim() || "-"
                ],

                [
                    `${breedA.life} ${wrapper.dataset.i18nYears || "years"}`,
                    `${breedB.life} ${wrapper.dataset.i18nYears || "years"}`
                ],

                [
                    breedA.trainability,
                    breedB.trainability
                ],

                [
                    breedA.activity,
                    breedB.activity
                ],

                [
                    breedA.barking || "-",
                    breedB.barking || "-"
                ],

                [
                    breedA.hypoallergenic || "-",
                    breedB.hypoallergenic || "-"
                ],

                [
                    breedA.family_friendliness || "-",
                    breedB.family_friendliness || "-"
                ]
            ];

            rows.forEach((row, index) => {

                row.querySelector(".value-a").textContent =
                    values[index][0];

                row.querySelector(".value-b").textContent =
                    values[index][1];
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

        const [a, b] = await Promise.all([
            loadBreed(idA),
            loadBreed(idB)
        ]);

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

// Кастомные навигационные селекты (home: группы и породы)
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

        // Клик в любом месте вне кастомного селекта закрывает все открытые списки.
        // capture-фаза нужна: стоп-пропагация на триггере не мешает перехвату,
        // и клик по другому триггеру тоже гасит остальные дропдауны.
        document.addEventListener("click", (e) => {
            const customEl = e.target.closest(".custom-select");
            document.querySelectorAll(".custom-select-list").forEach((openList) => {
                if (openList.hidden) return;
                if (customEl && customEl.contains(openList)) return;
                openList.hidden = true;
                const openTrigger = openList.parentElement.querySelector(".custom-select-trigger");
                if (openTrigger) openTrigger.setAttribute("aria-expanded", "false");
            });
        }, true);

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

    // Группы: текстом, без фото
    initNavSelect({
        customId: "groupCustom",
        triggerId: "groupTrigger",
        listId: "groupList",
        selectId: "breed-select",
        triggerTextId: "groupTriggerText"
    });

    // Породы: с фото, как в compare
    initNavSelect({
        customId: "breedCustom",
        triggerId: "breedTrigger",
        listId: "breedList",
        selectId: "breed-select-1",
        triggerTextId: "breedTriggerText",
        triggerImgId: "breedTriggerImg"
    });
});
