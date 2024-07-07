document.addEventListener('DOMContentLoaded', (event) => {
    const comments = document.querySelectorAll('.com');

    function handleClickOutside(event) {
        comments.forEach(comment => {
            if (comment === document.activeElement && !comment.contains(event.target)) {
                comment.blur(); 
            }
        });
    }

    ['click', 'touchstart', 'touchend', 'touchcancel', 'touchmove'].forEach(eventType => {
        document.addEventListener(eventType, handleClickOutside);
    });
});

let tripData = {
    origin: '',
    destination: '',
    addInfoDest: '',
    addInfoOrigin: '',
    date: '',
    time: '',
    type: '',
    price: '',
    car: '',
    lagg: false,
    an: false,
    ch: false,
    bust: false,
    av: '',
    additional: ''
};

function updateTripData() {
    const tripDataDiv = document.getElementById('trip-data');
    tripDataDiv.innerHTML = `
        <p>Откуда: ${tripData.origin} (${tripData.addInfoOrigin})</p>
        <p>Куда: ${tripData.destination} (${tripData.addInfoDest})</p>
        <p>Дата и время: ${tripData.date}</p>
    `;
}

function selectOrigin(city, id) {
    tripData.origin = city;
    const button = document.getElementById(id);
    if (button.classList.contains('selected')) {
        button.classList.remove('selected');
        button.style.backgroundColor = ''; 
    } else {
        document.querySelectorAll('.button1').forEach(btn => {
            btn.classList.remove('selected');
            btn.style.backgroundColor = '';
        });

        button.classList.add('selected');
        button.style.backgroundColor = '#969696';
    }
    updateTripData()
}

function selectDestination(city, id) {
    tripData.destination = city;
    const button = document.getElementById(id);
    if (button.classList.contains('selected')) {
        button.classList.remove('selected');
        button.style.backgroundColor = ''; 
    } else {
        document.querySelectorAll('.button2').forEach(btn => {
            btn.classList.remove('selected');
            btn.style.backgroundColor = '';
        });

        button.classList.add('selected');
        button.style.backgroundColor = '#969696';
    }
    updateTripData()
}

function addInfoOrigin() {
    let input = document.getElementById('comment1');
    tripData.addInfoOrigin = input.value;
    goToStep(2);
    updateTripData()
}

function addInfoDest() {
    let input = document.getElementById('comment2');
    tripData.addInfoDest = input.value;
    goToStep(3);
    updateTripData()
}

function selectDate() {
    let date = document.getElementById('date-f');
    let time = document.getElementById('time-f');
    tripData.date = `${date.value}   ${time.value}`;
    goToStep(4);
    updateTripData()
}

function selectTypePrice(date) {
    tripData.date = date;
}

function selectCar(date) {
    tripData.date = date;
}

function goBack(cuurent) {
    goToStep(cuurent - 1);
}

function showSummary() {
    document.getElementById('summary-text').innerText = `Город отправления: ${tripData.origin}, Город назначения: ${tripData.destination}, Дата поездки: ${tripData.date}`;
}

function submitTrip() {
    window.location.href = "tripcreated.html";
    console.log('Trip submitted:', tripData);
}

function goToStep(step) {
    document.querySelectorAll('.step').forEach(el => el.classList.remove('active'));
    document.getElementById(`step${step}`).classList.add('active');
}