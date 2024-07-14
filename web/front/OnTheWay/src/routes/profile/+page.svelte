<script lang="ts">
    import {url} from "../../enviroment.js";
    import type {Car} from "$lib/Types";
    import type {User} from "$lib/Types"
    import AddCar from "$lib/AddCar.svelte";
    import './profile.css';

    import {onMount} from "svelte";
    let userUrl: string;
    let user: User | null = null;

    let cars: Car[];

    async function carFetcher() {
        if (!user){
            return;
        }
        for (const id of user.car_ids) {
            cars.push(await (await fetch(url + "/api/cars/" + id, {})).json());
        }
    }
    onMount(async () => {
        userUrl = url + "/api/users/" + window.Telegram.WebApp.initDataUnsafe.user.id;
        window.Telegram.WebApp.expand();
        user = await (await fetch(userUrl, {
            method: "GET",
        })).json();
    });

</script>
{#if user}
    <div class="navig">
        <p id="My-profile"><img id="imgprof" src="{url}/static/icons/profile-1341-svgrepo-com.svg" alt="mark-profile">
            Мой
            профиль</p>
        <button id="back" on:click={()=>{window.history.back();}}>Назад</button>
    </div>
    <div class="lala">
        <p id="name">{user.name}</p>
    </div>

    <img src="{userUrl}/photo" alt="Аватарка" id="avatar"/>
    <div class="bio">
        <p id="age">Возраст: {user.age}</p>
        <p id="sex">Пол: {user.sex ? "Женский" : "Мужской"}</p>
        <p id="rides">{user.rides_amount}</p>
    </div>
    <div class="PhotoCar">
        <img id="carPhoto" src="{url}/static/icons/image-22.svg" alt="section-icon">
    </div>
    <div id="cars">
        <p id="MyCars">Мои машины:</p>
        <div class="mashini">
            {#if user.car_ids}
                <p>У вас ещё нет добавленных машин.</p>
            {:else }
                <ul id="cars-ul">
                    {carFetcher()}
                    {#each cars as car}
                        <li><p class="car"><b>{car.color} {car.brand} {car.number}</b></p></li>
                    {/each}
                </ul>
            {/if}
        </div>
    </div>
    <br>
    <br>
    <a id="addcar">Добавить машину</a>
    <button id="redt" on:click={()=>{}}>Редактировать</button>
{:else}
    <p>nothing to render</p>
{/if}