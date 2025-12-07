// Show/hide back to top button based on scroll position
document.addEventListener("DOMContentLoaded", function () {
const backToTopButton = document.getElementById("backToTop");

if (backToTopButton) {
    // Show button when scrolling down
    window.addEventListener("scroll", function () {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.remove("opacity-0", "invisible");
        } else {
            backToTopButton.classList.add("opacity-0", "invisible");
        }
    });
}
});