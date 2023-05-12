// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    css: ['~/assets/css/main.css'],
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
    router: {
        options: {
            linkActiveClass: "active",
            linkExactActiveClass: "exact-active"
        }
    },
    modules: [
        [
            '@pinia/nuxt',
            {
                autoImports: ['defineStore', 'acceptHMRUpdate']
            },
        ],
    ],
    imports: {
        dirs: ['stores'],
    }
})
