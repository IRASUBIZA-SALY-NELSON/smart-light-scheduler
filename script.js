function submitSchedule() {
    const onTime = document.getElementById('onTime').value;
    const offTime = document.getElementById('offTime').value;

    const schedule = {
        on: onTime,
        off: offTime
    };

    const socket = new WebSocket('ws://localhost:8765'); // Make sure port matches Python server

    socket.onopen = () => {
        console.log('WebSocket connected, sending schedule...');
        socket.send(JSON.stringify(schedule));
    };

    socket.onmessage = (event) => {
        alert("Server response: " + event.data);
        socket.close();
    };

    socket.onerror = (error) => {
        console.error('WebSocket error:', error);
    };
}
