<script lang="ts">
    import {url} from '../../../enviroment'
    import {data, step} from "../Common";
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
            <input type="time" class="time-f" bind:value={data.timeFrom}>

            <p class="ft">-</p>
            <input type="time" class="time-f" bind:value={data.timeTo}>
        </div>
    </div>
    
</div>
<div class="nav-buttons">
    <button class="next" on:click={()=>{
        data.departure_time = `${data.timeFrom}-${data.timeTo}`;
        $step--;
    }}>
        Назад
    </button>
    <button class="next" on:click={()=>{
        data.departure_time = `${data.timeFrom}-${data.timeTo}`;
        $step++;
    }}>
        Далее
    </button>
</div>