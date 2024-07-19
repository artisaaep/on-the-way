import {Writable, writable} from "svelte/store";
import type {User} from "../lib/Types";

export let user: Writable<null | User> = writable(null);