<script lang="ts">
    import type {Trip} from "./Types";
    import {url} from "../enviroment";
    import './TripCard.css';

    export let trip: Trip;
    export let isSubmitted: boolean;

    let isApproved: boolean =
        trip.passengers
            .map(passenger => passenger.id)
            .includes(window.Telegram.WebApp.initDataUnsafe.user.id as number);

    // 0 - can apply
    // 1 - await for submission
    // 2 - participate
    $: type = isApproved ? 2 : isSubmitted ? 1 : 0;

    async function awaitSubmission(trip_id: number) {
        let params: URLSearchParams = new URLSearchParams();
        params.append("riderId", window.Telegram.WebApp.initDataUnsafe.user.id.toString())
        params.append("tripId", trip.id.toString())
        let response = await fetch(url + "/api/mediator/await_submission?" + params, {
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
        if (response.ok) {
            isSubmitted = true;
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    }

    async function rejectApplication(trip_id: number) {
        let params: URLSearchParams = new URLSearchParams();
        params.append("riderId", window.Telegram.WebApp.initDataUnsafe.user.id.toString())
        params.append("tripId", trip.id.toString())
        let response = await fetch(url + "/api/mediator/await_submission?" + params, {
            method: 'DELETE'
        });
        if (response.ok) {
            isApproved = false;
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    }

    async function rejectSubmission(trip_id: number) {
        let response = await fetch(url + "/api/trips/" + trip_id + "/rider?riderID=" + window.Telegram.WebApp.initDataUnsafe.user.id, {
            method: "DELETE",
        });
        if (response.ok) {
            isApproved = false;
            isSubmitted = false;
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    }
</script>

<div class="card">
    <img class="avatar" alt="driver-avatar" src="{url}/api/users/{trip.driver.id}/photo">
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
    <div class="pr-ch">
        <p class="price">{trip.price} руб.</p>
        {#if type === 2}
            <button class="choose"
                    on:click={() => rejectSubmission(trip.id)}
                    id="choose-rej-ok-{trip.id}"
                    style="background-color: #991B1BFF">
                Отказаться
            </button>
        {:else if type === 1}
            <button class="choose"
                    on:click={() => rejectApplication(trip.id)}
                    id="choose-not-ok-{trip.id}">
                Отменить
            </button>
        {:else}
            <button class="choose"
                    on:click={() => awaitSubmission(trip.id)}
                    id="choose-ok-{trip.id}">
                Выбрать
            </button>
        {/if}
    </div>
    <div class="additional-info">
        <p class="rides">Поездок: {trip.driver.rides_amount} </p>
        <p class="free-places">Свободных мест: {trip.available_seats}</p>
    </div>
</div>
