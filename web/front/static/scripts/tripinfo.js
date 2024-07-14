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

main();
