// success_alert.js
document.addEventListener("DOMContentLoaded", function () {
    var successMessage = "{{ success_message }}";

    if (successMessage) {
        alert(successMessage);
    }
});
