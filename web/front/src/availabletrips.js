let url = process.env["BASE_WEBAPP_URL "];

async function apply(trip_id) {
    await fetch(url + "/api/trips/" + trip_id + "/rider?riderID=" + window.Telegram.WebApp.initDataUnsafe.user.id, {
        method: "put",
    }).then(response => {
        if (response.ok) {
            const btn = document.getElementById("choose-" + trip_id);
            btn.onclick = async () => {
                await fetch(url + "/api/trips/" + trip_id + "/rider?riderID=" + window.Telegram.WebApp.initDataUnsafe.user.id, {
                    method: "DELETE",
                }).then(response => {
                    if (response.ok) {
                        btn.onclick = apply;
                        btn.textContent = "Выбрать";
                    } else {
                        window.Telegram.WebApp.showAlert("Something went wrong");
                    }
                })
            }
            btn.textContent = "Отменить";
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    })
}


async function main() {
    const bar = window.document.querySelector('.scrolling');
    const response = await (await fetch(url + "/api/trips")).json();
    response.forEach(trip => {
        bar.innerHTML += `
<div class="card">
    <img class="avatar" src="${url}/api/users/${trip.driver.id}/photo">
    <a class="name">${trip.driver.name}</a>
    <div class="maininfa">
        <a class="date">${trip.departure_time}<br></a>
        <a class="from">${trip.start_location}</a>
        <a class="strelka">&#8594;</a>
        <a class="to"><br>${trip.end_location}</a>
    </div>
    <div class="pr-ch">
        <button class="choose" onclick="apply(${trip.id})" id="choose-${trip.id}">Выбрать</button>
    </div>
    <div class="dopinfa">
        <a class="rides">Поездок: ${trip.driver.rides_amount} <br></a>
        <a class="free-places">Свободных мест: ${trip.available_seats}</a>
    </div>
</div>
`
    })
}

main()