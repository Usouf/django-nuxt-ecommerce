<template>
    <div>
        Order number: {{ uuid }}
    </div>
</template>

<script setup>
    const { uuid } = useRoute().params
</script>

<style lang="scss" scoped>

</style>