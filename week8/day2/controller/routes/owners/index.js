const express = require("express");
const router = express.Router();
const app = express();
const {Owners} = require("../../../sequelize/models")

//middleware
app.use(express.json());

router.get('/get_owners', async (req, res) => {
    const ownerToGet = await Owners.findAll()
    console.log(ownerToGet)
    res.render("owners.html", {locals:{
        Owners: ownerToGet
}})
})
router.post("/create_owner", async (req, res) => {
    res.send("create owner")
});
router.put("/update_owner", async (req, res) => {
    res.send("update owner")
});
router.delete("/delete_owner", async (req, res) => {
    res.send("owner deleted")
});




module.exports = router;