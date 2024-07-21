let url = "https://d2fd-188-130-155-177.ngrok-free.app";

async function main() {
    let url = "https://d2fd-188-130-155-177.ngrok-free.app";
    let href = document.location.href;
    let id = href.split("?")[1].split("#")[0];
    const trip = await (await fetch(url + "/api/trips/" + id, {
        method: "GET",
    })).json();
    let from = document.getElementById('from');
    let clarfrom = document.getElementById('clarfrom');
    let to = document.getElementById('to');
    let clarto = document.getElementById('clarto');
    let date = document.getElementById('date');
    let time = document.getElementById('time');
    let cost = document.getElementById('cost');
    let free = document.getElementById('free');
    from.placeholder = trip.start_location;
    clarfrom.placeholder = trip.clarify_from;
    to.placeholder = trip.end_location;
    clarto.placeholder = trip.clarify_to;
    date.placeholder = trip.departure_date;
    time.placeholder = trip.departure_time;
    cost.placeholder = trip.price;
    free.placeholder = trip.available_seats;
}

async function edit() {
    let from = document.getElementById('from').value;
    let clarfrom = document.getElementById('clarfrom').value;
    let to = document.getElementById('to').value;
    let clarto = document.getElementById('clarto').value;
    let date = document.getElementById('date').value;
    let time = document.getElementById('time').value;
    let cost = document.getElementById('cost').value;
    let free = document.getElementById('free').value;

    let href = document.location.href;
    let id = href.split("?")[1].split("#")[0];

    const trip = await (await fetch(url + "/api/trips/" + id, {
        method: "GET",
    })).json();

    if (!from) {
        from = trip.start_location;
    }
    if (!clarfrom) {
        clarfrom = trip.clarify_from;
    }
    if (!to) {
        to = trip.end_location;
    }
    if (!clarto) {
        clarto = trip.clarify_to;
    }
    if (!date) {
        date = trip.departure_date;
    }
    if (!time) {
        time = trip.departure_time;
    }
    if (!cost) {
        cost = trip.price;
    }
    if (!free) {
        free = trip.available_seats;
    }

    const newtrip = await (await fetch(url + "/api/trips/" + id + "?driverID=" + trip.driver.id, {
        method: "PUT",
        body: JSON.stringify({
            "start_location": from,
            "end_location": to,
            "departure_time": time,
            "price": cost,
            "available_seats": free,
            "has_child_seat": trip.has_child_seat,
            "departure_date": date,
            "clarify_from": clarfrom,
            "clarify_to": clarto,
            "car_id": trip.car.id,
            "driver_id": trip.driver.id,
            "is_request": trip.is_request,
            "add_info": trip.add_info
        })
    }));

}

main();
