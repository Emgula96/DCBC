const express = require("express")
const app = express()
const PORT = 3008
// const bcrypt = require("bcrypt")
// const {user} = require("../database/models")
const router = express.Router()

const userRoutes = require("./user")

app.use(express.json())
app.use("/users",userRoutes)

//Examples of stuff

// app.post("/create_user", async (req,res) =>{
//     const {username, password} = req.body
//     try {
//         const salt = await bcrypt.genSalt(5)
//         const hashedPass = await bcrypt.hash(password,salt)
//         const encryptedUser = {
//             username: username,
//             password:hashedPass,
//             createdAt: new Date (),
//             updatedAt: new Date(),
//         }
//         const createUser = await user.create(encryptedUser)
//         res.send(createUser)
//     } catch (error) {
//         res.send(error)
//     }
// });


// app.post("/login", async (req,res) =>{
//     const {username, password} = req.body
//     try {
//         const findUser = await user.findOne({
//             where: {
//                 username: username,
//             },
//         });
//         const userWeFound = findUser.dataValues;
//         console.log(userWeFound.password);

//         const validated = await bcrypt.compare(password, userWeFound.password);
//         // console.log(validated);
//         if(!validated){
//             res.status(400).send("please enter a valid user/password")
//         } else{
//             res.status(200).send("Successful login")
//         }
//     } catch (error) {
//         res.status(400).send(error)
//     }
// });


// app.put("/update", async (req,res) =>{
//     const {username, password} = req.body
//     try {
//         const findUser = await user.findOne({
//             where: {
//                 username:username,
//             },
//         });
//         try{
//             const salt = await bcrypt.genSalt(5);
//             const hashedPass = await bcrypt.hash(password,salt);
//             findUser.password = hashedPass;
//             findUser.update({
//                 username: username,
//                 password: hashedPass,
//                 updatedAt: new Date(),
//             });
//             res.send("Password updated");
//         } catch (error){
//             console.log(error)
//             res.status(400).send(error);
//         }
//     } catch (error){
//         console.log(error);
//         res.status(400).send(error);
//     }
// });

// app.delete("/delete_user", async (req, res) => {
//     const { username, password } = req.body;
//     try {
//     const findUser = await user.findOne({
//         where: {
//         username: username,
//         // password: password validate since encrypted?
//         },
//     });
//     try {
//         findUser.destroy();
//         res.send("User deleted");
//     } catch (error) {
//         console.log(error);
//         res.status(400).send(error);
//     }
//     } catch (error) {
//     console.log(error);
//     res.status(400).send(error);
//     }
// });

app.listen(PORT, console.log(`listening on port ${PORT}`))