const socket = io.connect('http://' + document.domain + ':' + location.port);

function fetchData() {
    socket.emit('tart_pc',{
        "url": window.location.href,
    });
}

function displayData(data) {
    const cpu = document.getElementById('cpu');
    if (cpu) {
        cpu.textContent = data.cpu;
    }

    const mem = document.getElementById('mem');
    if (mem) {
        mem.textContent = data.mem;
    }

    const str = document.getElementById('str');
    if (str) {
        str.textContent = data.str;
    }

    const net = document.getElementById('net');
    if (net) {
        net.textContent = data.net;
    }

    const err = document.getElementById('err');
    if (err) {
        err.textContent = data.err;
    }

}

socket.on('data_response', function (data) {
    displayData(data);
});

setInterval(fetchData, 5000);
