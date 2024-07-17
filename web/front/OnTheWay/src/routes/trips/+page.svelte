<script lang="ts">
    import FinishedTrip from "$lib/FinishedTrip.svelte";
    import {url} from "../../enviroment";
    import type {Trip} from "$lib/Types";
    import {onMount} from "svelte";
    let trips: Trip[];
    const fetcher = async () => {
        trips = await (await fetch(url + `/api/finished/${window.Telegram.WebApp.initDataUnsafe.user.id}`, {
            method: "GET",
        })).json();
        console.log(trips);
    };
    onMount(()=>{
        console.log("Mounted");
        fetcher();
    });
</script>
<div class="scrolling" id="main-scrolling-div" style="--owner-bg-col: red">
    {#if trips}
        {#each trips as trip}
            <FinishedTrip trip={trip}/>
        {/each}
    {:else}
        <p>Вы еще не совершили ни одну поедку.</p>
    {/if}
</div>

