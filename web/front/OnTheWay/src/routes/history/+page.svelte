<script lang="ts">
    import FinishedTrip from "$lib/FinishedTrip.svelte";
    import {url} from "../../enviroment";
    import type {Trip} from "$lib/Types";
    import {onMount} from "svelte";
    import DivisionHeader from "$lib/DivisionHeader.svelte";

    let ownTrips: Trip[] = [];
    let participatedTrips: Trip[] = [];
    let type: boolean = true;
    onMount(async () => {
            ownTrips = await (await fetch(`${url}/api/finished/driver/${window.Telegram.WebApp.initDataUnsafe.user.id}`, {
                method: "GET",
            })).json();
            participatedTrips = await (await fetch(`${url}/api/finished/rider/${window.Telegram.WebApp.initDataUnsafe.user.id}`, {
                method: "GET"
            })).json();
        }
    );
    let tripsToShow: Trip[] = [];
</script>
{#key type}
    <DivisionHeader
            bind:type={type}
            bind:tripShowLeftCollection={ownTrips}
            bind:tripShowRightCollection={participatedTrips}

            default_label="Мои заявки"
            optional_label="Мои отклики"/>
    <div class="scrolling" id="main-scrolling-div" style="--owner-bg-col: red">
        {#if tripsToShow}
            {#each tripsToShow as trip}
                <FinishedTrip trip={trip}/>
            {/each}
        {:else}
            <p>Вы еще не совершили ни одну поедку.</p>
        {/if}
    </div>
{/key}
