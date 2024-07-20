<script>
    import {data, step} from "../Common";
    import {url} from "../../../enviroment"
</script>

<div class="step0">
    <div class="pdiv">
        <p class="q">В какой роли вы хотели бы</p>
        <p class="q">совершить поездку?</p>
    </div>
    <div id="buttonschoose">
        <button id="btnc" class="buttonchoose" on:click={()=>{ data.is_request = false; $step++; }}>
            Водитель
        </button>
        <button id="btnc" class="buttonchoose" on:click={()=>{ data.is_request = true; $step++; }}>
            Пассажир
        </button>
    </div>
    <div class="img-cont">
        <img id="firstimg" src="{url}/static/images/car-svgrepo-com.svg" alt="hzcho">
    </div>
</div>
