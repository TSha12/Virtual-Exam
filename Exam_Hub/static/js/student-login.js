document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("student-login-form").addEventListener("submit", function (event) {
        event.preventDefault();
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (!email || !password) {
            alert("Please enter both email and password.");
            return;
        }

        alert("Login successful! Redirecting to dashboard...");
        window.location.href = "student-dashboard.html"; // Redirect to dashboard after login
    });
});
