// Ensure DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    console.log("Online Exam Portal Loaded Successfully!");

    // About Page
    console.log("About page loaded successfully!");

    // Features Page
    console.log("Features page loaded successfully!");

    // Smooth Scrolling for Navigation Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            document.getElementById(targetId)?.scrollIntoView({ behavior: "smooth" });
        });
    });

    // Auto-slideshow for Features Section
    let featureIndex = 0;
    function showNextFeature() {
        let features = document.querySelectorAll(".feature");
        features.forEach((f, i) => f.style.display = i === featureIndex ? "block" : "none");
        featureIndex = (featureIndex + 1) % features.length;
    }
    if (document.querySelector(".feature")) {
        showNextFeature();
        setInterval(showNextFeature, 3000);
    }

    // Contact Form Submission
    const contactForm = document.getElementById("contact-form");
    if (contactForm) {
        contactForm.addEventListener("submit", function (event) {
            event.preventDefault();
            alert("Thank you for reaching out! We will get back to you soon.");
            this.reset();
        });
    }

    // Student Login Form Validation
    const studentLoginForm = document.getElementById("student-login-form");
    if (studentLoginForm) {
        studentLoginForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            if (!email || !password) {
                alert("Please enter both email and password.");
                return;
            }

            alert("Login successful! Redirecting to student dashboard...");
            window.location.href = "student-dashboard.html"; // Redirect after login
        });
    }

    // Student Signup Form Validation
    const studentSignupForm = document.getElementById("student-signup-form");
    if (studentSignupForm) {
        studentSignupForm.addEventListener("submit", function (event) {
            event.preventDefault();
            
            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;
            const confirmPassword = document.getElementById("confirm-password").value;

            if (!name || !email || !password || !confirmPassword) {
                alert("Please fill in all fields.");
                return;
            }

            if (password !== confirmPassword) {
                alert("Passwords do not match.");
                return;
            }

            alert("Signup successful! Redirecting to login page...");
            window.location.href = "student-login.html"; // Redirect to login
        });
    }

    // Teacher Login Form Validation
    const teacherLoginForm = document.getElementById("teacher-login-form");
    if (teacherLoginForm) {
        teacherLoginForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            if (email && password) {
                alert("Login successful! Redirecting...");
                window.location.href = "teacher-portal.html"; // Redirect to teacher dashboard
            } else {
                alert("Please fill in all fields.");
            }
        });
    }

    // Teacher Signup Form Validation
    const teacherSignupForm = document.getElementById("teacher-signup-form");
    if (teacherSignupForm) {
        teacherSignupForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;
            const confirmPassword = document.getElementById("confirm-password").value;

            if (!name || !email || !password || !confirmPassword) {
                alert("Please fill in all fields.");
                return;
            }

            if (password !== confirmPassword) {
                alert("Passwords do not match.");
                return;
            }

            alert("Signup successful! Redirecting to login...");
            window.location.href = "teacher-login.html"; // Redirect to login
        });
    }
});
