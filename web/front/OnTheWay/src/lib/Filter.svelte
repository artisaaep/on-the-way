<script lang="ts">
    import {url} from '../enviroment'
    import Modal from "$lib/modal/Modal.svelte";
    import {Filter, Trip} from "$lib/Types";
    import "./assets/Filter.css"

    const filterDefault: Filter = {
        allow_luggage: false,
        allow_pets: false,
        child_seat: false,
        booster: false,
        seats: 0,
        date: null,
        from: null,
    };

    let filter: Filter = {...filterDefault};
    export let tripShowCollection: Trip[];
    const initialCollection: Trip[] = [...tripShowCollection]

    let modalOpen = false;

    function applyFilter() {
        tripShowCollection = tripShowCollection.filter((trip: Trip) => {
                return [
                    trip.has_buster >= filter.booster,
                    trip.allow_pets >= filter.allow_pets,
                    trip.has_child_seat >= filter.child_seat,
                    trip.allow_luggage >= filter.allow_luggage,
                    trip.available_seats >= filter.seats,
                    filter.date ? trip.departure_date === filter.date : true,
                    filter.from ? trip.start_location === filter.from : true,
                ].every((i) => i)
            }
        );
        console.log(tripShowCollection);
    }
</script>
<Modal bind:isOpen={modalOpen}>
    <div slot="content" class="filter-inner-thing">
        <div class="filter-header-high">
            <div class="filterBorder">
                <p id="FilterBorder">
                    <img id="inner-img-filter" src="{url}/static/icons/filter-svgrepo-com.svg" alt="filter">
                    Фильтр
                </p>

            </div>
            <button class="filter-drop-button"
                    on:click={()=>{
                        filter = {...filterDefault};
                        tripShowCollection=[...initialCollection];
                        modalOpen=false;}}>
                Сбросить
            </button>
        </div>
        <div class="filterBody">
            <div class="roundedSection1">
                <button
                        class="leftButton"
                        on:click={()=>{filter.from = 'Иннополис'}}
                        style="background-color: {filter.from==='Иннополис'? '#969696' : ''}"
                >
                    <img src="{url}/static/images/location-pin-alt-svgrepo-com.svg" class="leftIcon" alt="Left Icon">
                    <br>
                    <span class="leftButtonText">Из Иннополиса</span>
                </button>
                <button
                        class="rightButton"
                        on:click={()=>{filter.from = 'Казань'}}
                        style="background-color: {filter.from==='Казань'? '#969696' : ''}"
                >
                    <img src="{url}/static/images/location-xmark-svgrepo-com.svg" class="rightIcon" alt="Right Icon">
                    <br>
                    <span class="rightButtonText">Из Казани</span>
                </button>
            </div>


            <div class="roundedSection2">
                <button class="leftButton" style="background-color: {filter.date ? '#969696' : ''}">
                    <img src="{url}/static/images/date-range-svgrepo-com.svg" class="leftIcon2" alt="Left Icon 2">
                    <br>
                    <span class="leftButtonText2">
                        Дата <br> поездки
                    </span>
                </button>
                <button class="rightButton2">
                    <input class="rightButtonText2" type="date" bind:value={filter.date}>
                </button>
            </div>


            <div class="roundedSection3">
                <div class="additionalSection">
                    <p class="additionalTitle">Дополнительно</p>
                    <hr class="separator">
                    <ul class="additionalList">
                        <li>
                            <label for="check1">Поеду с багажом</label>
                            <input type="checkbox" id="check1" bind:checked={filter.allow_luggage}>
                        </li>
                        <li>
                            <label for="check1">Поеду с животным</label>
                            <input type="checkbox" id="check1" bind:checked={filter.allow_pets}>
                        </li>
                        <li>
                            <label for="check1">Необходимо детское кресло</label>
                            <input type="checkbox" id="check1" bind:checked={filter.child_seat}>
                        </li>
                        <li>
                            <label for="check1">Необходим бустер</label>
                            <input type="checkbox" id="check1" bind:checked={filter.booster}>
                        </li>
                        <li>
                            Сколько требуется мест
                            <input id="check1"
                                   type="number"
                                   step="1"
                                   min="0"
                                   max="4"
                                   class="number-input"
                                   bind:value={filter.seats}/>
                        </li>
                    </ul>
                </div>
            </div>

            <button id="find" on:click={()=>{modalOpen=false; applyFilter()}}>Поиск</button>
        </div>
    </div>

    <slot slot="trigger"/>
</Modal>
<style>

</style>