function generate() {
    var content = document.getElementById('content').value;
    eel.generate(content)(setImage);
}

function setImage(base64) {
    document.getElementById('qrcode').src = base64;
}