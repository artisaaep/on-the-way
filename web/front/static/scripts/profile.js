async function main() {
    let url = "https://8aef-188-130-155-165.ngrok-free.app";
    const userUrl = url + "/api/users/" + window.Telegram.WebApp.initDataUnsafe.user.id;
    const response = await (await fetch(userUrl, {})).json();
    const img = document.getElementById("avatar");
    img.src = userUrl + "/photo";
    const nameElem = document.getElementById("name");
    nameElem.textContent = response.name;
    const ageElem = document.getElementById("age");
    ageElem.textContent = "Возраст: " + response.age;
    const ridesElem = document.getElementById("rides");
    ridesElem.textContent = "Количество поездок: " + response.rides_amount;
    const carsElem = document.getElementById("cars-ul");
    for (const id of response.car_ids) {
        const carInfo = await (await fetch(url + "/api/cars/" + id, {})).json();
        carsElem.innerHTML += `<li><p class="car"><b>${carInfo.color} ${carInfo.brand} ${carInfo.number}</b></p></li>`;
    }
}

main();
