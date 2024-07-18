<script lang="ts">
    import TripCard from "$lib/TripCard.svelte";
    import {myProfile} from "$lib/links";
    import type {Trip} from "$lib/Types";
    import {url} from "../../enviroment";
    import './availableTrips.css';

    let trips: Trip[];
    const fetcher = async () => {
        trips = await (await fetch(url + "/api/trips", {
            method: "GET",
        })).json();
    };
    fetcher()

    let type: boolean = false;
    let name_color: string = type ? "#fbea50ab" : "#d0cecee6";
</script>
<div id="zakrep">
    <button id="filter" on:click={()=>{}}>
        <img id="imgfilter" src="{url}/static/icons/filter-svgrepo-com.svg" alt="filter">
        Фильтр
    </button>
    <div class="tab">
        <input
                checked id="tab-btn-1"
                name="tab-btn" type="radio"
                value=""
                on:click={()=>{type = true}}
        />
        <label id="drivers" for="tab-btn-1">Заявки водителей</label>
        <input
                id="tab-btn-2"
                name="tab-btn"
                type="radio"
                value=""
                on:click={()=>{type = false}}
                style=""
        />
        <label id="passengers" for="tab-btn-2">Заявки пассажиров</label>
    </div>
</div>
<br><br>
<div class="scrolling" id="main-scrolling-div" style="--owner-bg-col: {name_color}">
    {#if trips}
        {#each trips as trip}
            {#if trip.is_request === type}
                <TripCard trip={trip}/>
            {/if}
        {/each}
    {:else}
        <p>Доступных поездок нет</p>
    {/if}
</div>


<footer class="footer">
    <button id="My-profile" on:click={myProfile}>
        <img id="imgprof" src="{url}/static/icons/profile-1341-svgrepo-com.svg" alt="button">Мой <br> профиль
    </button>
    <button id="history" on:click={()=>{}}>
        <img id="imghist" src="{url}/static/icons/travel-car-svgrepo-com.svg" alt="button">История <br> поездок
    </button>
</footer>
