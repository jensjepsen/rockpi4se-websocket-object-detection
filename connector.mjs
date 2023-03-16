var canvas = document.getElementById("c");
var ctx = canvas.getContext("2d");

ctx.lineWidth = 5
ctx.strokeStyle = 'green'

let model = await cocoSsd.load();

var image = new Image();

image.onload = async () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    ctx.beginPath()
    ctx.drawImage(image, 0, 0);
    if(model !== null) {
        const objects = await model.detect(image)
        let x, y, w, h
        for(const obj of objects) {
            [x, y, w, h] = obj.bbox
            ctx.rect(x, y, w, h)
            ctx.stroke()
            ctx.fillText(obj.class, x, y-10)
        }
    }
}

let socket = null;

window.connectSocket =  () => {
    // Create WebSocket connection.
    //const socket = new WebSocket('ws://192.168.0.143:8765')
    socket = new WebSocket('ws://localhost:8765')

    // Connection opened
    socket.addEventListener('open', (event) => {})

    // Listen for messages
    socket.addEventListener('message', (event) => {
        image.src = "data:image/png;base64," + event.data;
    })
}