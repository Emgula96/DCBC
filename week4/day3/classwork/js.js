console.log(Howdy)

//ternary operator ?
// const data= if truthy ? do this :  else do this if falsy


const admin = 'rayleigh'
const username = admin === 'joe' ? 'jwfraiser' : 'rrozzier'
console.log(username)



//const loggedIn = username == 'joe' ? 'jwfraiser' : null
//AND operator &&

const loggedIn = username === 'joe' && 'jwfrasier'

//or Operator
// ||

const permittedToStay = loggedIn || 'child';

//add 2 arrays combinedArray = array1.concat(array2)
// spread operator [...array1,...array2]
// make string into a number
//unary operator shorthand make string into numebr
// const notANumber = '1'
// console.log(typeof+notANumber)
//counter ++
//forEach can is shorthand to loop over array

//.map loop or array and returns changes
const upperCaseStudents = students.map((student) => student.toUpperCase())
console.log(upperCaseStudents);

const googleEmployee = {
    name: 'Sundar pichai',
    status: 'ceo',
    salary:' 1 billion dollars',
    projects:[
        {name: 'projext x'},
        {name: 'google fi'},
        {name: 'google maps 2.0'},
    ],
};
    const noogleEmployee ={
        name: 'carlos',
        status: 'noogler',
        salary: 'not a billion',
        department: 'google cloud',
    };
//optional chain ?
    const allGoogle = [googleEmployee, noogleEmployee];    
allGoogle.forEach((emp) => console.log(emp?.project[0]))
console.log(allGoogle)

//.reduce (most powerful)