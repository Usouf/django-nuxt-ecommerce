<template>
    <div>
        <header class="shadow-sm bg-white">
            <Nav />
        </header>

        <div class="container mx-auto p-4">
            <slot />
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})
</script>

<style>
    .exact-active {
        color: primary
    }

    .active {
        color: #12b488
    }
</style>