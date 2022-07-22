const express = require('express');
const {User} = require("./models");
const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
    res.send("Hello World!");
});

//read all users
app.get("/users", async (req, res) => {
    //user find all using aync await
    const users = await User.findAll();
    res.send(users);
});


//read user by id
app.get("/users/:id", async (req, res) => {
    const id = req.params.id
    const user = await User.findByPk(id);
    res.send(user);
    // const users = await User.findAll();
    // res.send(users);
});

//read user by name


//update user


app.listen(port, () => console.log(`Listening on port ${port}`));

