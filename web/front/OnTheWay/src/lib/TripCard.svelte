<script lang="ts">
    import type {Trip} from "./Types";
    import {url} from "../enviroment";

    export let trip: Trip;

    let isAttached_: boolean =
        trip.passengers
            .map(passenger => passenger.id)
            .includes(window.Telegram.WebApp.initDataUnsafe.user.id as number);

    async function apply(trip_id: number) {
        let response = await fetch(url + "/api/trips/" + trip_id + "/rider?riderID=" + window.Telegram.WebApp.initDataUnsafe.user.id, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "has_luggage": false,
                "has_kids": false,
                "has_pets": false
            })
        });
        if (response.ok) {
            isAttached_ = true;
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    }

    async function reject(trip_id: number) {
        let response = await fetch(url + "/api/trips/" + trip_id + "/rider?riderID=" + window.Telegram.WebApp.initDataUnsafe.user.id, {
            method: "DELETE",
        });
        if (response.ok) {
            isAttached_ = false;
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    }
</script>

<div class="card">
    <img class="avatar" alt="driver-avatar" src="{url}/api/users/${trip.driver.id}/photo">
    <p class="owner_name">{trip.driver.name}</p>
    <div class="main-info">
        <div class="from_main">
            <p class="from">{trip.start_location}</p><br>
            <p class="clari-from">{trip.clarify_from}</p>
        </div>
        <div class="bott">
            <p class="date">{trip.departure_date}<br></p>
            <p class="arrow">&#8594;</p><br>
            <p class="time">{trip.departure_time}</p>
        </div>
        <div class="to_main">
            <p class="to"><br>{trip.end_location}</p><br>
            <p class="clari-to">{trip.clarify_to}</p>
        </div>
    </div>
    <div class="pr-ch">
        <p class="price">{trip.price} руб.</p>
        {#if isAttached_}
            <button class="choose" on:click={() => reject(trip.id)} id="choose-{trip.id}">Отменить</button>
        {:else}
            <button class="choose" on:click={() => apply(trip.id)} id="choose-{trip.id}">Выбрать</button>
        {/if}
    </div>
    <div class="additional-info">
        <p class="rides">Поездок: {trip.driver.rides_amount} <br></p>
        <p class="free-places">Свободных мест: {trip.available_seats}</p>
    </div>
</div>

<style>
    .card {
        padding: 2.5%;
        text-align: center;
        border: 0;
        border-radius: 10px;
        width: 90%;
        background-color: #E3E1E1;
        min-height: 50%;
        box-shadow: 0 3px 1cqmax rgba(0, 0, 0, 0.3);
        margin: 3% auto auto;
    }

    .avatar {
        width: 5em;
        height: 5em;
        object-fit: cover;
        border-radius: 50%;
        border: solid 0.1px black;
        float: left;
    }

    .owner_name {
        font-family: Kreadon_demi;
        margin-left: 5%;
        font-size: 16px;
        background-color: var(--owner-bg-col);
        border: 0;
        border-radius: 10px;
        padding: 0.5% 5%;
    }

    .main-info {
        padding-top: 10%;
        margin-top: 10%;
        width: 100%;

    }

    .from_main {
        width: 35%;
        float: left;
        align-items: center;
        text-align: center;
        margin-top: 6%;
    }

    .date {
        font-family: Kreadon_medium;
        font-size: 11px;
        width: 10%;
    }

    .from {
        font-family: Kreadon_demi;
        margin-left: 0%;
        font-size: 15px;

    }

    .arrow {
        font-family: Kreadon_demi;
        font-size: 15px;

    }

    .to_main {
        width: 35%;
        float: right;
        align-items: center;
        text-align: center;
        margin-top: -17%;
        margin-right: -6%;
    }

    .to {
        font-family: Kreadon_demi;
        font-size: 15px;
    }

    .bott {
        width: 20%;
        float: left;
        align-items: center;
        text-align: center;
        margin-top: 1%;
        margin-left: -4%;

    }

    .clari-from {
        font-family: Kreadon_regular;
        font-size: 10px;

    }

    .time {
        font-family: Kreadon_medium;
        font-size: 11px;
        padding-top: 5%;

    }

    .clari-to {
        font-family: Kreadon_regular;
        font-size: 10px;
        margin-top: 10%;
    }

    .additional-info {
        float: left;
        margin-top: -8.5%;

    }

    .rides {
        font-family: Kreadon_medium;
        font-size: 11px;
    }

    .free-places {
        font-family: Kreadon_medium;
        font-size: 11px;
    }

</style>