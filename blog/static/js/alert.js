document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function() {
        var messageAlert = document.getElementById("message-alert");
        if (messageAlert) {
            messageAlert.style.display = "none";
        }
    }, 3000); // 3000 milliseconds = 3 seconds
});