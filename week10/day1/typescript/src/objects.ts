// let user:object = {
//     name: "joe",
// }

//type alias
type User = {
    name:string
    username:string,
    age: number,
    emailAdress:string;
};

let amanda: User = {
    name:"Amanda",
    username:"Agrove",
    age: 22,
    emailAdress: "lizardCoder@beji.com"
}


type Carpenter = {
    companyName:string;
    readonly id: number;
};

let carlos:Carpenter = {
    companyName:"ABC Company",
    id:1001,
}

const listOfCarpenters:Carpenter[] = []
listOfCarpenters.push(carlos)

type Password = {
    password: string | number
}

type SoftwareEgineer ={
    readonly id:number
    password: Password
}

// const Blke: SoftwareEgineer = {
//     id: 122021,
//     password: {
//         password: 7777,
//         securityClearance: "Top Secret"
//     }
// }



type Clearancelevel = {
    level: "Basic" | "top Secret"
}

type Basicuser = {
    id: number
    password:Password
    email: string
    createdAt:Date
    updatedAt:Date
}

type MasterUser = {
    id: number
    password:Password
    email: string
    createdAt:Date
    updatedAt:Date
    clearanceLevel: Clearancelevel
}

const listOfUsers:MasterUser | Basicuser[] = []