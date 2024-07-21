<script lang="ts">
    import {url} from '../../../enviroment';
</script>

<p id="success">Успешно!</p>
<p id="created">Ваше объявление создано</p>
<p id="message">Бот отправит Вам сообщение об откликнувшихся пассажирах</p>
<div id="botton">
    <button id="again" on:click={()=>{window.location.href="../createTrip.html"}}>Создать ещё одну поездку</button>
</div>
<img id="car" src="{url}/static/images/Frame%203.svg" alt="car">
<p id="color-value"></p>

<style>
    p {
        text-align: center;
        color: black;
        font-family: 'Kreadon Regular';
    }

    #success {
        margin-top: 25%;
        font-size: 40px;
    }

    #created {
        font-size: 30px;
    }

    #message {
        font-size: 20px;
    }

    #car {
        display: block;
        margin-left: -25%;
        margin-right: auto;
        width: 130%;
        position: fixed;
    }

    #botton {
        width: 100%;
        display: flex;
        justify-content: center;
    }

    #again {
        font-family: "Kreadon Regular";
        font-size: 20px;
        width: 80%;
        border-radius: 10px;
        padding: 3%;
        border: 0px;
        background-color: #FBEC69;
        box-shadow: 0px 3px 1cqmax rgba(0, 0, 0, 0.3);
        color: black;
    }
</style>