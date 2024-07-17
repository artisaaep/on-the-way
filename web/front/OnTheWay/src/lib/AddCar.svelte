<script lang="ts">
    import Modal from "$lib/modal/Modal.svelte";
    import Content from "$lib/modal/Content.svelte";
    import Trigger from "$lib/modal/Trigger.svelte";
    import {closeModal} from "$lib/modal/store";
    import {NewCar} from "$lib/Types";
    import {onMount} from "svelte";
    import {url} from '../enviroment'

    function defaultCar(): NewCar {
        return {
            owner_id: 0,
            brand: "",
            number: undefined,
            color: undefined
        }
    }

    let car: NewCar = defaultCar();

    onMount(()=>{
        car.owner_id = window.Telegram.WebApp.initDataUnsafe.user.id;
    })

    async function submit(){
        if (!car.brand || !car.number || !car.color) {
            window.Telegram.WebApp.showAlert("Not all data is filled");
            return false;
        }
        await fetch(url + "/api/cars/", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(car),
        }).then(async response => {
            if (response.ok) {
                // closeModal()
                window.location.reload();
            } else {
                window.Telegram.WebApp.showAlert("Something went wrong");
            }
        })
    }
</script>

<Modal>
    <Content>
        <div id="myModal" class="modal">
            <div class="modal-content">
                <div class="navig">
                    <button id="back" class="close" on:click={()=>{closeModal()}}>Назад</button>
                </div>

                <p id="Hadd">Добавить машину</p>
                <br>
                <div class="parameters">
                    <p><b>Модель</b></p>
                    <input type="text" class="vvod" id="p1" placeholder="Пример: BMW X5" bind:value={car.brand}>
                </div>
                <div class="parameters">
                    <p><b>Номер</b></p>
                    <input type="text" class="vvod" id="p2" placeholder="Пример: А123БВ" bind:value={car.number}>
                </div>
                <div class="parameters">
                    <p><b>Цвет</b></p>
                    <input type="text" class="vvod" id="p3" placeholder="Пример: Белый" bind:value={car.color}>
                </div>
                <button id="ADDcarBtn" on:click={submit}>Добавить</button>
            </div>
        </div>
    </Content>
    <Trigger>
        <slot/>
    </Trigger>
</Modal>
<style>
    .close {
        font-family: Kreadon_regular;
        font-size: 20px;
        margin-right: 15px;
        padding: 0;
        margin-top: -20%;
        background-color: var(--tg-theme-secondary-bg-color);
        color: var(--tg-theme-text-color);
        border-radius: 10px;
        border: 1px solid black;
        width: 100px;
        height: 38px;
        float: right;
        top: 200px;
        transition: 0.2s;
    }

    .close:hover,
    .close:focus {
        background-color: gray;
    }

    #Hadd {
        font-family: Kreadon_regular;
        font-size: 26px;
        text-align: center;
        background-color: #E3E1E1;
        color: black;
        border-radius: 10px;
        padding: 5px;
        margin-left: auto;
        margin-right: auto;
        width: 250px;
        margin-top: 10px;
    }

    .parameters {
        font-size: 20px;
        color: black;
        font-family: Kreadon_medium;
        display: flex;
        flex-direction: column;
    }

    .modal p {
        margin-left: 10%;
    }

    .parameters a {
        margin-right: 10px;
        margin-left: 5%;
        font-size: 20px;
    }

    .vvod::placeholder {
        font-size: 16px;
    }

    input, a {
        -webkit-tap-highlight-color: transparent;
    }

    .parameters input {
        display: block;
        margin-bottom: 15px;
        font-size: 16px;
        border: 0px;
        border-radius: 10px;
        padding: 2%;
        width: 80%;
        height: 30px;
        margin-left: auto;
        margin-right: auto;
        background-color: #E3E1E1;
        box-shadow: 0px 3px 1cqmax rgba(0, 0, 0, 0.3);
    }

    #ADDcarBtn {
        font-family: Kreadon_regular;
        font-size: 16px;
        margin-top: 15%;
        padding: 2%;
        padding-left: 10%;
        padding-right: 10%;
        text-align: center;
        border-radius: 10px;
        margin: auto;
        display: flex;
        justify-content: center;
        border: 0px;
        background-color: #FBEA50;
        color: #1a1a1a;
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.3);
        transition: 0.2s;
    }

    button {
        cursor: pointer;
    }
</style>