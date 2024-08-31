// Скрипт для закрытия меню при клике вне его
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

// Скрипт для применения и переключения темы
document.addEventListener("DOMContentLoaded", function() {
    // При начальной загрузке добавить класс темы из localStorage
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.body.classList.add(currentTheme + '-theme');

    // Удалить класс .hidden после применения темы
    document.body.classList.remove('hidden');

    // Переключение темы по нажатию кнопки
    document.querySelector('#theme-toggle').addEventListener('click', function() {
        let newTheme = document.body.classList.contains('light-theme') ? 'dark' : 'light';
        document.body.classList.remove('light-theme', 'dark-theme');
        document.body.classList.add(newTheme + '-theme');
        localStorage.setItem('theme', newTheme);
    });
});

// Скрыть контент до применения темы
document.body.classList.add('hidden');

// Скрипт для кнопки "Прокрутить наверх"
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
