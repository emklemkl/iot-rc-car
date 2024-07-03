import { KEY } from "./config.js"
const CONNECT_TO_IP = "192.168.1.9"
const CONNECT_TO_PORT = "3000"
let ws;
window.addEventListener("load", establishWebSocketConnection)

carControllerDiv = document.getElementById("car-controller");
carControllerDiv.addEventListener("change", (e) => {
    drive(e.target.value)
})

async function establishWebSocketConnection() {
    ws = new WebSocket(`ws://${CONNECT_TO_IP}:${CONNECT_TO_PORT}`);
    ws.onerror = function (event) {
        console.error("WebSocket error observed:", event);
    };

    ws.onopen = function (event) {
        console.log("WebSocket is open.");
        ws.send('Client connected');
    };
}
async function fetchData() {
    const url = `https://io.adafruit.com/api/v2/emklemkl/feeds/temperature/data?limit=10`;
    const response = await fetch(url, {
        headers: {
            'X-AIO-Key': KEY
        }
    });
    const data = await response.json();
    const mean = () => (data.reduce((tot, curr) => tot + parseFloat(curr.value), 0)) / (data.length + 1)
    document.getElementById("temp").value = await mean().toFixed(1) + "°C"
    console.log(data);
}
function drive(value) {
    ws.send(value)
}
fetchData()
setInterval(async () => fetchData(), 10000)
