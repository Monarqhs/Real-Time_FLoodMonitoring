document.addEventListener('DOMContentLoaded', function() {
    fetch('/weather')
        .then(response => response.json())
        .then(data => {
            document.getElementById('description').textContent = data.description;
            document.getElementById('temperature').textContent = data.temperature;
            document.getElementById('humidity').textContent = data.humidity;
            document.getElementById('wind-speed').textContent = data.wind_speed;
            document.getElementById('wind-direction').textContent = data.wind_direction;
        });

    var map = L.map('map').setView([-6.2146, 106.8451], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    fetch('/heatmap-data')
        .then(response => response.json())
        .then(data => {
            // Example: Generate heatmap using Heatmap.js
            var heatmap = L.heatLayer(data).addTo(map);
        });

    // Example marker for flood detection
    L.marker([-6.2146, 106.8451]).addTo(map)
        .bindPopup('Flooding detected here')
        .openPopup();

    // Example: Generate rainfall chart using Chart.js
    var ctx = document.getElementById('rainfall-chart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'Rainfall',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
                data: [65, 59, 80, 81, 56, 55, 40]
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
