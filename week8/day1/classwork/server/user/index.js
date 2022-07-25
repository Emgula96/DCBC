const {user} = require("../../database/models")
const express = require("express")
const router = express.Router()
const bcrypt = require("bcrypt")

router.get("/all_users", async (req,res) =>{
const usersToGet = await user.findAll()
res.send(usersToGet);
});
module.exports = router;
router.get("/by_id/:id", async (req,res) =>{
    const {id} = req.params;
const usersToGet = await user.findAll({
    where: {
        id: id,
    },
})
res.send(usersToGet);
});
module.exports = router;


router.post("/create_user", async (req,res) =>{
    const {username, password} = req.body
    try {
        const salt = await bcrypt.genSalt(5)
        const hashedPass = await bcrypt.hash(password,salt)
        const encryptedUser = {
            username: username,
            password:hashedPass,
            createdAt: new Date (),
            updatedAt: new Date(),
        }
        const createUser = await user.create(encryptedUser)
        res.send(createUser)
    } catch (error) {
        res.send(error)
    }
});


router.post("/login", async (req,res) =>{
    const {username, password} = req.body
    try {
        const findUser = await user.findOne({
            where: {
                username: username,
            },
        });
        const userWeFound = findUser.dataValues;
        console.log(userWeFound.password);

        const validated = await bcrypt.compare(password, userWeFound.password);
        // console.log(validated);
        if(!validated){
            res.status(400).send("please enter a valid user/password")
        } else{
            res.status(200).send("Successful login")
        }
    } catch (error) {
        res.status(400).send(error)
    }
});


router.put("/update", async (req,res) =>{
    const {username, password} = req.body
    try {
        const findUser = await user.findOne({
            where: {
                username:username,
            },
        });
        try{
            const salt = await bcrypt.genSalt(5);
            const hashedPass = await bcrypt.hash(password,salt);
            findUser.password = hashedPass;
            findUser.update({
                username: username,
                password: hashedPass,
                updatedAt: new Date(),
            });
            res.send("Password updated");
        } catch (error){
            console.log(error)
            res.status(400).send(error);
        }
    } catch (error){
        console.log(error);
        res.status(400).send(error);
    }
});

router.delete("/delete_user", async (req, res) => {
    const { username, password } = req.body;
    try {
    const findUser = await user.findOne({
        where: {
        username: username,
        // password: password validate since encrypted?
        },
    });
    try {
        findUser.destroy();
        res.send("User deleted");
    } catch (error) {
        console.log(error);
        res.status(400).send(error);
    }
    } catch (error) {
    console.log(error);
    res.status(400).send(error);
    }
});