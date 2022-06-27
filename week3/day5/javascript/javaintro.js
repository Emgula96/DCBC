// console.log("hello");
// comment
//variable
// let, var, const
// let and var can be reasigned to different data types
// const can only be the value is isnt assigned and nothing else
// it can have stuff added to it
//arrays or lists are the same as they were is pytrhon and you acess them the same way via index
// objects are dictionaries


const student = {
    name:"Ethan",
    id: 3
};

// let rahmin = 'gamer';
// var carlos = 'meme lord';
// const jason = 'windows progblem guy';
// const students =["Olivia","Andrea", "Amanda"];
// rahmin = "engineer";
// console.log('rahmin');
// console.log(jason);
// console.log(students[1]);
// console.log(student["name"]);
// console.log(student.name);

// for loop in array for..of
const restaurants = ["whataburger","mala","tofuVillage"];
console.log(restaurants[2]);
console.log(restaurants.at(-1));

for (let restaurant of restaurants){
    console.log(restaurant);
}
// oldest way and most precise
// for (let index = 0; index < array.length; index++) {
//     const element = array[index];
    
// }



// for loop used for an object. the for ..in loop
for (let key in student){
//  this prints every key
    console.log(key)
    // this prints out every object
    console.log(student[key]);
}

function TwoSum (name,sum,number,username){
    let name ="rayleigh"
    name = 'not the ta anymore'
    return "she cant be our ta ever again";
}