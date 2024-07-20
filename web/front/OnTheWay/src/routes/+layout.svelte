<script lang="ts" xmlns="http://www.w3.org/1999/html">
    import "../app.css";
    import {url} from "../enviroment";
</script>

<div id="page-container" style="
        --font-reg: url('{url}/static/fonts/Kreadon-Regular.ttf');
        --font-regular: url('{url}/static/fonts/Kreadon-Regular.ttf');
        --font-medium: url('{url}/static/fonts/Kreadon-Medium.ttf)');
        --font-demi: url('{url}/static/fonts/Kreadon-demi.ttf');
    ">
    <slot/>
</div>

<style>
    @font-face {
        font-family: Kreadon_regular;
        src: var(--font-reg);
    }

    @font-face {
        font-family: Kreadon_bold;
        src: var(--font-bold);
    }

    @font-face {
        font-family: Kreadon_demi;
        src: var(--font-demi);
    }

    @font-face {
        font-family: Kreadon_medium;
        src: var(--font-medium);
    }

    #page-container {
        position: relative;
        min-height: 100vh;
        min-width: 90vw;
        height: 100%;
        width: 100%;
        margin: 0;
        padding: 0;
        justify-content: center;
        background-color: white;
        color: black;
        font-family: Kreadon_regular;
    }
</style>