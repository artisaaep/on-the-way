import {writable, Writable} from "svelte/store";
import {NewTrip, Passenger} from "../../lib/Types";

export let step= writable(0);
export let data: NewTrip = {
    driver_id: 0,
    is_request: true,

    start_location: "",
    clarify_from: undefined,
    end_location: "",
    clarify_to: undefined,

    departure_date: "2024-06-23",
    departure_time: "",

    car_id: undefined,

    has_child_seat: false,
    has_buster: false,
    allow_luggage: false,
    allow_pets: false,
    available_seats: 1,
    add_info: undefined,
    price: 100,
};
