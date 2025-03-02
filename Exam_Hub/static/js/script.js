document.addEventListener("DOMContentLoaded", function() {
    // Smooth scroll for navigation links
    document.querySelectorAll("nav a").forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            if (this.getAttribute("href").startsWith("#")) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute("href"));
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // Contact section highlight on hover
    const contactSection = document.querySelector(".contact");
    contactSection.addEventListener("mouseenter", function() {
        contactSection.style.backgroundColor = "#b0e0e6";
    });

    contactSection.addEventListener("mouseleave", function() {
        contactSection.style.backgroundColor = "#d1ecf1";
    });
});


