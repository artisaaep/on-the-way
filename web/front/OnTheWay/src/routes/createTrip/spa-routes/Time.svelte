<script lang="ts">
    import {url} from '../../../enviroment'
    import {data, step} from "../Common";

    let timeFrom: string = "00:00";
    let timeTo: string = "00:00";
</script>
<img src="{url}/static/images/date-range-svgrepo-com.svg" class="date-img" alt="calendar">
<div class="grey-rect">
    <div class="desc-img">
        <p class="dir-desc">Дата и время поездки</p>
    </div>
    <div class="date">
        <p class="choose-d">Дата:</p>
        <input type="date" id="date-f" bind:value={data.departure_date}/>
    </div>
    <div class="time">
        <p class="choose-t">Временной диапазон начала поездки:</p>
        <div id="time-range">
            <p class="ft">от</p>
            <input type="time" class="time-f" bind:value={timeFrom}>

            <p class="ft">до</p>
            <input type="time" class="time-f" bind:value={timeTo}>
        </div>
    </div>
    <div class="nav-buttons">
        <button class="next" on:click={()=>{
            data.departure_time = `${timeFrom}-${timeTo}`;
            $step--;
        }}>
            Назад
        </button>
        <button class="next" on:click={()=>{
            data.departure_time = `${timeFrom}-${timeTo}`;
            $step++;
        }}>
            Далее
        </button>
    </div>
</div>
