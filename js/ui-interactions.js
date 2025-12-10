// Show/hide back to top button based on scroll position
document.addEventListener("DOMContentLoaded", function () {
    const scrollTopButton = document.getElementById("scrollTopButton");

    if (scrollTopButton) {
        // Show button when scrolling down
        window.addEventListener("scroll", function () {
            if (window.pageYOffset > 300) {
                scrollTopButton.classList.remove("opacity-0", "invisible");
            } else {
                scrollTopButton.classList.add("opacity-0", "invisible");
            }
        });
    }
});