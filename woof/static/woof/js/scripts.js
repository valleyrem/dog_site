document.addEventListener('click', function(event) {
    const menuToggle = document.querySelector('#menu__toggle');
    const menuBox = document.querySelector('.menu__box');
    const menuButton = document.querySelector('.menu__btn');

    if (!menuBox.contains(event.target) && 
        !menuToggle.contains(event.target) && 
        !menuButton.contains(event.target)) {
        menuToggle.checked = false;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const scrollToTopBtn = document.getElementById('scroll-to-top');
    let lastScrollTop = window.pageYOffset;

    if (scrollToTopBtn) {
        scrollToTopBtn.style.display = 'none';

        window.addEventListener('scroll', function() {
            const currentScroll = window.pageYOffset;

            if (currentScroll > 600) {
                scrollToTopBtn.style.display = 'block';
            } else {
                scrollToTopBtn.style.display = 'none';
            }

            lastScrollTop = currentScroll;
        });

        scrollToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});

document.getElementById('breed-search').addEventListener('change', function() {
            const selectedValue = this.value;
            if (selectedValue) {
                window.location.href = selectedValue;
            }
        });
