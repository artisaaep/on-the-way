<script lang="ts">
    import {onMount} from "svelte";
    import {url} from "../../enviroment.js";
    import type {Car} from "$lib/Types";
    import type {User} from "$lib/Types"
    import AddCar from "$lib/AddCar.svelte";
    import './profile.css';
    import {carFetcher, userFetcher} from "$lib/fetchers";

    let userUrl: string;
    let user: User | null = null;

    let cars: Car[] = [];

    onMount(async () => {
        userUrl = url + "/api/users/" + window.Telegram.WebApp.initDataUnsafe.user.id;
        window.Telegram.WebApp.expand();
        user = userFetcher();
    });

</script>
{#if user}

    <div class="lala">
        <p id="name">{user.name}</p>
    </div>

    <img src="{userUrl}/photo" alt="Аватарка" id="avatar"/>
    <div class="bio">
        <p id="age">Возраст: {user.age}</p>
        <p id="sex">Пол: {user.sex ? "Женский" : "Мужской"}</p>
        <p id="rides">Поездок: {user.rides_amount}</p>
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
                    {carFetcher(cars, user)}
                    <!--TODO: this is (each block) not work properly for unknown reason-->
                    {#each cars as car}
                        <li><p class="car"><b>{car.color} {car.brand} {car.number}</b></p></li>
                    {/each}
                </ul>
            {/if}
        </div>
    </div>
    <AddCar>
        <a id="addcar">Добавить машину</a>
    </AddCar>
    <button id="redt" on:click={()=>{}}>Редактировать</button>
{:else}
    <p>nothing to render</p>
{/if}