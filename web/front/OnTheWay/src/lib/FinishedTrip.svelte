<script lang="ts">
    import type {Trip} from "./Types";
    import {url} from "../enviroment";
    import {goBack} from "$lib/links";

    export let trip: Trip;
</script>

<button id="back" on:click={goBack}>Назад</button>
<button id="hist" on:click={()=>{}}><img id="imghist" src="icons/travel-car-svgrepo-com.svg">История поездок</button>
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
    /*    @font-face { font-family: Kreadon_regular; src: url(fonts/Kreadon-Regular.ttf); } */
    /*@font-face { font-family: Kreadon_bold; src: url(fonts/Kreadon-Bold.ttf); } */
    /*@font-face { font-family: Kreadon_demi; src: url(fonts/Kreadon-Demi.ttf); } */
    /*@font-face { font-family: Kreadon_medium; src: url(fonts/Kreadon-Medium.ttf); }*/

    .arrow-right {
        width: 0;
        height: 0;
        border-top: 10px solid transparent;
        border-bottom: 10px solid transparent;
        border-left: 10px solid black;
    }

    #back {
        float: left;
        padding: 5px;
        width: 20%;
        background-color: #E3E1E1;
        color: black;
        border-radius: 10px;
        border: 1px solid black;
        border-color: black;
        font-size: 100%;
        font-family: Kreadon_regular;
    }

    #imghist {
        height: 13%;
        width: 13%;
        float: left;
        margin-right: 5%;
        margin-left: -20%;
    }

    #hist {
        float: right;
        padding: 5px;
        margin-left: 15px;
        width: 50%;
        background-color: #E3E1E1;
        color: black;
        border-radius: 10px;
        border: 1px solid black;
        border-color: black;
        font-size: 100%;
        font-family: Kreadon_regular;
        padding-left: 40px;
    }

    .card {
        padding: 2.5%;
        text-align: center;
        margin: auto;
        border: 0px;
        border-radius: 10px;
        width: 90%;
        background-color: #E3E1E1;
        min-height: 50%;
        box-shadow: 0px 3px 1cqmax rgba(0, 0, 0, 0.3);
        margin-top: 3%;
    }

    .avatar {
        width: 25%;
        height: 25%;
        border-radius: 50%;
        border: solid 0.5px black;
        float: left;
    }

    .name {
        font-family: Kreadon_demi;
        margin-left: 5%;
        font-size: 16px;
        background-color: rgba(251, 234, 80, 0.67);
        border: 0px;
        padding-left: 5%;
        padding-right: 5%;
        border-radius: 10px;
        padding-top: 0.5%;
        padding-bottom: 0.5%;
    }

    .maininfa {
        margin-top: 2%;
        width: 100%;
    }

    .date {
        font-family: Kreadon_medium;
        margin-left: 8%;
        font-size: 11px;
        width: 10%;
    }

    .from {
        font-family: Kreadon_demi;
        margin-left: 0%;
        font-size: 15px;

    }

    .strelka {
        font-family: Kreadon_demi;
        font-size: 15px;
        margin-left: 7%;

    }

    .to {
        font-family: Kreadon_demi;
        font-size: 15px;
        margin-left: 6%;
    }

    .clari-from {
        font-family: Kreadon_regular;
        margin-right: 1%;
        margin-left: 3%;
        font-size: 10px;
    }

    .time {
        font-family: Kreadon_medium;
        font-size: 11px;
        margin-left: 10%;
    }

    .clari-to {
        font-family: Kreadon_regular;
        font-size: 10px;
        margin-left: 10%;
    }

    .dopinfa {
        float: left;
        margin-top: -8%;
    }

    .rides {
        font-family: Kreadon_medium;
        font-size: 11px;
    }

    .free-places {
        font-family: Kreadon_medium;
        font-size: 11px;
    }

    .pr-ch {
        margin-top: 4%;
        margin-left: 40%;
    }

    .price {
        font-family: Kreadon_bold;
        font-size: 16px;
        width: 16%;
        padding-top: 10%;
        margin-right: 8%;
    }

    .choose {
        font-family: Kreadon_demi;
        font-size: 16px;
        border-radius: 10px;
        border: 0px;
        background-color: #CDCDCD;
        margin-left: 10%;
        padding: 3%;
        color: black;
    }

    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        height: 20%;
        border-top-right-radius: 15%;
        box-shadow: 0px -3px 8px rgba(0, 0, 0, 0.3);
        background-color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-left: -2%;
        box-sizing: border-box;
    }

    footer button {
        width: 33%;
        height: 78%;
        font-family: "Kreadon";
        font-size: 5vw;
        text-align: left;
        border-radius: 5vw;
        border-color: #000;
        bottom: 0%;
        margin-top: 4%;
        margin-left: 5%;
        margin-right: 5%;
        background-color: #D0CECE;
        margin-bottom: 3%;
        padding-top: 10%;
        color: black;
    }

</style>