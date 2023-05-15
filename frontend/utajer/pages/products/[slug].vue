<template>
    <div class="my-12">
        <ProductDetails :product="currentProduct"/>
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { useStore } from '~/stores/main';

const { slug } = useRoute().params

const store = useStore();
const { fetchProduct } = store; // have all non reactive stuff here
const { currentProduct } = storeToRefs(store); // have all reactive states here

await fetchProduct(slug);
</script>

<style scoped>

</style>