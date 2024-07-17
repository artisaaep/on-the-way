<script lang="ts">
    import {url} from "../../../enviroment"
    import {data, step} from "../Common";
</script>
<div class="grey-rect">
    <div class="desc-img">
        {#if $step === 1}
            <p class="dir-desc">Откуда</p>
        {:else}
            <p class="dir-desc">Куда</p>
        {/if}
        <img src="{url}/static/images/location-pin-alt-svgrepo-com.svg" class="dir-image" alt="Location Pin">
    </div>
    <div class="but-text">
        <div class="buttons">
            {#if $step === 1}
                <button class="button1" id="left1" on:click={()=>{data.start_location = "Иннополис"}}>
                    Иннополис
                </button>
                <button class="button1" id="right1" on:click={()=>{data.start_location = "Казань"}}>
                    Казань
                </button>
            {:else}
                {#if data.start_location === "Иннополис"}
                    <button class="button1" id="left1" on:click={()=>{}}>Иннополис</button>
                    <button class="button1" id="right1" on:click={()=>{}} style="background-color: #969696">
                        Казань
                    </button>
                {:else}
                    <button class="button1" id="left1" on:click={()=>{}} style="background-color: #969696">
                        Иннополис
                    </button>
                    <button class="button1" id="right1" on:click={()=>{}}>Казань</button>
                {/if}
            {/if}
        </div>
        <textarea
                id="comment1"
                class="com"
                placeholder="Уточните место отправления..."
                bind:value={data.clarify_from}
        />
    </div>
    <div class="nav-buttons">
        <button class="next" on:click={()=>{$step--}}>Назад</button>
        <button class="next" on:click={()=>{$step++}}>Далее</button>
    </div>
</div>
