<script lang="ts">
    import {data, step} from "../Common";
    import {url} from "../../../enviroment";

    let carType: string;
    $: if (carType === "taxi") {
        data.car_id = 0;
    } else if (carType === "carsh") {
        data.car_id = 1;
    }

</script>
<img src="{url}/static/images/ruble-svgrepo-com.svg" class="date-img" alt="calendar">
<div class="grey-rect">
    {#if data.is_request === false}
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
    {/if}
    <div class="grey-rect">
        <div class="av-text">
            Сколько свободных мест нужно?
            <input type="number" list="places" step="1" min="1" max="4" id="av" class="number-input"
                   bind:value={data.available_seats}/>
            <datalist id="places">
                <option value="1">
                <option value="2">
                <option value="3">
                <option value="4">
            </datalist>
        </div>
    </div>
</div>


<div class="nav-buttons">
    <button class="next" on:click={() => { $step-- }}>Назад</button>
    <!--        TODO: validation over vehicle choice       -->
    <button class="next" on:click={() => { (data.car_id!==0 && data.car_id!==1) ? $step++ : $step += 2; console.log(data) }}>Далее</button>
</div>
