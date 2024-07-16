<script lang="ts">
    import {ComponentType, onMount} from "svelte";
    import Choice from "./spa-routes/Choice.svelte";
    import Place from "./spa-routes/Place.svelte";
    import Time from "./spa-routes/Time.svelte";
    import Options from "./spa-routes/Options.svelte";
    import Vehicle from "./spa-routes/Vehicle.svelte";
    import Cars from "./spa-routes/Cars.svelte";
    import Form from "./spa-routes/Form.svelte";
    import "./createTrip.css";
    import {data, step} from "./Common";

    const routes: { [key: string]: ComponentType } = {
        '/': Choice,
        '/from': Place,
        '/to': Place,
        '/time': Time,
        '/options': Options,
        '/cars': Vehicle,
        '/myCars': Cars,
        '/submission': Form,
    };

    const steps = [
        '/',
        '/from',
        '/to',
        '/time',
        '/cars',
        '/myCars',
        '/options',
        '/submission',
    ]

    onMount(()=>{
        data.driver_id = window.Telegram.WebApp.initDataUnsafe.user.id;
    })
</script>

<div id="content-wrap">
    {#key step}
        <svelte:component this={routes[steps[$step]]} />
    {/key}
</div>