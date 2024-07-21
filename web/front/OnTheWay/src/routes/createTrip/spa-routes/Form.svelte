<script lang="ts">
    import {data, step} from "../Common";
    import {url} from "../../../enviroment";
    import {onMount} from "svelte";
    import {Car} from "$lib/Types";
    import {carFetcher} from "$lib/fetchers";

    function formatDate(date: Date): string {
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${day}-${month}-${year}`;
    }

    let car_: Car;
    onMount(async () => {
        car_ = await (await fetch(url + "/api/cars/" + data.car_id, {})).json();
    })

    let options: string = '';
    if (data.allow_luggage) {
        options += "Можно с багажом. "
    }
    if (data.allow_pets) {
        options += "Можно с животными. "
    }
    if (data.has_child_seat) {
        options += "Детское кресло. "
    }
    if (data.has_buster) {
        options += "Бустер. "
    }

    async function submitTrip() {
        data.departure_date = formatDate(new Date(data.departure_date));
        console.log(data)
        if (data.available_seats===null){
            data.available_seats = 4;
        }
        await fetch(url + "/api/trips/", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data),
        }).then(async response => {
            if (response.ok) {
                await finish()
            } else {
                window.Telegram.WebApp.showAlert("Something went wrong");
                console.log(response)
            }
        });
    }

    async function finish() {
        let id = window.Telegram.WebApp.initDataUnsafe.user.id;
        // TODO: transfer it to the backend
        const trips = await (await fetch(url + "/api/trips", {
                method: "GET",
            })).json();
        let kb = {
            inline_keyboard: [[{
                text: 'Подробнее',
                // TODO page for tripInfo
                web_app: {url: `${url}/app/tripinfo.html?${trips[trips.length-1].id}`},
            }]]
        };
        let text = `Ваша поездка *${data.start_location} - ${data.end_location}* успешно создана! 🚙

Нажмите на кнопку ниже, чтобы посмотреть подробную информацию о поездке или отредактировать ее ☺️`;

        let encodedText = encodeURIComponent(text);
        let encodedReplyMarkup = encodeURIComponent(JSON.stringify(kb));
        await fetch(`https://api.telegram.org/bot6658030178:AAF7JwKztrDvVQVlzR3lZlSebnf961JUocs/sendMessage?chat_id=${id}&text=${encodedText}&parse_mode=Markdown&reply_markup=${encodedReplyMarkup}`);
        // endTODO
        window.location.href = `${url}/static/tripcreated.html`;
    }


</script>
<div class="grey-rect">
    <table id="trip">
        <tr class="line">
            <td class="param-name">
                <p>откуда</p>
            </td>
            <td class="param-val">
                <p>{data.start_location}</p>
                {#if data.clarify_from != ""}
                <p>{data.clarify_from}</p>
                {/if}
            </td>
        </tr>
        <tr class="line">
            <td class="param-name">
                <p>куда</p>
            </td>
            <td class="param-val">
                <p>{data.end_location}</p>
                {#if data.clarify_to != ""}
                <p>{data.clarify_to}</p>
                {/if}
            </td>
        </tr>
        <tr class="line">
            <td class="param-name">
                <p>дата</p>
            </td>
            <td class="param-val">
                <p>{formatDate(new Date(data.departure_date))}</p>
            </td>
        </tr>
        <tr class="line">
            <td class="param-name">
                <p>время</p>
            </td>
            <td class="param-val">
                <p>{data.departure_time}</p>
            </td>
        </tr>
        {#if data.is_request === false}
            <tr class="line">
                <td class="param-name">
                    <p>цена</p>
                </td>
                <td class="param-val">
                    <p>{data.price}</p>
                </td>
            </tr>
        <tr class="line">
            <td class="param-name">
                <p>Транспорт</p>
            </td>
            <td class="param-val">
                {#if car_}
                    <p>{car_.color ? car_.color + ' ' : ''}{car_.brand}</p>
                {/if}
            </td>
        </tr>
        {/if}
        <tr class="line">
            <td class="param-name">
                <p>мест</p>
            </td>
            <td class="param-val">
                <p>{data.available_seats}</p>
            </td>
        </tr>
        {#if data.add_info != null}
        <tr class="line">
            <td class="param-name">
                <p>прочее</p>
            </td>
            <td class="param-val">
                <p>{data.add_info}</p>
            </td>
        </tr>
        {/if}
    </table>
    <p class="data-dop">{options}</p>
</div>
<div class="nav-buttons">
    <button class="next" id="dir-button1" on:click={()=>{$step--}}>Назад</button>
    <button class="next" id="dir-button2" on:click={submitTrip}>Подтвердить</button>
</div>
