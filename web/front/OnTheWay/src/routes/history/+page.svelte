<script lang="ts">
    import FinishedTrip from "$lib/FinishedTrip.svelte";
    import {url} from "../../enviroment";
    import type {Trip} from "$lib/Types";
    import {onMount} from "svelte";
    import DivisionHeader from "$lib/DivisionHeader.svelte";

    let own_trips: Trip[];
    let participated_trips: Trip[];
    let type: boolean = true;
    onMount(async () => {
            own_trips = await (await fetch(`${url}/api/finished/driver/${window.Telegram.WebApp.initDataUnsafe.user.id}`, {
                method: "GET",
            })).json();
            participated_trips = await (await fetch(`${url}/api/finished/rider/${window.Telegram.WebApp.initDataUnsafe.user.id}`, {
                method: "GET"
            })).json();
        }
    );
</script>
<br><br><br>
{#key type}
    <DivisionHeader bind:type={type} default_label="Мои заявки" optional_label="Мои отклики"/>
    <div class="scrolling" id="main-scrolling-div" style="--owner-bg-col: red">
        {#if type}
            {#if own_trips}
                {#each own_trips as trip}
                    <FinishedTrip trip={trip}/>
                {/each}
            {:else}
                <p>Вы еще не совершили ни одну поедку.</p>
            {/if}
        {:else}
            {#if participated_trips}
                {#each participated_trips as trip}
                    <FinishedTrip trip={trip}/>
                {/each}
            {:else}
                <p>Вы еще не учавствовали ни в одной поедке.</p>
            {/if}
        {/if}
    </div>
{/key}
