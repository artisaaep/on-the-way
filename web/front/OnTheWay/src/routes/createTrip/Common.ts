import {writable, Writable} from "svelte/store";
import {NewTrip, Passenger} from "../../lib/Types";

export const activeButton = writable("");

export let step= writable(0);

const today = new Date();
const year = today.getFullYear();
const month = String(today.getMonth() + 1).padStart(2, '0'); // Months are zero-based
const day = String(today.getDate()).padStart(2, '0');
const currentDate = `${year}-${month}-${day}`;

const hours = String(today.getHours()).padStart(2, '0');
const minutes = String(today.getMinutes()).padStart(2, '0');
const currentTime = `${hours}:${minutes}`;

export let data: NewTrip = {
    driver_id: 0,
    is_request: true,

    start_location: "",
    clarify_from: "",
    end_location: "",
    clarify_to: "",

    departure_date: currentDate,
    departure_time: `${currentTime}-${currentTime}`,

    car_id: undefined,

    has_child_seat: false,
    has_buster: false,
    allow_luggage: false,
    allow_pets: false,
    available_seats: null,
    add_info: null,
    price: 100,
};
