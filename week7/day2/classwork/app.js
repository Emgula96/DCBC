import express from "express"
const app = express()
const PORT = 3001



import es6Renderer from "express-es6-template-engine";
//middleware
app.engine('html', es6Renderer);
app.set('views', 'templates');
app.set('view engine', 'html');
//this line lets us use local pathing for out html and css
app.use(express.static("public"));
app.use(express.json())

//routes
app.get("/", (req,res) => {
    // res.send("Hello from Express!");
    const user = {name: "JOE"};
    res.render('home',{locals: {
        user: user, 
        teacher: "JOE",
        students: ["Amanda", "Carlos"],
    } 
});
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
