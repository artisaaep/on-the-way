<script lang="ts">
    import {onMount} from "svelte";
    import {Trip} from "$lib/Types";
    import "./driversprof.css"
    import {url} from "../../enviroment";

    let trip: Trip;
    let sex: string;
    let photo: string;

    async function main() {
        var BackButton = window.Telegram.WebApp.BackButton;
        BackButton.show();
        BackButton.onClick(function () {
            window.history.back();
            BackButton.hide();
        });
        let trip_id = window.location.href.split('?')[1];
        console.log(await fetch(url + "/api/trips/" + trip_id, {
            method: "GET",
        }));
        trip = await (await fetch(url + "/api/trips/" + trip_id, {
            method: "GET",
        })).json();
        console.log(trip);
        if (trip.driver.sex) {
            sex = "Женский";
        } else {
            sex= "Мужской";
        }
        photo = `${url}/api/users/${trip.driver.id}/photo`;
    }

    onMount(main);
</script>
{#if trip}
    <p id="name">{trip.driver.name}</p>

    <div class="bio">
        <img src={photo} alt="Аватарка" id="avatar">
        <div id="textt">
            <p id="age">Возраст: {trip.driver.age}</p>
            <p id="sex">Пол: {sex}</p>
            <p id="rides">Количество поездок: {trip.driver.rides_amount}</p>
        </div>
    </div>
    <div class="maininfa">
        <a id="date" class="date">{trip.departure_date}<br></a>
        <a id="from" class="from">{trip.start_location}</a>
        <a class="strelka">&#8594;</a>
        <a id="to" class="to">{trip.end_location}<br></a>
        <a id="clari-from" class="clari-from">{trip.clarify_from}</a>
        <a id="time" class="time">{trip.departure_time}</a>
        <a id="clari-to" class="clari-to">{trip.clarify_to}</a>
    </div>
    <div class="options">
        <div id="pets">
            <a>Животные<br></a>
            <a id="z1">{trip.allow_pets?'✔':'✖'}</a>
        </div>
        <div id="kids">
            <a>Детское кресло<br></a>
            <a id="z2">{trip.has_child_seat?'✔':'✖'}</a>
        </div>
        <div id="minikids">
            <a>Бустер<br></a>
            <a id="z3">{trip.has_buster?'✔':'✖'}</a>
        </div>
        <div id="bag">
            <a>Багаж<br></a>
            <a id="z4">{trip.allow_luggage?'✔':'✖'}</a>
        </div>
    </div>
    <div id="car">
        <a id="mashina">Машина:</a>
        <a id="named">{trip.car.color} {trip.car.brand} {trip.car.number}</a>
    </div>
    <div id="info">
        <a>важная информация от водителя</a>
    </div>
    <br>
    <div id="ch+pr">
        <a id="price">Цена: {trip.price} руб</a>
        <button id="choose" on:click={window.Telegram.WebApp.close}>Выбрать</button>
    </div>
{:else}
    nothing
{/if}