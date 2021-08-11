var express = require('express')
require('dotenv').config();
var app = express()


app.get("/",(req,res) =>{
	res.send("hello");
})

const PORT=process.env.PORT || 3000;

app.listen(PORT,()=>{
	console.log(`Server running at ${PORT}`);
})
