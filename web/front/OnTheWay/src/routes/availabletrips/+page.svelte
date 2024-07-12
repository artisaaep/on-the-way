<script lang="ts">
    import TripCard from "$lib/TripCard.svelte";
    import {myProfile} from "$lib/links";
    import type {Trip} from "$lib/Types";

   
    let trips: Trip[];
    const fetcher = async () => {
        trips = await (await fetch(url + "/api/trips", {
            method: "GET",
        })).json();
    };
    fetcher()


</script>
<body>
<div id="zakrep">
    <button id="filter" on:click={()=>{}}><img id="imgfilter" src="icons/filter-svgrepo-com.svg" alt="filter">Фильтр
    </button>
</div>
<br><br>
<div class="scrolling" id="main-scrolling-div">
    {#each trips as trip}
        <TripCard trip={trip}/>
    {/each}
</div>


<footer class="footer">
    <button id="My-profile" on:click={myProfile}>
        <img id="imgprof" src="icons/profile-1341-svgrepo-com.svg" alt="button">
        Мой профиль
    </button>
    <button id="history" on:click={()=>{}}>
        <img id="imghist" src="./icons/travel-car-svgrepo-com.svg" alt="button">История
        поездок
    </button>
</footer>
</body>
