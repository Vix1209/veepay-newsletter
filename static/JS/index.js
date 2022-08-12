
let checkEmail = () => {
    form.action = "#";
    const email = document.getElementById("email");
    const emailValue = email.value;
    const errorBox = document.getElementById("error-message");

    if (emailValue == "") {
        errorBox.style.display = "flex";
        email.focus();
        setTimeout(hideAlert, 2000)
        function hideAlert() {
            errorBox.style.display = "none";
        }
        return;
    } else {
        form.action = "/templates/pages/thankyou.html";
    }
}
