const express = require('express')
const bodyParser = require('body-parser')
const md5 = require('md5');
const MongoClient = require('mongodb').MongoClient;
const app = express()
const port = 3000
const url = 'mongodb://db:27017';
const dbName = 'CTFweb1';
const client = new MongoClient(url);
const flag_web_002 = "DeniceCTF_2020{web_002_don't_use_md5_use_sha+salt_KYBSCU}"
console.log("change")
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.get('/', (req, res) => res.send('Use postman'))
app.post('/', (req, res) => {
    let { collection } = req.body
    if (collection !== undefined) {
        client.connect(function (err) {
            const db = client.db(dbName);
            db.collection(collection).find({}).toArray(function (err, data) {
                if (err) res.send(err)
                res.send(data)
            });
        });
    } else {
        res.send({ error: "Error key collection missing", detail: `Example {collection:"data"}` })
    }
})

app.post('/login', (req, res) => {
    let { username, password } = req.body
    if (username !== undefined && password !== undefined) {
        client.connect(function (err) {
            const db = client.db(dbName);
            db.collection('user').findOne({ username, password: md5(password) }, function (err, data) {
                if (err) res.send(err)
                console.log(data)
                console.log(md5(password))
                if (data !== null) {
                    res.send(flag_web_002)
                } else {
                    res.send("worng password")
                }
            });
        });
    } else {
        res.send({ error: "Error key fields missing", detail: `Example {username:"",password:""}` })
    }
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
