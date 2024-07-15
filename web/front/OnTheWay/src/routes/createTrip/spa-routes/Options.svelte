<script lang="ts">
    import {data, step} from "../Common";
    import {url} from "../../../enviroment";

    let isOwnCar: boolean;
</script>
<img src="{url}/static/images/ruble-svgrepo-com.svg" class="date-img" alt="calendar">
<div class="grey-rect">
    <div class="desc-img">
        <p class="dir-desc">Вид и цена поездки</p>
    </div>
    <div class="type">
        <ul class="choice">
            <li>
                <label for="own">
                    <input type="radio" id="own" name="r">
                    <div class="checkbox__checkmark"></div>
                    На своей машине
                </label>
            </li>
            <li>
                <label for="carsh">
                    <input type="radio" id="carsh" name="r">
                    Каршеринг
                </label>
            </li>
            <li>
                <label for="taxi">
                    <input type="radio" id="taxi" name="r">
                    <div class="checkbox__checkmark"></div>
                    Совместное такси
                </label>
            </li>
        </ul>
    </div>

    <div class="price">
        <p class="choose-price">Цена в рублях:</p>
        <input type="number" id="price-rub" value="100" step="50" min="0">
    </div>
    <div class="av-text">
        Свободных мест
        <input type="number" list="places" step="1" min="1" max="4" id="av" class="number-input"/>
        <datalist id="places">
            <option value="1">
            <option value="2">
            <option value="3">
            <option value="4">
        </datalist>
    </div>
    <div class="nav-buttons">
        <button class="next" id="dir-button1" on:click={()=>{$step--}}>Назад</button>
        <button class="next" id="dir-button2" on:click={()=>{isOwnCar ? $step++ : $step+=2}}>Далее</button>
    </div>
</div>
