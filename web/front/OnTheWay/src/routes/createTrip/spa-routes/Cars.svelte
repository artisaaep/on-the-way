<script lang="ts">
    import {url} from "../../../enviroment";
    import AddCar from "$lib/AddCar.svelte";
    import {data, step} from "../Common";
    import {Car} from "$lib/Types";
    import {onMount} from "svelte";
    import {carFetcher, userFetcher} from "$lib/fetchers";

    let cars: Car[] = [];
    onMount(() => {
        carFetcher(cars, userFetcher());
        cars = [...cars];
    })

    let currentCar: string | undefined = undefined;

    $: data.car_id = currentCar ? +currentCar : undefined;

    function validateCarChoice(): boolean {
        if (!currentCar) {
            window.Telegram.WebApp.showAlert("Вы не выбрали машину");
            return false;
        }
        return true;
    }
</script>

<img src="{url}/static/images/travel-car-svgrepo-com.svg" class="car-img" alt="little-car">
<div class="grey-rect">
    <div class="desc-img">
        <p class="dir-desc">Выберите машину</p>
    </div>
    <div class="car">
        {#if cars}
            <ul class="choice" id="carchoice">
                <!--TODO: this is (each block) not work properly for unknown reason-->
                {#each cars as car}
                    <li>
                        <label for="car-${car.id}">
                            <input bind:group={currentCar} type="radio" id="car-${car.id}" name="c" value="{car.id}">
                            <div class="checkbox__checkmark"></div>
                            {car.color} {car.brand}, {car.number}
                        </label>
                    </li>
                {/each}
            </ul>
        {:else}
            <p id="no-cars">У вас пока нет машин.</p>
        {/if}
    </div>

    <AddCar>
        <u id="addcar">Добавить машину</u>
    </AddCar>
    
</div>
<div class="nav-buttons">
    <button class="next" on:click={()=>{$step--}}>Назад</button>
    <button class="next" on:click={()=>{if (validateCarChoice()) {$step++}}}>Далее</button>
</div>
