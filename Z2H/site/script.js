function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('show');
}

let slideIndex = 0;
let slideInterval;

showSlides(slideIndex);
startAutoSlide();

function moveSlide(n) {
    clearInterval(slideInterval); // Stop auto slide
    slideIndex += n;
    showSlides(slideIndex);
    startAutoSlide(); // Restart auto slide
}

function showSlides(n) {
    const slides = document.querySelectorAll('.carousel-images img');
    if (n >= slides.length) { slideIndex = 0; }
    if (n < 0) { slideIndex = slides.length - 1; }
    const offset = -slideIndex * 100;
    document.querySelector('.carousel-images').style.transform = `translateX(${offset}%)`;
}

function startAutoSlide() {
    slideInterval = setInterval(() => {
        moveSlide(1);
    }, 3000); // Change slide every 3 seconds
}
