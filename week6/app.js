const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json())

app.get("/users", (req, res) => {
    res.send([{
        name: "John",
        age: 30
    }, {
        name: "Jane",
        age: 25
    }]);
})


app.post("/create_user", (req, res) => {
    console.log(req.body)
    res.send(req.body)
})

app.listen(PORT, console.log(`server is running on port ${PORT}`));
