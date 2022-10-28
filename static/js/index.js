const hb = document.querySelector('.header__hamburger');
const menu = document.querySelector('.header');
const body = document.querySelector('body');


hb.addEventListener('click', function () {
    menu.classList.toggle('active');
    body.classList.toggle('lock');

})

var swiperr = new Swiper(".mySwiperr", {
    zoom: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });
