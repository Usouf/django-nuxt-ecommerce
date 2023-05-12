export default defineEventHandler(async (event) => {

    // handle query params
    const { slug } = event.context.params
    console.log(slug)

    // handle cookies

    // handle body
    // const { age, gender } = await readBody(event)

    // const { currencyKey } = useRuntimeConfig()

    console.log("Fetching products")

    const uri = `http://localhost:8000/products/${slug}`

    const data = await $fetch(uri)

    console.log(data)

    return data
})