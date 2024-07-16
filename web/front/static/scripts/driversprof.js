let url = "https://d2fd-188-130-155-177.ngrok-free.app";

async function main() {
    let trip_id = window.location.href.split('?')[1];
    const name = document.getElementById("name");
    const age = document.getElementById("age");
    const sex = document.getElementById("sex");
    const rides = document.getElementById("rides");
    const date = document.getElementById("date");
    const from = document.getElementById("from");
    const to = document.getElementById("to");
    const time = document.getElementById("time");
    const clarfrom = document.getElementById("clari-from");
    const clarto = document.getElementById("clari-to");
    const price = document.getElementById("price");
    const photo = document.getElementById("avatar");
    const car = document.getElementById("named");

    const trip = await (await fetch(url + "/api/trips/" + trip_id, {
        method: "GET",
    })).json();
    console.log(trip);
    name.innerHTML = trip.driver.name;
    age.innerHTML = "Возраст: " + trip.driver.age;
    if (trip.driver.sex) {
        sex.innerHTML = "Пол: Женский";
    } else {
        sex.innerHTML = "Пол: Мужской";
    }
    rides.innerHTML = "Количество поездок: " + trip.driver.rides_amount;
    date.innerHTML = trip.departure_date;
    from.innerHTML = trip.start_location;
    to.innerHTML = trip.end_location;
    time.innerHTML = trip.departure_time;
    clarfrom.innerHTML = trip.clarify_from;
    clarto.innerHTML = trip.clarify_to;
    price.innerHTML = trip.price + " руб.";
    photo.src = `${url}/api/users/${trip.driver.id}/photo`;
    car.innerHTML = trip.car.brand;
}

main();