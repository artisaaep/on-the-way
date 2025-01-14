let url = "https://d2fd-188-130-155-177.ngrok-free.app";
function initializeCustomCheckboxes() {
    const checkboxes = document.querySelectorAll('.checkbox__checkmark');
    checkboxes.forEach(checkbox => {
        // Добавить необходимые обработчики событий или стили
        checkbox.addEventListener('click', () => {
            const input = checkbox.previousElementSibling;
            input.checked = true;
        });
    });
}
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

function backToRole() {
    console.log("back");
    window.location.href = "chooserole.html";
}


function main() {
    window.Telegram.WebApp.expand();
}

function setCurrentTime() {
    var now = new Date();

    var hours = now.getHours().toString().padStart(2, '0');
    var minutes = now.getMinutes().toString().padStart(2, '0');

    var currentTime = hours + ':' + minutes;

    const times = document.querySelectorAll('.time-f');
    times.forEach(win => {
        win.value = currentTime;
    })
}


function setCurrentDate() {
    var now = new Date();

    var year = now.getFullYear();
    var month = (now.getMonth() + 1).toString().padStart(2, '0'); 
    var day = now.getDate().toString().padStart(2, '0');
    
    var currentDate = year + '-' + month + '-' + day;
    
    document.getElementById('date-f').value = currentDate;
}

window.addEventListener('load', setCurrentTime);
window.addEventListener('load', setCurrentDate);

let tripData = {
    origin: '',
    destination: '',
    addInfoDest: '',
    addInfoOrigin: '',
    available_seats: 0,
    date: '',
    time: '',
    type: '',
    price: 0,
    car: '',
    lagg: false,
    an: false,
    ch: false,
    bust: false,
    av: '',
    additional: '',
    car_id: 1,
    is_request: 0
};

function driver() {
    tripData.is_request = 0;
    goToStep(1);
}

function passenger() {
    tripData.is_request = 1;
    goToStep(1);
}

function updateTripData() {
    const tripDataDiv = document.getElementById('trip-data');
    tripDataDiv.innerHTML = `
        <p>Откуда: ${tripData.origin} (${tripData.addInfoOrigin})</p>
        <p>Куда: ${tripData.destination} (${tripData.addInfoDest})</p>
        <p>Дата и время: ${tripData.date}</p>
    `;
}

function selectOrigin(city, id) {
    if (city == "Казань") {
        selectDestination('Иннополис', 'left2');
    } else {
        selectDestination('Казань', 'right2');
    }
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
    const times = document.querySelectorAll('.time-f');
    tripData.date = `${date.value}`;  
    tripData.time = `${times[0].value}-${times[1].value}`;
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
    if (cuurent == 6) {
        const ownRadio = document.getElementById('own');
        console.log(ownRadio);
        if (!ownRadio.checked) {
            goToStep(4);
            return;
        }
    }
    goToStep(cuurent - 1);

}

function showSummary() {
    document.getElementById('summary-text').innerText = `Город отправления: ${tripData.origin}, Город назначения: ${tripData.destination}, Дата поездки: ${tripData.date}  ${tripData.date}`;
}

async function submitTrip() {
    let input = document.getElementById('av');
    tripData.available_seats = input.value;
    await fetch(url + "/api/trips/", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "start_location": tripData.origin,
            "end_location": tripData.destination,
            "departure_time": tripData.time,
            "price": tripData.price,
            "available_seats": tripData.available_seats,
            "has_child_seat": tripData.ch,
            "departure_date": tripData.date,
            "clarify_from": tripData.addInfoOrigin,
            "clarify_to": tripData.addInfoDest,
            "car_id": tripData.car_id,
            "driver_id": window.Telegram.WebApp.initDataUnsafe.user.id,
            "is_request": tripData.is_request,
            "add_info": tripData.additional
          }),
    }).then(async response => {
        if (response.ok) {
            let id = window.Telegram.WebApp.initDataUnsafe.user.id;
            let kb = {
                inline_keyboard: [[{
                    text: 'Подробнее',
                    web_app: { url: `${url}/static/tripinfo.html`}
                }]]
            };
            let text = `Ваша поездка *${tripData.origin} - ${tripData.destination}* успешно создана! 🚙
            
Нажмите на кнопку ниже, чтобы посмотреть подробную информацию о поездке или отредактировать ее ☺️`;

            let encodedText = encodeURIComponent(text);
            let encodedReplyMarkup = encodeURIComponent(JSON.stringify(kb));
            console.log("aaa");
            await fetch(`https://api.telegram.org/bot6658030178:AAF7JwKztrDvVQVlzR3lZlSebnf961JUocs/sendMessage?chat_id=${id}&text=${encodedText}&parse_mode=Markdown&reply_markup=${encodedReplyMarkup}`);
            // TODO: token from .env
            window.location.href = "tripcreated.html";
            

        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    });
}

async function checkCar() {
    let input = document.getElementById('price-rub');
    tripData.price = input.value;
    const ownRadio = document.getElementById('own');
    if (ownRadio.checked) {
        goToStep(5);
        const bar = document.getElementById("carchoice");
        const response = await (await fetch(url + "/api/users/" + window.Telegram.WebApp.initDataUnsafe.user.id, {
            method: "GET",
        })).json();
        if (response.car_ids.length == 0){
            bar.innerHTML = `<p id="no-cars">У вас пока нет машин.</p>`;
            return;
        }
        bar.innerHTML = "";
        response.car_ids.forEach(async(id) => {
            const response = await (await fetch(url + "/api/cars/" + id, {
                method: "GET",
            })).json();
            bar.innerHTML += `
                <li>
                    <label for="car-${id}">
                        <input type="radio" id="car-${id}" name="c">
                        <div class="checkbox__checkmark"></div>
                        ${response.color} ${response.brand}
                    </label>
                </li>
            `
        });
    } else {
        goToStep(6);
    }
}

function goToStep(step) {
    document.querySelectorAll('.step').forEach(el => el.classList.remove('active'));
    document.getElementById(`step${step}`).classList.add('active');
}

main()