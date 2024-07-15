<script lang="ts">
    import { setContext } from "svelte"
    import { isOpen, id } from "./store"
    const modalId = $$props.$$slots.default[0].name;
    setContext("modalId", modalId)
</script>

<div>
    <slot />
</div>

