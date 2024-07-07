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
    let date = document.getElementById('trip-date');
    let time = document.getElementById('trip-time');
    const selectedDate = new Date(`${date.value}T${time.value}`);
    const now = new Date();

    if (selectedDate > now) {
        tripData.date = `${date.value}   ${time.value}`;
        goToStep(4);
        updateTripData();
    } else {
        alert('Выберите дату и время позже текущего момента.');
    }
}

function selectTypePrice() {
    const selectedType = document.querySelector('input[name="r"]:checked');
    if (selectedType) {
        tripData.type = selectedType.nextElementSibling.textContent;
        tripData.price = document.getElementById('price-rub').value;
        if (tripData.type === 'На своей машине') {
            fetchCarOptions();
        } else {
            goToStep(6);
        }
        updateTripData();
    } else {
        alert('Выберите вид поездки.');
    }
}

function fetchCarOptions() {
    fetch('/api/cars/')
        .then(response => response.json())
        .then(cars => {
            const carList = document.querySelector('.car ul.choice');
            carList.innerHTML = '';
            cars.forEach(car => {
                const carItem = document.createElement('li');
                carItem.innerHTML = `
                    <label for="car${car.id}">
                        <input type="radio" id="car${car.id}" name="c" value="${car.id}">
                        <div class="checkbox__checkmark"></div>
                        ${car.brand} - ${car.color}
                    </label>
                `;
                carList.appendChild(carItem);
            });
            goToStep(5);
        })
        .catch(error => console.error('Error fetching cars:', error));
}

function selectCar() {
    const selectedCar = document.querySelector('input[name="c"]:checked');
    if (selectedCar) {
        tripData.car = selectedCar.value;
        goToStep(6);
        updateTripData();
    } else {
        alert('Выберите машину.');
    }
}

function goBack(current) {
    goToStep(current - 1);
}

function showSummary() {
    document.getElementById('summary-text').innerText = `Город отправления: ${tripData.origin}, Город назначения: ${tripData.destination}, Дата поездки: ${tripData.date}`;
}

function submitTrip() {
    fetch('/api/trips/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(tripData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Trip submitted:', data);
        alert('Поездка успешно создана!');
    })
    .catch(error => console.error('Error submitting trip:', error));
}

function goToStep(step) {
    document.querySelectorAll('.step').forEach(el => el.classList.remove('active'));
    document.getElementById(`step${step}`).classList.add('active');
}
