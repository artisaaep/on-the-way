<script lang="ts">
    import type {Trip} from "./Types";
    import {url} from "../enviroment";
    import './assets/FinishedTrip.css';

    export let trip: Trip;

    function formatDate(date: Date): string {
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${day}-${month}-${year}`;
    }
</script>

<div class="finished_trips">
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
                        <p class="date">{formatDate(new Date(trip.departure_date))}</p>
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
                <p class="free-places">Занятых мест: {trip.available_seats}</p>
            </div>
            <div class="pr-ch">
                <p class="price">{trip.price} руб.</p>
            </div>
        </div>
    </div>
</div>

<style>


</style>