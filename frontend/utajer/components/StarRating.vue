<template>
    <div class="flex flex-wrap">
        <span v-for="(star, index) in filledStars" :key="index">
            <svg class="star-icon" viewBox="0 0 24 24">
                <defs>
                <linearGradient :id="`starGradient${index}-${id}`" x1="0" y1="0" x2="100%" y2="0">
                    <stop :offset="star.fillPercentage" stop-color="#ffc107" />
                    <stop :offset="star.fillPercentage" stop-color="#e0e0e0" />
                </linearGradient>
                </defs>
                <path :style="{ fill: `url(#starGradient${index}-${id})` }" d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
            </svg>
        </span>
        <span class="bg-blue-100 text-blue-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800 ml-3">{{ rating }}</span>
    </div>
</template>

<script setup>
    import { computed } from 'vue'

    const { rating, id } = defineProps(['rating', 'id'])


    const filledStars = computed(() => {
        const filledCount = Math.floor(rating);
        const fractionalPart = rating - filledCount;
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