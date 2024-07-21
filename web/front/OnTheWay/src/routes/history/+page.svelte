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
            tripsToShow = [...ownTrips]
            let BackButton = window.Telegram.WebApp.BackButton;
            BackButton.show();
            BackButton.onClick(function () {
                window.history.back();
                BackButton.hide();
            });
        }
    );
    let tripsToShow: Trip[] = [];
    $: name_color = type ? "#fbea50ab" : "#d0cecee6";
</script>
<br><br><br>
{#key type}
    <DivisionHeader
            bind:type={type}
            bind:tripShowLeftCollection={ownTrips}
            bind:tripShowRightCollection={participatedTrips}
            bind:destinationCollection={tripsToShow}

            default_label="Мои заявки"
            optional_label="Мои отклики"/>
    <div class="scrolling" id="main-scrolling-div" style="--owner-bg-col: {name_color}">
        {#if tripsToShow && tripsToShow.length !== 0}
            {#each tripsToShow as trip}
                <FinishedTrip trip={trip}/>
            {/each}
        {:else}
            <p>Вы еще не совершили ни одну поедку.</p>
        {/if}
    </div>
{/key}
