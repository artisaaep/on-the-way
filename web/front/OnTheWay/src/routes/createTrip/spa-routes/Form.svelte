<script lang="ts">
    import {data, step} from "../Common";
    import {url} from "../../../enviroment";

    async function submitTrip() {
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
            }
        });
    }

    async function finish() {
        let id = window.Telegram.WebApp.initDataUnsafe.user.id;
        // TODO: transfer it to the backend
        let kb = {
            inline_keyboard: [[{
                text: 'Подробнее',
                // TODO page for tripInfo
                web_app: {url: `${url}/static/tripinfo.html`}
            }]]
        };
        let text = `Ваша поездка *${data.start_location} - ${data.end_location}* успешно создана! 🚙

Нажмите на кнопку ниже, чтобы посмотреть подробную информацию о поездке или отредактировать ее ☺️`;

        let encodedText = encodeURIComponent(text);
        let encodedReplyMarkup = encodeURIComponent(JSON.stringify(kb));
        console.log("aaa");
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
                        <p>{data.clarify_from}</p>
                    </td>
                </tr>
                <tr class="line">
                    <td class="param-name">
                        <p>куда</p>
                    </td>
                    <td class="param-val">
                        <p>{data.end_location}</p>
                        <p>{data.clarify_to}</p>
                    </td>
                </tr>
                <tr class="line">
                    <td class="param-name">
                        <p>дата</p>
                    </td>
                    <td class="param-val">
                        <p>{data.departure_date}</p>
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
                        <p>вид</p>
                    </td>
                    <td class="param-val">
                        <p>{data.kind}</p>
                    </td>
                </tr>
                <tr class="line">
                    <td class="param-name">
                        <p>цена</p>
                    </td>
                    <td class="param-val">
                        <p>{data.price}</p>
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
                <tr class="line">
                    <td class="param-name">
                        <p>прочее</p>
                    </td>
                    <td class="param-val">
                        <p>{data.add_info}</p>
                    </td>
                </tr>
            </table>
            <p class="data-dop">{data.dop}</p>   
</div>
<div class="nav-buttons">
    <button class="next" id="dir-button1" on:click={()=>{$step--}}>Назад</button>
    <button class="next" id="dir-button2" on:click={submitTrip}>Подтвердить</button>
</div>
