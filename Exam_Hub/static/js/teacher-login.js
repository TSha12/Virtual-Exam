document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("teacher-login-form").addEventListener("submit", function (event) {
        event.preventDefault();
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (email && password) {
            alert("Login successful! Redirecting...");
            window.location.href = "teacher-portal.html"; // Redirect to the teacher dashboard
        } else {
            alert("Please fill in all fields.");
        }
    });
});
