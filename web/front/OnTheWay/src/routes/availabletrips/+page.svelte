<script lang="ts">
    import TripCard from "$lib/TripCard.svelte";
    import {myProfile} from "$lib/links";
    import type {Trip} from "$lib/Types";
    import {url} from "../../enviroment";

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
    <button id="filter" on:click={()=>{}}><img id="imgfilter" src="{url}/static/icons/filter-svgrepo-com.svg" alt="filter">Фильтр
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
        <img id="imgprof" src="{url}/static/icons/profile-1341-svgrepo-com.svg" alt="button">Мой профиль
    </button>
    <button id="history" on:click={()=>{}}>
        <img id="imghist" src="{url}/static/icons/travel-car-svgrepo-com.svg" alt="button">История поездок
    </button>
</footer>

<style>
    #zakrep {
        width: 100%;
        height: 11%;
        background-color: white;
        position: fixed;
        top: 0;
    }

    .scrolling {
        display: none;
        margin-bottom: 20%;
    }

    #filter {
        position: fixed;
        left: 70%;
        float: right;
        width: 25%;
        background-color: rgba(251, 234, 80, 0.85);
        color: black;
        border-radius: 10px;
        border: 0 black;
        font-size: 15px;
        font-family: Kreadon_medium;
        padding: 1% 1% 1% 5%;
        box-shadow: 1.5px 1.5px 2px rgb(0, 0, 0, 0.2);;

    }

    .tab {
        margin-top: 8%;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
    }

    .tab > input[type="radio"] {
        display: none;
    }

    .tab > label {
        display: block;
        padding: 2%;
        cursor: pointer;
        transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out;
        text-decoration: none;
        color: black;
        background: #E3E1E1;
        border-bottom: 1px solid black;
        text-align: center;

    }

    #drivers {
        width: 46%;
        float: left;
        border-top-right-radius: 1.2rem;
        margin-left: -2.5%;
    }

    #passengers {
        float: right;
        border-top-left-radius: 1.2rem;
        width: 46.5%;
    }

    .tab > input[type="radio"]:checked + label {
        cursor: default;
        color: black;
        background-color: white;
        border: 1px solid black;
        border-bottom: 0;
        box-shadow: inset 0 8px 10px rgba(0, 0, 0, 0.1);
    }

    #imgfilter {
        height: 25%;
        width: 25%;
        float: left;
        margin-right: 5%;
        margin-left: -12%;
    }

    #imghist {
        float: right;
        height: 40%;
        width: 40%;
        position: absolute;
        top: 35%;
        right: -5%;
    }

    #imgprof {
        float: right;
        height: 40%;
        width: 40%;
        position: absolute;
        top: 35%;
        right: 43%;
    }

    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        height: 15%;
        border-top-right-radius: 23%;
        box-shadow: 0 -3px 8px rgba(0, 0, 0, 0.3);
        background-color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-left: -2%;
        box-sizing: border-box;
    }

    footer button {
        width: 50%;
        height: 80%;
        font-family: "Kreadon_medium";
        font-size: 4.3vw;
        text-align: left;
        border-radius: 5vw;
        bottom: 0%;
        background-color: rgb(208, 206, 206, 90%);;
        margin: 1% 5%;
        color: black;
        padding-left: 3%;
        border: 0;
        box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.3);
    }

</style>