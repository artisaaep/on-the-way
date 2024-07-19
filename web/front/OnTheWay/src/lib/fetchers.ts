import type {Car, User} from "./Types";
import {url} from "../enviroment";

export async function carFetcher(destination: Car[], user: User): Promise<void> {
    if (!user) {
        return;
    }
    if (!user.car_ids){
        return ;
    }
    for (const id of user.car_ids) {
        destination.push(await (await fetch(url + "/api/cars/" + id, {})).json());
    }
}

export async function userFetcher(): Promise<User> {
    return await (await fetch(url + "/api/users/" + window.Telegram.WebApp.initDataUnsafe.user.id, {
        method: "GET",
    })).json();
}