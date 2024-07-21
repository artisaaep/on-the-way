<script lang="ts">
    import {onMount} from "svelte";

    export let isOpen = false;
    $: hiddenStyle = isOpen ? 'display: block' : 'display: none';
    let BackButton = {
        show: ()=>{},
        hide: ()=>{},
        onClick: (callback: CallableFunction)=>{}
    };
    onMount(()=>{
        BackButton = window.Telegram.WebApp.BackButton;
        BackButton.onClick(function () {
            isOpen = false
            BackButton.hide();
        });
    })

    $: if (isOpen){
        BackButton.show();
    } else {
        BackButton.hide()
    }

</script>

<div>
    <div class="modal" style={hiddenStyle}>
        <div class="content">
            <slot name="content"/>
        </div>
    </div>
    <span on:click={() => {isOpen = !isOpen}}>
        <div class="trigger">
            <slot name="trigger"/>
        </div>
    </span>
</div>

<style>
    span:hover {
        cursor: pointer;
    }

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
        margin: 5% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
        border-radius: 2em;
    }
</style>