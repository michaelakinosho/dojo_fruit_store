function grabCheckoutDateTime() {
    var newDateTime = new Date().toLocaleString()
    console.log(newDateTime)
    document.getElementById("newDate").innerText = newDateTime;
}