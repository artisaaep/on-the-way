let url = "https://d2fd-188-130-155-177.ngrok-free.app";

document.addEventListener('DOMContentLoaded', function() {
    const tabBtn1 = document.getElementById('tab-btn-1');
    const tabBtn2 = document.getElementById('tab-btn-2');
    const mainScrollingDiv = document.getElementById('main-scrolling-div');
    const pasScrollingDiv = document.getElementById('pas-scrolling-div');

    function toggleScrollingDivs() {
        if (tabBtn1.checked) {
            mainScrollingDiv.style.display = 'block';
            pasScrollingDiv.style.display = 'none';
        } else if (tabBtn2.checked) {
            mainScrollingDiv.style.display = 'none';
            pasScrollingDiv.style.display = 'block';
        }
    }

    tabBtn1.addEventListener('change', toggleScrollingDivs);
    tabBtn2.addEventListener('change', toggleScrollingDivs);

    toggleScrollingDivs();
});

async function apply(trip_id) {
    await fetch(url + "/api/trips/" + trip_id + "/rider?riderID=" + window.Telegram.WebApp.initDataUnsafe.user.id, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "has_luggage": false,
            "has_kids": false,
            "has_pets": false
        })
    }).then(response => {
        if (response.ok) {
            const btn = document.getElementById("choose-" + trip_id);
            btn.onclick = rejectDecorator(trip_id);
            btn.textContent = "Отменить";
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    })
}

async function reject(trip_id) {
    await fetch(url + "/api/trips/" + trip_id + "/rider?riderID=" + window.Telegram.WebApp.initDataUnsafe.user.id, {
        method: "DELETE",
    }).then(response => {
        if (response.ok) {
            const btn = document.getElementById("choose-" + trip_id);
            btn.onclick = applyDecorator(trip_id);
            btn.textContent = "Выбрать";
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    })
}

const rejectDecorator = (trip_id) => {
    return () => {
        return reject(trip_id)
    }
}

const applyDecorator = (trip_id) => {
    return () => {
        return apply(trip_id)
    }
}

async function wide(trip_id) {
    window.location.href = "driversprof.html?" + trip_id;
}

async function main() {
    window.Telegram.WebApp.expand();
    const bar = document.getElementById("main-scrolling-div");
    const response = await (await fetch(url + "/api/trips", {
        method: "GET",
    })).json();
    const drivers = [];
    const requests = [];
    for (const element of response) {
        if (!element.is_request) {
            drivers.push(element);
        } else {
            requests.push(element);
        }
    }
    if (drivers.length===0){
        bar.innerHTML = `<p>Пока нет доступных поездок от водителей.</p>`;
    } else {
        bar.innerHTML = ``;
    }
    drivers.forEach(trip => {
        let is_attached = false;
        console.log(trip.passengers)
        for (let index in trip.passengers) {
            console.log(trip.passengers[index]);
            if (trip.passengers[index].id !== window.Telegram.WebApp.initDataUnsafe.user.id) {
                continue;
            }
            is_attached = true;
            break;
        }
        
        bar.innerHTML += `
            <div onclick="wide(${trip.id})" class="card" id="card">
                <img class="avatar" alt="driver-avatar" src="${url}/api/users/${trip.driver.id}/photo">
                <a class="driver_name">${trip.driver.name}</a>
                <div class="maininfa">
                    <div class="from_main">
                        <a class="from">${trip.start_location}</a><br>
                        <a class="clari-from">${trip.clarify_from}</a>
                    </div>
                    <div class="bott">
                        <a class="date">${trip.departure_date}<br></a>
                        <a class="arrow">&#8594;</a><br>
                        <a class="time">${trip.departure_time}</a>
                    </div>
                    <div class="to_main">
                        <a class="to"><br>${trip.end_location}</a><br>
                        <a class="clari-to">${trip.clarify_to}</a>
                    </div>
                </div>
                <div class="pr-ch">
                    <a class="price">${trip.price} руб.</a>` +
            (is_attached
                    ? `<button class="driver_choose" onClick="reject(${trip.id})" id="choose-${trip.id}">Отменить</button>`
                    : `<button class="driver_choose" onClick="apply(${trip.id})" id="choose-${trip.id}">Выбрать</button>`
            ) +
            `</div>
                <div class="dopinfa">
                    <a class="rides" id="rides-amount-of-${trip.id}-driver">Поездок: ${trip.driver.rides_amount} <br></a>
                    <a class="free-places">Свободных мест: ${trip.available_seats}</a>
                </div>
            </div>
        `
    })
    const bar2 = document.getElementById("pas-scrolling-div");
    if (requests.length===0){
        bar2.innerHTML = `<p>Пока нет запросов на поездки от пассажиров.</p>`;
    } else {
        bar2.innerHTML = ``;
    }
    requests.forEach(trip => {
        let is_attached = false;
        console.log(trip.passengers)
        for (let index in trip.passengers) {
            console.log(trip.passengers[index]);
            if (trip.passengers[index].id !== window.Telegram.WebApp.initDataUnsafe.user.id) {
                continue;
            }
            is_attached = true;
            break;
        }
        
        bar2.innerHTML += `
            <div onclick="wide(${trip.id})" class="card" id="trip-card-by-id-${trip.id}">
                <img class="avatar" alt="driver-avatar" src="${url}/api/users/${trip.driver.id}/photo">
                <a class="request_name">${trip.driver.name}</a>
                <div class="maininfa">
                    <div class="from_main">
                        <a class="from">${trip.start_location}</a><br>
                        <a class="clari-from">${trip.clarify_from}</a>
                    </div>
                    <div class="bott">
                        <a class="date">${trip.departure_date}<br></a>
                        <a class="arrow">&#8594;</a><br>
                        <a class="time">${trip.departure_time}</a>
                    </div>
                    <div class="to_main">
                        <a class="to"><br>${trip.end_location}</a><br>
                        <a class="clari-to">${trip.clarify_to}</a>
                    </div>
                </div>
                <div class="pr-ch">
                    <a class="price">${trip.price} руб.</a>` +
            (is_attached
                    ? `<button class="request_choose" onClick="reject(${trip.id})" id="choose-${trip.id}">Отменить</button>`
                    : `<button class="request_choose" onClick="apply(${trip.id})" id="choose-${trip.id}">Выбрать</button>`
            ) +
            `</div>
                <div class="dopinfa">
                    <a class="rides" id="rides-amount-of-${trip.id}-driver">Поездок: ${trip.driver.rides_amount} <br></a>
                    <a class="free-places">Свободных мест: ${trip.available_seats}</a>
                </div>
            </div>
        `
    })
}

main()