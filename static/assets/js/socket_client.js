const socket = io.connect('http://' + document.domain + ':' + location.port);

function fetchData() {
    socket.emit('request_data');
}

function displayData(data) {
    const cpu_event_number = document.getElementById('cpu_event_number');
    if (cpu_event_number) {
        cpu_event_number.textContent = data.cpu_event_number;
    }

    const mem_event_number = document.getElementById('mem_event_number');
    if (mem_event_number) {
        mem_event_number.textContent = data.mem_event_number;
    }

    const storage_event_number = document.getElementById('storage_event_number');
    if (storage_event_number) {
        storage_event_number.textContent = data.storage_event_number;
    }

    const network_event_number = document.getElementById('network_event_number');
    if (network_event_number) {
        network_event_number.textContent = data.network_event_number;
    }
}

socket.on('data_response', function (data) {
    displayData(data);
});

setInterval(fetchData, 5000);
