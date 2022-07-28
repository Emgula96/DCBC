const express = require("express");
const app = express();
const port = 3004;
const {Users} = require("./sequelize/models/")
const session = require("express-session")
const cookieParser = require("cookie-parser")

app.use(express.json())
app.use(cookieParser());
app.use(
    session({
        secret:"secret",
        resave: false,
        saveUninitialized:true,
        cookie:{
            secure:false,
            maxAge: 2592000000
        }
    })
);


app.post("/login",async(req,res) =>{
    const user = await Users.findOne({
        where:{
            username: req.body.username,
            password: req.body.password,
        }
    })
    res.send(user);
});

app.listen(port, console.log(`listening on ${port}`));