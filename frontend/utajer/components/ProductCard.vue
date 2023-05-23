<template>
    <div class="w-full max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <NuxtLink :to="`/products/${product.slug}`">
            <img class="p-8 rounded-t-lg max-h-52 mx-auto" :src="image.image" alt="product image" />
            <div class="px-5 pb-5">
                <h5 class="text-xl truncate font-semibold tracking-tight text-gray-900 dark:text-white">{{ product.name }}</h5>
                <div class="flex items-center mt-2.5 mb-5">
                    <StarRating :rating="product.rating" :id="product.id" />
                </div>
                <div class="flex items-center justify-between md:flex-wrap sm:flex-wrap">
                    <span class="text-3xl font-bold text-gray-900 dark:text-white md:mb-2">${{ product.price }}</span>
                    <a href="#" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Add to cart</a>
                </div>
            </div>
        </NuxtLink>
    </div>
</template>

<script setup>
    const { product } = defineProps(['product'])
    const image = product.images.find(image => image.preview_image == true)

    const filledStars = computed(() => {
        const filledCount = Math.floor(product.rating);
        const fractionalPart = product.rating - filledCount
        const stars = []

        if (rating === 0) {
            // Handle 0 rating
            for (let i = 0; i < 5; i++) {
                stars.push({ fillPercentage: '0%' });
            }
        } else {
            for (let i = 0; i < 5; i++) {
                if (i < filledCount) {
                    stars.push({ fillPercentage: '100%' });
                } else if (i === filledCount && fractionalPart > 0) {
                    const fillPercentage = Math.round(fractionalPart * 100);
                    stars.push({ fillPercentage: `${fillPercentage}%` });
                } else {
                    stars.push({ fillPercentage: '0%' });
                }
            }
        }

        return stars
    })
</script>

<style scoped>
.star-icon {
  width: 24px;
  height: 24px;
  fill: #faca15; /* Adjust the fill color to your liking */
}
</style>