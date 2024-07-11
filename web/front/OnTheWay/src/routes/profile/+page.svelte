<script>
    import {env} from "web/front/OnTheWay/src/enviroment.js"

    const url = env.BASE_WEBAPP_URL;

    async function main() {
        const userUrl = url + "/api/users/" + window.Telegram.WebApp.initDataUnsafe.user.id;
        const response = await (await fetch(userUrl, {})).json();
        const img = document.getElementById("avatar");
        img.src = userUrl + "/photo";
        const nameElem = document.getElementById("name");
        nameElem.textContent = response.name;
        const ageElem = document.getElementById("age");
        ageElem.textContent = "Возраст: " + response.age;
        const ridesElem = document.getElementById("rides");
        ridesElem.textContent = "Количество поездок: " + response.rides_amount;
        const carsElem = document.getElementById("cars-ul");
        for (const id of response.car_ids) {
            const carInfo = await (await fetch(url + "/api/cars/" + id, {})).json();
            carsElem.innerHTML += `<li><p class="car"><b>${carInfo.color} ${carInfo.brand} ${carInfo.number}</b></p></li>`;
        }
    }

    main();
</script>
<div class="navig">
    <p id="My-profile"><img id="imgprof" src="icons/profile-1341-svgrepo-com.svg"> Мой профиль</p>
    <button id="back" onclick="goBack()">Назад</button>
</div>
<p id="name"></p>
<img alt="Аватарка" id="avatar"/>
<div class="bio">
    <p id="age">Возраст: 18</p>
    <p id="rides">0</p>
</div>
<div id="cars">
    <p id="MyCars">Мои машины:</p>
    <div class="mashini">
        <ul id="cars-ul">
        </ul>
    </div>
</div>
<div id="myModal" class="modal">
    <div class="modal-content">
        <div class="navig">
            <button class="close">Закрыть</button>
        </div>

        <p id="Hadd">Добавить машину</p>
        <br>
        <div class="parameters">
            <p><b>Модель</b></p>
            <input type="text" class="vvod" id="p1" placeholder="Пример: BMW X5">
        </div>
        <div class="parameters">
            <p><b>Номер</b></p>
            <input type="text" class="vvod" id="p2" placeholder="Пример: А123БВ">
        </div>
        <div class="parameters">
            <p><b>Цвет</b></p>
            <input type="text" class="vvod" id="p3" placeholder="Пример: Белый">
        </div>
        <button id="ADD" onclick="addCar()">Добавить</button>
    </div>
</div>
<br>
<br>
<u id="addcar">Добавить машину</u>
<button id="redt" onclick="">Редактировать</button>


<style>
    input:focus {
        outline: none;
    }


    #My-profile {
        padding: 5px;
        margin-left: 15px;
        width: 130px;
        background-color: #E3E1E1;
        color: black;
        border-radius: 10px;
        border: 1px solid black;
        border-color: black;
        font-size: 20px;
        font-family: Kreadon_regular;
        padding-left: 40px;
    }

    #imgprof {
        height: 15%;
        width: 15%;
        float: left;
        margin-right: 5%;
        margin-left: -30px;
    }

    #back {
        font-family: Kreadon_regular;
        font-size: 20px;
        margin: -15.5%;
        margin-right: 4%;
        margin-top: -15%;
        padding: 1.5%;
        background-color: #E3E1E1;
        color: black;
        border-radius: 10px;
        border: 1px solid var(--tg-theme-text-color);
        width: 25%;
        float: right;
        top: 200px;
    }

    #name {
        margin-left: 5%;
        margin-right: 5%;
        font-family: Kreadon_regular;
        text-align: center;
        font-size: 26px;
        padding: 1.5%;
        width: 88%;
        background-color: #E3E1E1;
        color: black;
        border-radius: 10px;
        border-color: black;
    }

    #avatar {
        display: block;
        margin-left: 5%;
        width: 45%;
        height: 45%;
        border-radius: 50%;
        border: solid 1px black;
        margin-top: 3%;
    }

    #age {
        font-family: Kreadon_regular;
        font-size: 20px;
        position: absolute;
        margin-left: 55%;
        margin-right: 5%;
        margin-top: -38%;
    }

    #sex {
        font-family: Kreadon_regular;
        font-size: 20px;
        position: absolute;
        margin-left: 55%;
        margin-right: 5%;
        margin-top: -25%;
    }

    #rides {
        font-family: Kreadon_regular;
        font-size: 20px;
        position: absolute;
        margin-left: 55%;
        margin-right: 5%;
        margin-top: -14%;
    }

    #MyCars {
        font-size: 20px;
        background-color: #E3E1E1;
        width: 35%;
        border-radius: 10px;
        padding: 1.5%;
        margin-left: 5%;
        color: black;
        font-family: Kreadon_regular;
        padding-left: 5%;
    }

    .mashini {
        margin-right: 40%;
        margin-left: 5%;
    }

    .car {
        margin-top: auto;
        margin-bottom: auto;
        margin-left: 0;
        margin-top: 8%;
    }

    a {
        margin-left: 18%;
        margin-top: -20%;
        font-family: kreadon_demi;
        font-size: 15px;
    }

    #addcar {
        font-family: Kreadon_demi;
        font-size: 20px;
        margin-left: 6%;
        color: var(--tg-theme-text-color);
    }

    li {
        gap: 80px;
    }

    #redt {
        margin: auto;
        display: flex;
        justify-content: center;
        margin-top: 15%;
        font-family: Kreadon_regular;
        width: 65%;
        font-size: 26px;
        border-radius: 10px;
        border: 0px;
        color: black;
        padding: 2%;
        background-color: #FBEA50;
        box-shadow: 0px 7px 10px rgba(0, 0, 0, 0.3);
    }

</style>