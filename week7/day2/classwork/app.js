import express from "express"
const app = express()
const PORT = 3001



import es6Renderer from "express-es6-template-engine";
app.engine('html', es6Renderer);
app.set('views', 'templates');
app.set('view engine', 'html');



//routes
app.get("/", (req,res) => {
    // res.send("Hello from Express!");
    const user = {name: "JOE"};
    res.render('home',{locals: {user} });
})
app.get("/about", (req,res) => {
    // res.send("Hello from Express!");
    res.render('about')
})
app.get("/user", (req,res) => {
    // res.send("Hello from Express!");
    res.render('user/user')
})

app.post("/home", (req,res) => {
    res.send("Hello from Express!");
})


app.listen(PORT, console.log(`listening on port ${PORT}`))
