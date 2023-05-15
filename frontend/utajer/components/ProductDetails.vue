<template>
    <div>
        <div class="grid grid-cols-3 gap-4">
            <div class="col-span-1">
                <div class="grid gap-4">
                    <div class="mb-8">
                        <img class="h-auto max-w-full rounded-lg" :src="image.image" alt="">
                    </div>
                    <div class="grid grid-cols-5 gap-4">
                        <div v-for="img in product.images" :key="img.id">
                            <img class="h-auto max-w-full rounded-lg my-auto" :src="img.image" alt="">
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-span-2">
                <div class="px-4 mx-auto max-w-2xl">
                    <h2 class="mb-2 text-xl font-semibold leading-none text-gray-900 md:text-2xl dark:text-white">{{ product.name }}</h2>
                    <p class="mb-4 text-xl font-extrabold leading-none text-gray-900 md:text-2xl dark:text-white">$ {{ product.price }}</p>
                    <dl>
                        <dt class="mb-2 font-semibold leading-none text-gray-900 dark:text-white">Details</dt>
                        <dd class="mb-4 font-light text-gray-500 sm:mb-5 dark:text-gray-400">{{ product.description }}</dd>
                    </dl>
                    <dl class="flex items-center space-x-6">
                        <div>
                            <dt class="mb-2 font-semibold leading-none text-gray-900 dark:text-white">Category</dt>
                            <div v-for="cat in product.categories" :key="cat.id">
                                <dd class="mb-4 font-light text-gray-500 sm:mb-5 dark:text-gray-400">{{ cat.name }}</dd>
                            </div>
                        </div>
                    </dl>
                    <div class="flex items-center space-x-4">
                        <label for="quantity" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Qty</label>
                        <select id="quantity" class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 w-32">
                            <option selected>0</option>
                            <option v-for="index in product.stock" :key="index" value="index">{{ index }}</option>
                        </select>
                        <button type="button" class="text-white inline-flex items-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                            
                            <svg aria-hidden="true" class="mr-1 ml-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z"></path><path fill-rule="evenodd" d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z" clip-rule="evenodd"></path></svg>
                            Add to cart
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    const { product } = defineProps(['product'])
    const image = product.images.find(image => image.preview_image == true)


</script>

<style scoped>

</style>