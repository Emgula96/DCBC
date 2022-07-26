const express = require("express");
const router = express.Router();
const app = express();


//middleware
app.use(express.json());

router.get("/get_pets", async (req, res) => {
    

    // res.send("get pets")
});
router.post("/create_pets", async (req, res) => {
    res.send("create pets")
});
router.put("/update_pets", async (req, res) => {
    res.send("update pets")
});
router.delete("/delete_pets", async (req, res) => {
    res.send("pet deleted")
});




module.exports = router;