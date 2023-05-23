<template>
    <div>
        <p>Products</p>
        <div class="grid md:grid-cols-4 grid-cols-1 gap-5">
            <div v-for="p in products" :key="p.id">
                <ProductCard :product="p" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { useStore } from '~/stores/main';

const store = useStore();
const { fetchProducts } = store; // have all non reactive stuff here
const { products } = storeToRefs(store); // have all reactive states here

await fetchProducts();
</script>

<style lang="scss" scoped>

</style>