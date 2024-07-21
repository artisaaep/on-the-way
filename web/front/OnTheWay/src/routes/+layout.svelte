<script lang="ts" xmlns="http://www.w3.org/1999/html">
    import "../app.css";
    import {url} from "../enviroment";
    import "../app.css";
</script>

<div id="page-container">
    <slot/>
</div>

<style>
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