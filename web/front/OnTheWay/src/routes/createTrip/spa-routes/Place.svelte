<script lang="ts">
    import {url} from "../../../enviroment";
    import {data, step, activeButton} from "../Common";

</script>


<div class="grey-rect">
    <div class="desc-img">
        {#if $step === 1}
            <p class="dir-desc">Откуда</p>
        {:else}
            <p class="dir-desc">Куда</p>
        {/if}
        <img src="{url}/static/icons/location-pin-alt-svgrepo-com.svg"
             class="dir-image"
             alt="Location Pin"
        />
    </div>
    <div class="but-text">
        {#if $step === 1}
            <div class="buttons">
                <button
                        class="button1"
                        id="left1"
                        on:click={() => {
              data.start_location = "Иннополис";
              data.end_location = "Казань";
              $activeButton = "Иннополис";
            }}
                        style='background-color: {$activeButton === "Иннополис" ? "#969696" : ""}'
                >
                    Иннополис
                </button>
                <button
                        class="button1"
                        id="right1"
                        on:click={() => {
              data.start_location = "Казань";
              data.end_location = "Иннополис";
              $activeButton = "Казань";
            }}
                        style="background-color: {$activeButton === 'Казань' ? '#969696' : ''}"
                >
                    Казань
                </button>
            </div>
            <textarea
                    id="comment1"
                    class="com"
                    placeholder="Уточните место отправления..."
                    bind:value={data.clarify_from}
            />
        {:else}
            <div class="buttons">
                <button
                        class="button1"
                        id="left1"
                        on:click={() => {}}
                        style="background-color: {data.start_location === 'Казань' ? '#969696' : ''}"
                >
                    Иннополис
                </button>
                <button
                        class="button1"
                        id="right1"
                        on:click={() => {}}
                        style="background-color: {data.start_location === 'Иннополис' ? '#969696' : ''}"
                >
                    Казань
                </button>
            </div>
            <textarea
                    id="comment2"
                    class="com"
                    placeholder="Уточните место прибытия..."
                    bind:value={data.clarify_to}
            />
        {/if}
    </div>
</div>
<div class="nav-buttons">
    <button class="next" on:click={() => $step--}>Назад</button>
    <button class="next" on:click={() => {$step++; console.log(data)}}>Далее</button>
</div>
  