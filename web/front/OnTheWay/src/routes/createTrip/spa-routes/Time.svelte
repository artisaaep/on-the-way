<script lang="ts">
    import {url} from '../../../enviroment'
    import {data, step} from "../Common";
    const separate_time = data.departure_time.split('-');
    let timeFrom: string = separate_time[0];
    let timeTo: string = separate_time[1];
    function validateDate(): boolean {
        const currentDate = new Date();
        const selectedDate = new Date(data.departure_date);
        currentDate.setHours(0, 0, 0, 0);
        selectedDate.setHours(0, 0, 0, 0);
        
        if (selectedDate < currentDate) {
            window.Telegram.WebApp.showAlert("Дата и время поездки не могут быть раньше текщих даты и времени");
            return false;
        }
        return true;
    }
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
            <input type="time" class="time-f" bind:value={timeFrom}>

            <p class="ft">-</p>
            <input type="time" class="time-f" bind:value={timeTo}>
        </div>
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
        if (validateDate()) {
            data.departure_time = `${timeFrom}-${timeTo}`;
            $step++;
        }
    }}>
        Далее
    </button>
</div>