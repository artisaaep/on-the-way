<script lang="ts">
    import {data, step} from "../Common";
    import {url} from "../../../enviroment";

    async function submitTrip() {
        console.log(data)
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
    <div class="desc-img" id="sub-d">
        <p class="dir-desc" id="submit-data">Подтвердите данные о поездке</p>
    </div>
    <div id="trip-data">
        <p>Откуда: {data.start_location} ({data.clarify_from})</p>
        <p>Куда: {data.end_location} ({data.clarify_to})</p>
        <p>Дата и время: {data.departure_date} {data.departure_time}</p>
    </div>
    <div class="nav-buttons">
        <button class="next" id="dir-button1" on:click={()=>{$step--}}>Назад</button>
        <button class="next" id="dir-button2" on:click={submitTrip}>Подтвердить</button>
    </div>
</div>
