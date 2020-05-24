const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const port = 3000
const flag_logic_001 = "DeniceCTF_2020{logic_001_fuk_U_js_HECOBY}"
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.get('/', (req, res) => res.send('Use postman'))
app.post('/', (req, res) =>{
    let {a,b,c,d,e,f,g,h,i,j,k} = req.body
    let check = true;
    if(a == 1 && a +1 == 2){

    }else{
        check = false
    }
    if(b === true){
        if(b == c){

        }else{
            check = false
        }
    }else{
        check = false
    }
    let aa = a + 1
    let bb = b+c
    if(aa == bb){

    }else{
        check = false
    }
    if(d+d === 0.2){

    }else{
        check = false
    }
    if(d+d+d == e){
        
    }else{
        check = false
    }
    if(f.length === 1){
        if(f[0] === "1"){
        
        }else{
            check = false
        }
    }else{
        check = false
    }
    if(9+f[0]===h){
        
    }else{
        check = false
    }
    if(h-f[0] === i){
        
    }else{
        check = false
    }
    f.pop()
    if( (!+f+f+!f).length == g){
        
    }else{
        check = false
    }
    let jj = 99999999999999999999
    if( jj%1000 === j){
        
    }else{
        check = false
    }
    if(typeof(NaN) ==k){
        
    }else{
        console.log(typeof(k))
        check = false
    }
    if(check){
        res.send(flag_logic_001)
    }else{
        res.send("wrong")
    }
})
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
