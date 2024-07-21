<script lang="ts">
    import {onMount} from "svelte";
    import {Trip} from "$lib/Types";
    import "./enhancedTrip.css"
    import {url} from "../../enviroment";

    function formatDate(date: Date): string {
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${day}-${month}-${year}`;
    }


    let trip: Trip;
    let sex: string;
    let photo: string;

    async function main() {
        let BackButton = window.Telegram.WebApp.BackButton;
        BackButton.show();
        BackButton.onClick(function () {
            window.history.back();
            BackButton.hide();
        });
        let trip_id = window.location.href.split('?')[1];
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
    <div class="main-info">
        <div class="from_main">
            <p class="from">{trip.start_location}</p>
            <p class="clari-from">{trip.clarify_from}</p>
        </div>
        <div class="bott">
            <p class="date">{formatDate(new Date(trip.departure_date))}</p>
            <p class="arrow">&#8594;</p>
            <p class="time">{trip.departure_time}</p>
        </div>
        <div class="to_main">
            <p class="to">{trip.end_location}</p>
            <p class="clari-to">{trip.clarify_to}</p>
        </div>
    </div>
    <div class="options">
        <div id="pets">
            <a>Животные<br></a>
            <a id="z1">{trip.allow_pets?'✔️':'✖️'}</a>
        </div>
        <div id="kids">
            <a>Детское кресло<br></a>
            <a id="z2">{trip.has_child_seat?'✔️':'✖️'}</a>
        </div>
        <div id="minikids">
            <a>Бустер<br></a>
            <a id="z3">{trip.has_buster?'✔️':'✖️'}</a>
        </div>
        <div id="bag">
            <a>Багаж<br></a>
            <a id="z4">{trip.allow_luggage?'✔️':'✖️'}</a>
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
    <div id="pr">
        <a id="price">Цена: {trip.price} руб</a>
    </div>
{:else}
    nothing
{/if}
