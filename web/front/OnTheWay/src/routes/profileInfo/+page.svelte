<script lang="ts">
    import {onMount} from "svelte";
    import {url} from "../../enviroment.js";
    import './profileInfo.css';
    import {carFetcher, userFetcher} from "../../lib/fetchers";
    import type {Car, User} from "$lib/Types";
    import {draw} from "svelte/transition";
    import {data} from "../createTrip/Common";
    import {user} from '../CurrentUser'

    let cars: Car[] = [];

    async function main() {
        var BackButton = window.Telegram.WebApp.BackButton;
        BackButton.show();
        BackButton.onClick(function () {
            window.history.back();
            BackButton.hide();
        });
        $user = await userFetcher();
        if ($user.car_ids) {
            await carFetcher(cars, $user);
            cars = [...cars];
        }
    }

    async function submit() {
        let response = await fetch(`${url}/api/users`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify($user)
        })
        $user = $user;
    }

    onMount(main);

</script>
<div class="grey-rect">
    <div class="desc-img" id="sub-d">
        <p class="dir-desc" id="submit-data">Редактировать профиль</p>
    </div>
    <table id="trip">
        <tr class="line">
            <td class="param-name">
                <p>Имя</p>
            </td>
            <td class="param-val">
                {#if $user}
                    <input bind:value={$user.name}>
                {/if}
            </td>
        </tr>
        <br>
        <tr class="line">
            <td class="param-name">
                <p>Возраст</p>
            </td>
            <td class="param-val">
                {#if $user}
                    <input bind:value={$user.age}>
                {/if}
            </td>
        </tr>
        <br>
        <tr class="line">
            <td class="param-name">
                <p>Машины</p>
            </td>
            <td class="param-val">
                <ul>
                    {#each cars as car}
                        <li><p>{car.color} {car.brand} {car.number}</p></li>
                    {/each}
                </ul>
            </td>
        </tr>
        <tr class="line">
            <td class="submit">
                <button id="primenit" on:click={submit}>Применить</button>
            </td>
        </tr>
    </table>
</div>