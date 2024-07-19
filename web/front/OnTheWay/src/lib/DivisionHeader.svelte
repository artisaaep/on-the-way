<script lang="ts">
    import {url} from "../enviroment.js";

    export let type: boolean = true;
    export let default_label: string;
    export let optional_label:string;
</script>

<div id="zakrep">
    <button id="filter" on:click={()=>{}}>
        <img id="imgfilter" src="{url}/static/icons/filter-svgrepo-com.svg" alt="filter">
        Фильтр
    </button>
    <div class="tab">
        <input
                id="tab-btn-1"
                name="tab-btn" type="radio"
                value={true}
                bind:group={type}
        />
        <label id="drivers" for="tab-btn-1">{default_label}</label>
        <input
                id="tab-btn-2"
                name="tab-btn"
                type="radio"
                value={false}
                bind:group={type}
                style=""
        />
        <label id="passengers" for="tab-btn-2">{optional_label}</label>
    </div>
</div>

<style>
    #zakrep {
        width: 100%;
        height: 11%;
        background-color: white;
        position: fixed;
        top: 0;
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

    .tab > input[type="radio"]:checked + label {
        cursor: default;
        color: black;
        background-color: white;
        border: 1px solid black;
        border-bottom: 0;
        box-shadow: inset 0 8px 10px rgba(0, 0, 0, 0.1);
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


    #imgfilter {
        height: 25%;
        width: 25%;
        float: left;
        margin-right: 5%;
        margin-left: -12%;
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
</style>