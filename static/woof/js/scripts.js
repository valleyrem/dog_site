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


// Breed select navigation script
document.addEventListener('DOMContentLoaded', function () {

    const breedSelect =
        document.getElementById('breed-select-1');

    if (!breedSelect) return;

    function go(value) {

        if (value && value !== '') {
            window.location.href = value;
        }

    }

    breedSelect.addEventListener('change', function () {
        go(this.value);
    });

    breedSelect.addEventListener('pointerup', function () {

        setTimeout(() => {
            go(this.value);
        }, 50);

    });

});


// Dog slider

document.addEventListener('DOMContentLoaded', () => {

    const track = document.querySelector('.dog-slider-track');
    const items = [...document.querySelectorAll('.dog-card-link')];

    if (!track || !items.length) return;

    const prev = document.querySelector('.slider-prev');
    const next = document.querySelector('.slider-next');
    const currentPage = document.querySelector('.slider-current');
    const totalPages = document.querySelector('.slider-total');

    let page = 0;
    let holdInterval = null;


    function getPerPage() {
        if (window.innerWidth <= 767) return 1;
        if (window.innerWidth <= 853) return 2;
        if (window.innerWidth <= 1024) return 3;
        return 3;
    }


    function getPages() {
        return Math.ceil(items.length / getPerPage());
    }


    function update() {

        const perPage = getPerPage();

        page = Math.max(0, Math.min(page, getPages() - 1));

        const gap = parseFloat(getComputedStyle(track).gap) || 0;
        const itemWidth = items[0].getBoundingClientRect().width + gap;
        const shift = page * perPage * itemWidth;

        track.style.transform = `translateX(-${shift}px)`;

        currentPage.textContent = page + 1;
        totalPages.textContent = getPages();

        prev.classList.toggle('disabled', page === 0);
        next.classList.toggle('disabled', page >= getPages() - 1);


        const pagination = document.querySelector('.slider-pagination');
        const navigation = document.querySelector('.slider-nav');

        const hideControls =
            (window.innerWidth > 1024 && items.length <= 3) ||
            (window.innerWidth <= 768 && items.length <= 1);

        if (pagination) {
            pagination.style.display = hideControls ? 'none' : '';
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
    }


    function closeModal() {

        modal.classList.remove('active');

        document.documentElement.classList.remove('no-scroll');
        document.body.classList.remove('no-scroll');

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

    if (!selectA || !selectB || !wrapper) return;

    let breedA = null;
    let breedB = null;

    async function loadBreed(id) {
        const res = await fetch(`/api/breed/${id}/`);
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

            <img
                class="compare-breed-image breed-a-image"
                loading="lazy"
                decoding="async"
            >

            <div class="compare-breed-info">

                <a class="compare-breed-link breed-a-link"></a>

                <span class="breed-meta breed-a-meta"></span>

            </div>

        </div>
    </th>

    <th>
        <div class="compare-breed-head">

            <img
                class="compare-breed-image breed-b-image"
                loading="lazy"
                decoding="async"
            >

            <div class="compare-breed-info">

                <a class="compare-breed-link breed-b-link"></a>

                <span class="breed-meta breed-b-meta"></span>

            </div>

        </div>
    </th>

</tr>

                ${row("🧬", "Varieties")}
                ${row("🌍", "Origin")}
                ${row("🐕", "Size")}
                ${row("📏", "Height / Weight")}
                ${row("🐩", "Coat")}
                ${row("❤️", "Life expectancy")}
                ${row("💡", "Trainability")}
                ${row("🚀", "Activity")}
                ${row("📢", "Barking")}
                ${row("🌱", "Allergy-Friendly")}
                ${row("🏡", "Family friendly")}

            </table>
        `;

        document.getElementById("compareCloseBtn")
            .addEventListener("click", () => {

                wrapper.classList.add("is-changing");

                setTimeout(() => {
                    wrapper.innerHTML = "";
                    selectB.value = "";
                }, 180);
            });
    }

    function updateTable() {

        wrapper.classList.add("is-changing");

        setTimeout(() => {

            // HEADER

            document.querySelector(".breed-a-image").src =
                breedA.photo;

            document.querySelector(".breed-a-image").alt =
                breedA.title;

            document.querySelector(".breed-b-image").src =
                breedB.photo;

            document.querySelector(".breed-b-image").alt =
                breedB.title;

            document.querySelector(".breed-a-link").textContent =
                breedA.title;

            document.querySelector(".breed-a-link").href =
                breedA.url;

            document.querySelector(".breed-b-link").textContent =
                breedB.title;

            document.querySelector(".breed-b-link").href =
                breedB.url;

            document.querySelector(".breed-a-meta").innerHTML =
                `(${breedA.cat}${breedA.section ? `, ${breedA.section}` : ""})`;

            document.querySelector(".breed-b-meta").innerHTML =
                `(${breedB.cat}${breedB.section ? `, ${breedB.section}` : ""})`;

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
                    `${breedA.life} years`,
                    `${breedB.life} years`
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

