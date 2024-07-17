<script lang="ts">
    import {isOpen, id} from "./store"
    import {getContext} from "svelte"

    const modalId = getContext("modalId")
</script>
<div>
    <div class="modal" class:hidden={modalId !== $id}>
        <div class="content">
            <slot/>
        </div>
    </div>
</div>
<style>
    .modal {
        position: fixed;
        z-index: 9999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgb(0, 0, 0);
        background-color: rgba(0, 0, 0, 0.4);
    }

    .content {
        position: relative;
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
        border-radius: 2em;
    }

    .hidden {
        display: none;
    }
</style>