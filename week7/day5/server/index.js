const express = require("express")
const {User, Longboard, Order} = require("../database/models")
const app = express()
const PORT = 3009


//middleware
app.use(express.json())

//crud
app.post("/user",async (req,res)=>{
    //destructuring
    const {firstName, lastName, email, password } = req.body;
    const userToCreate = {
        firstName,
        lastName,
        email,
        password,
        createdAt: new Date(),
        updatedAt: new Date()
    }
    
    try {
        const user = await User.create(userToCreate);
        // const user = await User.create({
        //     firstName: req.body.firstName,
        //     lastName: req.body.lastName,
        //     email: req.body.email,
        //     password: req.body.password,
        //     createdAt: new Date(),
        //     updatedAt: new Date(),
        // });
        res.status(200).send(user)
    } catch (error) {
        res.status(400).send(error);
    }
});


app.post("/longboard", async (req,res)=>{
    res.send("longboard")
    const {name, brand, length} = req.body;
    const boardToCreate = {
        name,
        brand,
        length,
        createdAt: new Date(),
        updatedAt: new Date()
    }
    
    try {
        const longboard = await Longboard.create(boardToCreate);
        res.status(200).send(longboard)
    } catch (error) {
        res.status(400).send(error);
    }
});


app.post("/order",(req,res)=>{
    res.send("order")
});



app.listen(PORT,console.log(`listening on port ${PORT}`))