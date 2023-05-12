export const useStore = defineStore('main', {
    state: () => ({
      products: [],
      currentProduct: {},
    }),
    actions: {
      async fetchProducts() {
        const { data } = await useFetch('/api/products')
        console.log("Data: " + data.value)
        if (data.value) {
          console.log("available")
          this.products = data.value;
        }
      },
      async fetchProduct(slug: string) {
        console.log("slug: " + slug)
        const uri = "/api/products/" + slug
        const { data } = await useFetch(uri)
        if (data.value) {
          this.currentProduct = data.value
        } else {
          throw createError({ statusCode: 404, statusMessage: "Couldn't fetch data from server", fatal: true })
        }
      }
    },
    getters: {},
});