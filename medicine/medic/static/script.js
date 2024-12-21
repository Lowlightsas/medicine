// Инициализация Firebase
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.1/firebase-app.js";
import { getDatabase, ref, onValue } from "https://www.gstatic.com/firebasejs/9.17.1/firebase-database.js";

// Ваши Firebase настройки
const firebaseConfig = {
    apiKey: "AIzaSyDDTmDajaG2csbY-3WxfisORk8DcOCyvls",
    authDomain: "esp32-firebase-db-a2a7d.firebaseapp.com",
    databaseURL: "https://esp32-firebase-db-a2a7d-default-rtdb.asia-southeast1.firebasedatabase.app/",
    projectId: "esp32-firebase-db-a2a7d",
    storageBucket: "esp32-firebase-db-a2a7d.firebasestorage.app",
    messagingSenderId: "946481331769",
    appId: "1:946481331769:web:99347ea11c8f8d89eb57e8"
};

// Инициализация приложения
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

// Элементы графика
const ctx = document.getElementById('temperatureChart').getContext('2d');
const temperatureData = [];
const humidityData = [];
const labels = [];

// Создание графика
const temperatureChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels, // Временные метки
        datasets: [
            {
                label: 'Температура (°C)',
                data: temperatureData,
                borderColor: 'blue',
                fill: false,
                tension: 0.1
            },
            {
                label: 'Влажность (%)',
                data: humidityData,
                borderColor: 'orange',
                fill: false,
                tension: 0.1
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Время'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Значения'
                }
            }
        }
    }
});

// Подписка на данные из Firebase
const tempRef = ref(database, 'DHT_11/Temperature');
const humidityRef = ref(database, 'DHT_11/Humidity');

onValue(tempRef, (snapshot) => {
    const value = snapshot.val();
    if (value !== null) {
        const time = new Date().toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        temperatureData.push(value);
        labels.push(time);

        // Ограничиваем данные до 10 последних значений
        if (temperatureData.length > 10) {
            temperatureData.shift();
            labels.shift();
        }

        temperatureChart.update();
    } else {
        console.error("Температура не найдена в базе данных.");
    }
});

onValue(humidityRef, (snapshot) => {
    const value = snapshot.val();
    if (value !== null) {
        humidityData.push(value);

        // Ограничиваем данные до 10 последних значений
        if (humidityData.length > 10) {
            humidityData.shift();
        }

        temperatureChart.update();
    } else {
        console.error("Влажность не найдена в базе данных.");
    }
});
