document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("student-signup-form").addEventListener("submit", function (event) {
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
        window.location.href = "student-login.html"; // Redirect to login after signup
    });
});
