<script lang="ts">
    import TripCard from "$lib/TripCard.svelte";
    import type {Trip} from "$lib/Types";
    import {url} from "../../enviroment";
    import './availableTrips.css';
    import {onMount} from "svelte";
    import DivisionHeader from "$lib/DivisionHeader.svelte";

    let trips: Trip[] = [];
    let tripsToShow: Trip[] = [];
    let driversTrips: Trip = [];
    let ridersTrips:Trip = []
    const fetcher = async () => {
        trips = [...trips, ...await (await fetch(url + "/api/trips", {
            method: "GET",
        })).json()];
        console.log(trips);
        driversTrips = trips.filter((trip: Trip) => !trip.is_request);
        ridersTrips = trips.filter((trip: Trip) => trip.is_request);
        tripsToShow = [...driversTrips];
    };
    onMount(fetcher)

    let type: boolean = true;
    $: name_color = type ? "#fbea50ab" : "#d0cecee6";
</script>
{#key type}
    <DivisionHeader bind:type={type}
                    bind:tripShowLeftCollection={driversTrips}
                    bind:tripShowRightCollection={ridersTrips}
                    bind:destinationCollection={tripsToShow}
                    default_label="Заявки водителей"
                    optional_label="Заявки пассажиров"/>
{/key}
<br><br>
<div class="scrolling" id="main-scrolling-div" style="--owner-bg-col: {name_color}">
    <br>
    {#key tripsToShow}
        {#if tripsToShow && tripsToShow.length!==0}
            {#each tripsToShow as trip}
                <TripCard trip={trip}/>
            {/each}
        {:else}
            <p>Доступных поездок нет</p>
        {/if}
    {/key}
</div>


<footer class="footer">
    <button id="My-profile" on:click={()=>{window.location.href = 'profile.html';}}>
        <img id="imgprof" src="{url}/static/icons/profile-1341-svgrepo-com.svg" alt="button">
        Мой <br> профиль
    </button>
    <button id="history" on:click={()=>{window.location.href = 'history.html';}}>
        <img id="imghist" src="{url}/static/icons/travel-car-svgrepo-com.svg" alt="button">
        История <br> поездок
    </button>
</footer>
