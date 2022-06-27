// let count = 0;
// count =1;
// count =2;
// count =3;


// function incrementNumber(number){
//     let total = number + 1;
//     return total;
// }
// incrementNumber();

// //ES6 way of writing funciton

// const arrowInc = (number) => {
//     let total = number +1;
//     return total;
// };

// const palindrome  = (word) => {
//     if(typeof word === "string"){
//     console.lot("its a string")
//     }
// };
// // a function thaty recieves a function as an argument
// const funkyfunk = (argument) =>{
//     console.log(argument);
//     argument("racecar");
// }
// //a function by reference
// //palindrome;

// funkyfunk(palindrome);


// const finUserInDataBase = (user) => {
//     console.log(user())
// }

// const whatUser =() => {
//     //does some async code
//     return{name:"joe"}
// }

// finUserInDataBase(whatUser);

//make a tip cal recieves total and percente return new total
//calc only total bill if above 100 %30 if between 50 99 25%
//below 50 20%

// const tipCalc = (billTotal,tipPerc) => {
//     let tip = billTotal*tipPerc;
//     let newTotal = billTotal + tip;
//     return newTotal.toFixed(2)
// }

// const newTipCalc = (billTotal) => {
//     if (billTotal > 100) {
//         let tip = billTotal*.30
//         let newTotal = billTotal+tip
//         console.log(newTotal)
//     };
//     if (50 < billTotal < 99 ) {
//         let tip = billTotal*.25
//         let newTotal = billTotal+tip
//         console.log(newTotal)
//     };
//     if (billTotal < 50) {
//         let tip = billTotal*.20
//         let newTotal = billTotal+tip
//         console.log(newTotal)
//     };
// };

// (newTipCalc(120))


// const totalPlusTip = (total) =>{
//     let mealTotal = 0
//     if (total <= 100){
//         mealTotal = total + total*0.3;
//     }
//     if (total <= 99 && total >= 50) {
//         mealTotal = total + total *.25
//     }
//     if (total < 50) {
//         mealTotal = total + total*.02
        
//     }
//     return mealTotal.toFixed(2);
// };

// totalPlusTip(120.67)



// create a function that receives a number
// the number is guaranteed to be in the range of 1 to 5
// time slot, "7:30PM"
// (1, "7:30pm")

// function makeAReservation (vipStatus, timeslot){}
// if the vipStatus is a 4-5, they  are placed in the list first
// if it is 3, they are placed second
// anything below three is placed last
// you will run this function 3 times, with 3 different data sets
// 5
// 3
// 1
// output [ {vipStatus: 5, timeslot: "7:30pm"},{vipStatus: 3, timeslot: "7:30pm"},{vipStatus: 1, timeslot: "7:30pm"}]


// const reservationsList =[];
// const vipData =[
//     {number: 5, timeslot:"7:30"},
//     {number: 3, timeslot: "5:30"},
//     {number: 1, timeslot: "3:30pm"},
// ];

// const makeAReservation = (vipSatus, timeslot) =>{
//     // if(vipSatus => 4){
//         let reservationGuest ={
//             status:vipSatus,
//             time: timeslot,
//         };
//         reservationsList.push(reservationGuest)
//     }
// for (let index = 0; index < vipData.length; index++) {
//     makeAReservation(vipData[index].number, vipData[index].timeslot);
//     }
// reservationsList.sort((a,b) => b.vipSatus - a.vipSatus);
// console.log(reservationsList);



function lvl5exercise1() {
  // Push the string "hello" into the array and return the array
var arr = [1, "adam"];
arr.push('hello')
return arr
}
console.log(lvl5exercise1())

function lvl5exercise2() {
  // Remove the last element from the array and return the array
var arr = [1, "adam"];
arr.pop()
return arr
}
console.log(lvl5exercise2())

function lvl5exercise3() {
  // Return the length of the array
var arr = [1, "adam"];
let length = arr.length
return length
}
console.log(lvl5exercise3())


function lvl5exercise4() {
  // Return the index of item "adam" in the array
var arr = [1, "adam"];
let index = arr.indexOf("adam")
return index
}
console.log(lvl5exercise4())

function lvl6exercise1(num) {
  // Return 'hello' if num is 1, 'world' if num is 2, otherwise return 'bye'
switch(num){
    case 1:
        return "hello";
    case 2: 
        return "world";
    default:
        return "goodbye";
}
}


function lvl6exercise2() {
  // Push 10 'hello' strings into the array using a for loop, then return it
var arr = [];
for (let index = 0; index < 10; index++) {
    arr.push('Hello')
}
return arr
}
console.log(lvl6exercise2())

function lvl6exercise3() {
  // Empty this array using a while loop and return it
var arr = [
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    
];

while(arr.length > 0){
    arr.pop()
}
return arr
}
console.log(lvl6exercise3())
// Write a function that takes a number as an input.
// Have it create an empty array and then push a string into the array as many
// times as the input number. If the input is anything other than a positive
// integer return an empty array
//
// Name the function "finalFunction"

const finalFunction = (number) => {
    const emptyArr = [];
    for (let index = 0; index < number; index++) {
        emptyArr.push('hello');
    }
    return emptyArr
}
console.log(finalFunction(-1));

const mul = (num1, num2,num3) => {
    let finalNum = num1 * num2 *num3
    return finalNum
}
console.log(mul(2,3,4))

function mul(a) {
    return function (b){
        //anonymous function
        return function(c){
        //anonymous function
            return a * b * c;
        };
    };
}

