import express from "express";
const app = express();
const PORT = 3030;
app.use(express.json())

console.log(`server is running at port ${PORT}`)
app.get("/hello",(req,res)=> {
    res.send("Hello World");
});