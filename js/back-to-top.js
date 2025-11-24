// Show/hide back to top button based on scroll position
document.addEventListener("DOMContentLoaded", function () {
const backToTopButton = document.getElementById("backToTop");

// Show button when scrolling down
window.addEventListener("scroll", function () {
    if (window.pageYOffset > 300) {
    backToTopButton.classList.add("visible");
    } else {
    backToTopButton.classList.remove("visible");
    }
});
});