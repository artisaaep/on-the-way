let url = "https://8aef-188-130-155-165.ngrok-free.app";

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

async function main() {
    const bar = document.getElementById("main-scrolling-div");
    const response = await (await fetch(url + "/api/trips", {
        method: "GET",
    })).json();
    response.forEach(trip => {
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
        const msg = is_attached ? "Отменить" : "Выбрать";
        bar.innerHTML += `
            <div class="card">
                <img class="avatar" alt="driver-avatar" src="${url}/api/users/${trip.driver.id}/photo">
                <a class="name">${trip.driver.name}</a>
                <div class="maininfa">
                    <a class="date">${trip.departure_time}<br></a>
                    <a class="from">${trip.start_location}</a>
                    <a class="strelka">&#8594;</a>
                    <a class="to"><br>${trip.end_location}</a>
                </div>
                <div class="pr-ch">
                    <a class="price">${trip.price} руб.</a>` +
            (is_attached
                    ? `<button class="choose" onClick="reject(${trip.id})" id="choose-${trip.id}">Отменить</button>`
                    : `<button class="choose" onClick="apply(${trip.id})" id="choose-${trip.id}">Выбрать</button>`
            ) +
            `</div>
                <div class="dopinfa">
                    <a class="rides">Поездок: ${trip.driver.rides_amount} <br></a>
                    <a class="free-places">Свободных мест: ${trip.available_seats}</a>
                </div>
            </div>
        `
    })
}

main()