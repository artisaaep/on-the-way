<script lang="ts">
    import type {Trip} from "./Types";
    import {url} from "../enviroment";
    import './TripCard.css';

    export let trip: Trip;

    let isAttached_: boolean =
        trip.passengers
            .map(passenger => passenger.id)
            .includes(window.Telegram.WebApp.initDataUnsafe.user.id as number);

    async function apply(trip_id: number) {
        await fetch(url + "/api/mediator/await_submission?riderId=" + window.Telegram.WebApp.initDataUnsafe.user.id + "&driverId=" + trip.driver.id, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "has_luggage": false,
                "has_kids": false,
                "has_pets": false
            })
        });
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
<div class="centre">
    <div class="card">
        <div class="verh">
            <img class="avatar" alt="driver-avatar" src="{url}/api/users/{trip.driver.id}/photo">
            <div class="verhtext">
                <p class="owner_name">{trip.driver.name}</p>
                <div class="main-info">
                    <div class="from_main">
                        <p class="from">{trip.start_location}</p>
                        <p class="clari-from">{trip.clarify_from}</p>
                    </div>
                    <div class="bott">
                        <p class="date">{trip.departure_date}</p>
                        <p class="arrow">&#8594;</p>
                        <p class="time">{trip.departure_time}</p>
                    </div>
                    <div class="to_main">
                        <p class="to">{trip.end_location}</p>
                        <p class="clari-to">{trip.clarify_to}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="niz">
            <div class="additional-info">
                <p class="rides">Поездок: {trip.driver.rides_amount} </p>
                <p class="free-places">Свободных мест: {trip.available_seats}</p>
            </div>
            <div class="pr-ch">
                <p class="price">{trip.price} руб.</p>
                {#if isAttached_}
                    <button class="choose" on:click={() => reject(trip.id)} id="choose-not-ok-{trip.id}">Отменить</button>
                {:else}
                    <button class="choose" on:click={() => apply(trip.id)} id="choose-ok-{trip.id}">Выбрать</button>
                {/if}
            </div>
        </div>
    </div>
</div>
