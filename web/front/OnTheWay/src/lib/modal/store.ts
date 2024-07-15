import {Writable, writable} from "svelte/store"

export const isOpen = writable(false)
export const id = writable()
export function closeModal(){
    id.set(false);
}