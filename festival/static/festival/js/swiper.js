var swiper = new Swiper('.swiper-container', {
	autoplay: {
	delay: 5000,
},
loop: true,

pagination: {
	el: '.swiper-pagination',
	// type: 'fraction',
},

navigation: {
	nextEl: '.swiper-button-next',
	prevEl: '.swiper-button-prev',
},
});