<template>
    <div>
        <div class="grid grid-cols-3 gap-4">
            <div class="col-span-1">
                <div class="grid grid-rows-4 grid-flow-col gap-4">
                    <div class="row-span-3 ...">
                        <img class="p-8 rounded-t-lg w-3/4 mx-auto" :src="image.image" alt=""/>
                    </div>
                    <div class="row-span-1 ...">02</div>
                </div>
            </div>
            <div class="col-span-2">
                
                <div>bye</div>
            </div>
        </div>
    </div>
</template>

<script setup>
    const { product } = defineProps(['product'])
    const image = product.images.find(image => image.preview_image == true);
</script>

<style scoped>

</style>