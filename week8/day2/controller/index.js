const express = require("express");
const app = express();
const cors = require("cors");
const petRoutes = require("./routes/pets")
const ownerRoutes = require("./routes/owners")
const PORT = 3007;
const es6Renderer = require("express-es6-template-engine")

//middleware
app.use(express.json());
app.use(cors());
app.use("/pets", petRoutes)
app.use("/owners",ownerRoutes)
app.use(express.static("public"))
app.engine("html", es6Renderer)
app.set("views", "./public/views")
app.set("view engine", "html")



app.listen(PORT, console.log(`listening on ${PORT}`));
