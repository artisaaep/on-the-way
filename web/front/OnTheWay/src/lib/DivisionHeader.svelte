<script lang="ts">
    import {url} from "../enviroment.js";
    import Filter from "$lib/Filter.svelte";
    import {Trip} from "$lib/Types";
    import './assets/DivisionHeader.css'

    export let type: boolean = true;
    export let default_label: string;
    export let optional_label: string;

    export let tripShowLeftCollection: Trip[];
    export let tripShowRightCollection: Trip[];

    export let destinationCollection: Trip[];

    $: destinationCollection = type ? tripShowLeftCollection : tripShowRightCollection;
</script>

<div id="zakrep">
    <Filter bind:tripShowCollection={destinationCollection}>
        <a id="filter">
            <img id="imgfilter" src="{url}/static/icons/filter-svgrepo-com.svg" alt="filter">
            Фильтр
        </a>
    </Filter>
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
