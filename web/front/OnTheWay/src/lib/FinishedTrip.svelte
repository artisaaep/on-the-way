<script lang="ts">
    import type {Trip} from "./Types";
    import {url} from "../enviroment";
    import './FinishedTrip.css';

    export let trip: Trip;
</script>

<button id="back" on:click={()=>{window.history.back();}}>Назад</button>
<button id="hist" on:click={()=>{}}>
    <img id="imghist" src="{url}/static/icons/travel-car-svgrepo-com.svg" alt="hzchto">
    История поездок
</button>
<br><br>
<div class="finished_trips">
    <div class="card">
        <a class="name">{trip.driver.name}</a>
        <div class="maininfa">
            <a class="date">{trip.departure_date}<br></a>
            <a class="from">{trip.start_location}</a>
            <a class="strelka">&#8594;</a>
            <a class="to">{trip.end_location}<br></a>
            <a class="clari-from">{trip.clarify_from}</a>
            <a class="time">{trip.departure_time}</a>
            <a class="clari-to">{trip.clarify_to}</a>
        </div>
        <div class="pr-ch">
            <a class="price">{trip.price}</a>
        </div>
        <div class="dopinfa">
            <a class="free-places">Занятых мест: 3</a>
        </div>
    </div>
</div>

<style>


</style>