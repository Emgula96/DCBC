const express = require('express')

const { Restaurant, Reviewer, Review } = require('./models')
const app = express()
const PORT = process.env.PORT || 3000

app.get('/', (req, res) => {
    res.send('Yay it worked')
})

app.get('/restaurants', async (req, res) => {
    const restaurant = await Restaurant.findAll()
    res.send(restaurant)
})

app.listen(PORT, () => console.log(`listening on port ${PORT}`))