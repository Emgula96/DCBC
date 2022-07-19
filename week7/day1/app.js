import express from "express";
const app = express();
const PORT = 3000
app.use(express.json())

// routes
//routes will haev its http method on it get--get, post--post, etc--etc
//it will alwys includde in this order
// a req and a res
app.get("/", (req, res)=> {
    //inside this function body you can do whatever
    res.send("this is the home page");
});

app.get("/benji",(req,res)=> {
    res.send("lizard");
});

app.post("/beer",(req,res)=>{
    res.send("beer");
});

app.post("/create_user",(req,res)=>{
    res.send(`created user ${req.body.name}`);
})



app.listen(PORT,console.log(`listening on port ${PORT}`));


import * as cowsay from "cowsay";


app.get("/cow",(req,res)=>{
    res.send(
        cowsay.say({
            text:"i turn to borger",
            e: "oO",
            T: "U",
        }))
})

app.post("/cow2",(req,res)=>{
    res.send(
        cowsay.say({
            text:(`${req.body.text}`),
            e: (`${req.body.e}`),
            T: (`${req.body.T}`)
        }))
})