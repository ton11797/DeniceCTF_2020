const fs = require('fs');
module.exports = function(input){
    let {filename,content} = input
    if(filename.toLowerCase().indexOf("read") === -1 && filename.toLowerCase().indexOf("write") === -1 && filename.toLowerCase().indexOf("index") === -1){
        fs.writeFile(`./file_store/${filename}`, content, function (err) {
            if (err) return console.log(err);
        });
        return "done"
    }else{
        return "not allow word read or write in filename"
    }

};