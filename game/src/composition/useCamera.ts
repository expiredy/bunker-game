function sendFrame(frame: any) {
    var request = new XMLHttpRequest();
    request.open('POST', '/submit?image=' + frame.toString('base64'), true);
    request.send();
}