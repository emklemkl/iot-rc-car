const net = require('net');

    const client = net.createConnection({ port: 3000, host: "192.168.1.11" }, () => {
        console.log('Connected to server!');
        client.write('123');
    });


client.on('data', (data) => {
    console.log('Received from server:', data.toString());
    client.end(); // Close the connection
});

client.on('end', () => {
    console.log('Disconnected from server');
});

// document.getElementById("forward").addEventListener("click", (e) => {
//     console.log("asdasd");
//     client.write('forward');
// })