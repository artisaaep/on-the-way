<script lang="ts">
    import {url} from '../../../enviroment'
    import {data, step} from "../Common";
    const separate_time = data.departure_time.split('-');
    let timeFrom: string = separate_time[0];
    let timeTo: string = separate_time[1];
    const currentDate = new Date();
    const currentDateString = currentDate.toISOString().split('T')[0];
    console.log(currentDateString);
    function validateDate(): boolean {
        const selectedDate = new Date(data.departure_date);
        const currentDateMidnight = new Date(currentDateString);
        currentDateMidnight.setHours(0, 0, 0, 0);
        selectedDate.setHours(0, 0, 0, 0);
        const currentTime = new Date();
        const [hoursFrom, minutesFrom] = timeFrom.split(':').map(Number);
        const [hoursTo, minutesTo] = timeTo.split(':').map(Number);

        if (selectedDate < currentDateMidnight) {
            window.Telegram.WebApp.showAlert("Дата поездки не может быть раньше текущей даты");
            return false;
        }

        else if (selectedDate.getTime() === currentDateMidnight.getTime() && 
            (hoursFrom < currentTime.getHours() || (hoursFrom === currentTime.getHours() && minutesFrom < currentTime.getMinutes()))) {
            window.Telegram.WebApp.showAlert("Время начала поездки не может быть раньше текущего времени");
            return false;
        }

        else if (hoursTo < hoursFrom || (hoursTo === hoursFrom && minutesTo < minutesFrom)) {
            window.Telegram.WebApp.showAlert("Время конца промежутка не может быть раньше времени его начала");
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
        <input type="date" id="date-f" bind:value={data.departure_date} min={currentDateString}/>
    </div>
    <div class="time">
        <p class="choose-t">Временной диапазон начала поездки:</p>
        <div id="time-range">
            <input type="time" class="time-f" bind:value={timeFrom}>

            <p class="ft">-</p>
            <input type="time" class="time-f" bind:value={timeTo} min={timeFrom}>
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