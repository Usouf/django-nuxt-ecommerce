export default defineEventHandler(async (event) => {

    // handle query params
    // const { name } = getQuery(event)

    // handle body
    // const { age, gender } = await readBody(event)

    // const { currencyKey } = useRuntimeConfig()

    console.log("Fetching products")
    
    const uri = 'http://localhost:8000/products/'

    console.log(uri)

    const data = await $fetch(uri)

    return data
})