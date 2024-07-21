<script lang="ts">
    import Modal from "$lib/modal/Modal.svelte";
    import {NewCar} from "$lib/Types";
    import {onMount} from "svelte";
    import {url} from '../enviroment'
    import './assets/AddCar.css'

    let modelOpen:boolean = false;

    function defaultCar(): NewCar {
        return {
            owner_id: 0,
            brand: "",
            number: undefined,
            color: undefined
        }
    }

    let car: NewCar = defaultCar();

    onMount(() => {
        car.owner_id = window.Telegram.WebApp.initDataUnsafe.user.id;
    })

    async function submit() {
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
                modelOpen = false;
            } else {
                window.Telegram.WebApp.showAlert("Something went wrong");
            }
        })
    }
</script>

<Modal bind:isOpen={modelOpen}>
    <div id="myModal" class="modal" slot="content">
        <div class="modal-content">
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
    <slot slot="trigger"/>
</Modal>