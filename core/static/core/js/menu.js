const menuToggle = document.getElementById('menu-toggle');
const menuClose = document.getElementById('menu-close');

const mobileMenu = document.getElementById('mobile-menu');
const menuOverlay = document.getElementById('menu-overlay');


function openMenu() {

    mobileMenu.classList.add('open');

    menuOverlay.classList.add('open');
    document.body.classList.add('menu-open');

    menuToggle.setAttribute('aria-expanded', 'true');
}


function closeMenu() {

    mobileMenu.classList.remove('open');

    menuOverlay.classList.remove('open');
    document.body.classList.remove('menu-open');


    menuToggle.setAttribute('aria-expanded', 'false');
}


if (menuToggle) {

    menuToggle.addEventListener('click', openMenu);

}


if (menuClose) {

    menuClose.addEventListener('click', closeMenu);

}


if (menuOverlay) {

    menuOverlay.addEventListener('click', closeMenu);

}