<script lang="ts">
    import {data, step} from "../Common";
    import {url} from "../../../enviroment";

    async function checkCar() {

        const ownRadio = document.getElementById('own') as HTMLInputElement;
        const carshRadio = document.getElementById('carsh') as HTMLInputElement;
        const taxiRadio = document.getElementById('taxi') as HTMLInputElement;

        if (ownRadio.checked) {
            data.kind = "На своей машине";
        } else if (carshRadio.checked) {
            data.kind = "Каршеринг";
        } else if (taxiRadio.checked) {
            data.kind = "Такси";
        }
    }
    let carType: string;
    $: if (carType === "taxi") {
        data.car_id = 0;
    } else if (carType === "taxi") {
        data.car_id = 1;
    }

</script>
{#if data.is_request === false}
<img src="{url}/static/images/ruble-svgrepo-com.svg" class="date-img" alt="calendar">
<div class="grey-rect">
    <p class="dir-desc">Вид и цена поездки</p>
    <div class="type">
        <ul class="choice">
            <li>
                <label for="own">
                    <input bind:group={carType} type="radio" id="own" name="r" value="own">
                    <div class="checkbox__checkmark"></div>
                    На своей машине
                </label>
            </li>
            <li>
                <label for="carsh">
                    <input bind:group={carType} type="radio" id="carsh" name="r" value="carsh">
                    <div class="checkbox__checkmark"></div>
                    Каршеринг
                </label>
            </li>
            <li>
                <label for="taxi">
                    <input bind:group={carType} type="radio" id="taxi" name="r" value="taxi">
                    <div class="checkbox__checkmark"></div>
                    Совместное такси
                </label>
            </li>
        </ul>
    </div>

    <div class="price">
        <p class="choose-price">Цена в рублях:</p>
        <input type="number" id="price-rub" step="50" min="0" bind:value={data.price}>
    </div>

<!--    TODO: this    -->
    <div class="av-text">
        Свободных мест
        <input type="number" list="places" step="1" min="1" max="4" id="av" class="number-input" bind:value={data.available_seats}/>
        <datalist id="places">
            <option value="1">
            <option value="2">
            <option value="3">
            <option value="4">
        </datalist>
    </div>
</div>
{:else}
<div class="grey-rect">
<div class="av-text" id="av-pl-pass">
    Сколько свободных мест нужно?
    <input type="number" list="places" step="1" min="1" max="4" id="av" class="number-input" bind:value={data.available_seats}/>
    <datalist id="places">
        <option value="1">
        <option value="2">
        <option value="3">
        <option value="4">
    </datalist>
</div>
</div>
{/if}
<!--    endTODO   -->

    

<div class="nav-buttons">
    <button class="next" on:click={() => { checkCar(); $step-- }}>Назад</button>
<!--        TODO: validation over vehicle choice       -->
    <button class="next" on:click={() => { checkCar(); (data.kind === "На своей машине") ? $step++ : $step += 2 }}>Далее</button>
</div>
