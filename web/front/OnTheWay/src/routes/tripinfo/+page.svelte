<script lang="ts">
    import {onMount} from "svelte";
    import {Trip} from "$lib/Types";
    import {url} from "../../enviroment";
    import "./tripinfo.css"
    import {user} from "../CurrentUser";

    let trip: Trip;

    async function main() {
        let href = document.location.href;
        let id = href.split("?")[1].split("#")[0];
        trip = await (await fetch(url + "/api/trips/" + id, {
            method: "GET",
        })).json();
    }
    async function submit() {
        let cond1 = trip.start_location.toLowerCase() != "иннополис" && trip.start_location.toLowerCase() != "казань";
        let cond2 = trip.end_location.toLowerCase() != "иннополис" && trip.end_location.toLowerCase() != "казань"
        if (cond1 || cond2) {
            alert("Локация может быть только Иннополис или Казань");
        } else {
            try {
                let left = trip.departure_time.split('-')[0].split(":");
                let right = trip.departure_time.split('-')[1].split(":");
                console.log(left);
                console.log(right);
                let timecond1 = left[0].length == 0 || left[1].length == 0 || left[0].length > 2 || left[1].length > 2;
                let timecond2 = right[0].length == 0 || right[1].length == 0 || right[0].length > 2 || right[1].length > 2;
                let timecond3 = Number(left[0]) < 0 || Number(left[0]) > 23 || Number(left[1]) < 0 || Number(left[1]) > 59;
                let timecond4 = Number(right[0]) < 0 || Number(right[0]) > 23 || Number(right[1]) < 0 || Number(right[1]) > 59;
                if (timecond1 || timecond2 || timecond3 || timecond4) {
                    alert("Время введено в неправильном формате.\nВведите время в формате хх:xx-xx:xx");
                } else {
                    let response = await fetch(`${url}/api/trips/` + trip.id + `/driver?driverID=` + trip.driver.id, {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(trip)
                    })
                    trip = trip;
                    alert("Изменения успешно применены!");
                    window.Telegram.WebApp.close();
                }
            } catch (e) {
                alert("Время введено в неправильно формате.\nВведите время в формате хх:xx-xx:xx");
            }
        }
    }
    async function deleteTrip() {
        let response = await fetch(`${url}/api/trips/` + trip.id, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            }
        })
        alert("Ваша поездка успешно удалена!");
        window.Telegram.WebApp.close();
    }

    onMount(main);
</script>
{#if trip && trip.detail !== "Trip not found"}
    <div class="grey-rect">
        <p class="dir-desc">Данные о поездке</p>
        <div id="trip-data">
            <table id="trip">
                <tr class="line">
                    <td class="param-name">
                        <p>откуда</p>
                    </td>
                    <td class="param-val">
                        <input bind:value={trip.start_location}><input bind:value={trip.clarify_from}>
                    </td>
                </tr>
                <tr class="line">
                    <td class="param-name">
                        <p>куда</p>
                    </td>
                    <td class="param-val">
                        <input bind:value={trip.end_location}><input bind:value={trip.clarify_to}>
                    </td>
                </tr>
                <tr class="line">
                    <td class="param-name">
                        <p>дата</p>
                    </td>
                    <td class="param-val">
                        <input type="date" id="date-f" bind:value={trip.departure_date}>
                    </td>
                </tr>
                <tr class="line">
                    <td class="param-name">
                        <p>время</p>
                    </td>
                    <td class="param-val">
                        <input bind:value={trip.departure_time}>
                    </td>
                </tr>
                <tr class="line">
                    <td class="param-name">
                        <p>цена</p>
                    </td>
                    <td class="param-val">
                        <input bind:value={trip.price}>
                    </td>
                </tr>
                <tr class="line">
                    <td class="param-name">
                        <p>кол-во мест</p>
                    </td>
                    <td class="param-val">
                        <input bind:value={trip.available_seats}>
                    </td>
                </tr>
            </table>
        </div>
        
    </div>
    <div class="three-buttons">
        <div class="nav-buttons">
        <button class="next" id="dir-button1" on:click={submit}>Применить</button>
        <button class="next" id="dir-button2" on:click={window.Telegram.WebApp.close}>Закрыть</button>
        </div>
        <button class="next" id="delete" on:click={deleteTrip}>Удалить поездку</button>
    </div>
{:else}
    Поездки не существует
{/if}