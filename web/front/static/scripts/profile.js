async function main() {
    window.Telegram.WebApp.expand();
    let url = "https://d2fd-188-130-155-177.ngrok-free.app";
    const userUrl = url + "/api/users/" + window.Telegram.WebApp.initDataUnsafe.user.id;
    const response = await (await fetch(userUrl, {})).json();
    const img = document.getElementById("avatar");
    img.src = userUrl + "/photo";
    const nameElem = document.getElementById("name");
    nameElem.textContent = response.name;
    const sexElem = document.getElementById("sex");
    if (response.sex) {
        sexElem.textContent += "Женский";
    } else {
        sexElem.textContent += "Мужской";
    }
    const ageElem = document.getElementById("age");
    ageElem.textContent = "Возраст: " + response.age;
    const ridesElem = document.getElementById("rides");
    ridesElem.textContent = "Количество поездок: " + response.rides_amount;
    const carsElem = document.getElementById("cars-ul");
    if (response.car_ids.length == 0) {
        carsElem.innerHTML = `<p>У вас ещё нет добавленных машин.</p>`;
    } else {
        for (const id of response.car_ids) {
            const carInfo = await (await fetch(url + "/api/cars/" + id, {})).json();
            console.log(carInfo);
            carsElem.innerHTML += `<li><p class="car"><b>${carInfo.color} ${carInfo.brand} ${carInfo.number}</b></p></li>`;
        }
    }
}

main();
