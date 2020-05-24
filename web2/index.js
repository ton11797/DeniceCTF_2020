const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const port = 3003
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.get('/', (req, res) => res.send('Use postman'))
app.post('/:module', async (req, res) =>{
    const module = require(`./src/${req.params.module}`)
    res.send(await module(req.body))
})
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))