<script lang="ts">
    import TripCard from "$lib/TripCard.svelte";
    import type {Trip} from "$lib/Types";
    import {url} from "../../enviroment";
    import './availableTrips.css';
    import { onMount } from 'svelte';
    import DivisionHeader from "$lib/DivisionHeader.svelte";


    let trips: Trip[] = [];
    let tripsToShow: Trip[] = [];
    let driversTrips: Trip = [];
    let ridersTrips: Trip = [];
    let appliedTrips: Trip[] = [];


    async function filterTripsSideEffect(): Promise<void> {
        let hrs = Number(new Date().toLocaleTimeString().split(':')[0]);
        let min = Number(new Date().toLocaleTimeString().split(':')[1]);
        let day = Number(new Date().toLocaleDateString().split('/')[0]);
        let mon = Number(new Date().toLocaleDateString().split('/')[1]);
        {
            let toDelete: number[] = [];
            for (let trip of trips) {
                let tripHrs = Number(trip.departure_time.split("-")[1].split(':')[0]);
                let tripmin = Number(trip.departure_time.split("-")[1].split(':')[1]);
                let tripday = Number(trip.departure_date.split("-")[0]);
                let tripmon = Number(trip.departure_date.split("-")[1]);
                let cond1 = day > tripday && mon == tripmon || mon > tripmon;
                let cond2 = day == tripday && mon == tripmon && (hrs > tripHrs || min > tripmin && hrs == tripHrs);
                if (cond1 || cond2) {
                    await fetch(`${url}/api/trips/` + trip.id, {
                        method: "DELETE",
                        headers: {
                            "Content-Type": "application/json"
                        }
                    })
                    toDelete.push(trip.id)
                }
            }
            trips = trips.filter(trip => {
                return !toDelete.includes(trip.id)
            })
        }
    }


    async function fetcher() {
        trips = [...trips, ...await (await fetch(url + "/api/trips", {
            method: "GET",
        })).json()];
        await filterTripsSideEffect();
        driversTrips = trips.filter((trip: Trip) => !trip.is_request);
        ridersTrips = trips.filter((trip: Trip) => trip.is_request);
        appliedTrips = [
            ...appliedTrips,
            ...await (await fetch(`${url}/api/trips/awaited/${window.Telegram.WebApp.initDataUnsafe.user.id}`, {
                method: "GET",
            })).json()
        ];
    }


    onMount(() => {
        fetcher();
        window.Telegram.WebApp.expand();
    })

    let type: boolean = true;
    $: name_color = type ? "#fbea50ab" : "#d0cecee6";
</script>
{#key trips}
    {#key type}
        <DivisionHeader bind:type={type}
                        bind:tripShowLeftCollection={driversTrips}
                        bind:tripShowRightCollection={ridersTrips}
                        bind:destinationCollection={tripsToShow}
                        default_label="Заявки водителей"
                        optional_label="Заявки пассажиров"/>
    {/key}
{/key}
<br><br>
<div class="scrolling" id="main-scrolling-div" style="--owner-bg-col: {name_color}">
    <br>
    {#key tripsToShow}
        {#if tripsToShow && tripsToShow.length !== 0}
            {#each tripsToShow as trip}
                {#key appliedTrips}
                    <TripCard trip={trip} appliedTrips={appliedTrips}/>
                {/key}
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
