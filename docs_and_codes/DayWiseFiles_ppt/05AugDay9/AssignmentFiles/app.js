var express = require('express')
var app = express()


app.get("/",(req,res) =>{
	res.send("hello");
})

const PORT = process.env.PORT || 3000;
app.listen(PORT,()=>{
	console.log("Service is running at 3000");	
})
