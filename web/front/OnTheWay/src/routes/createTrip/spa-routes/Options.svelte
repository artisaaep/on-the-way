<script>
    import {data, step} from "../Common";

    function addInfo() {
        data.allow_luggage = document.getElementById('lag').checked;
        data.allow_pets = document.getElementById('an').checked;
        data.has_child_seat = document.getElementById('ch').checked;
        data.has_buster = document.getElementById('bu').checked;
        if (data.allow_luggage) {
            data.dop += "Есть место для багажа."
        }
        if (data.allow_pets) {
            data.dop += "Можно с животными."
        }
        if (data.has_child_seat) {
            data.dop += "Есть детское кресло."
        }
        if (data.has_buster) {
            data.dop += "Есть бустер."
        }
    }

</script>

<div class="grey-rect">
    <div class="header">
        <p id="param-text">Параметры</p>
        <hr id="hr">
    </div>
    <ul class="choice" id="param">
        <li class="param-li">
            <label for="lag">
                <input type="checkbox" id="lag" bind:checked={data.allow_luggage}>
                <div class="checkbox__checkmark"></div>
                Есть место для багажа
            </label>
        </li>
        <li class="param-li">
            <label for="an">
                <input type="checkbox" id="an" bind:checked={data.allow_pets}>
                <div class="checkbox__checkmark"></div>
                Можно с животными
            </label>
        </li>
        <li class="param-li">
            <label for="ch">
                <input type="checkbox" id="ch" bind:checked={data.has_child_seat}>
                <div class="checkbox__checkmark"></div>
                Есть детское кресло
            </label>
        </li>
        <li class="param-li">
            <label for="bu">
                <input type="checkbox" id="bu" bind:checked={data.has_buster}>
                <div class="checkbox__checkmark"></div>
                Есть бустер
            </label>
        </li>
    </ul>

    <textarea id="add" class="com" placeholder="Дополнительные сведения о поездке..." bind:value={data.add_info}/>

    
</div>
<div class="nav-buttons">
    <button class="next" on:click={()=>{
        if (data.kind === "На своей машине")
            $step--
        else
            $step-=2
    }}>
        Назад
    </button>
    <button class="next"
        on:click={() => {
            addInfo(); 
            $step++;
        }}>
        Далее
    </button>
</div>