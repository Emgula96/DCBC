//parameters, arguments, body, return value

const returnTwelve = ():number =>{
    return 12;
};

const returnNumArray = ():number[] =>{
    return [123,123,567];
};
const returnNumArray2 = (num1:number,num2:number):number[] =>{
    return [num1,num2];
};

const parsePassword = (password:string |number):boolean => {
    if(password){

        return true;
    }
    return false
};

const clacIncomeTax = (salary:number, state?:string):number =>{
    if(state){
        const total = salary*1.30
        return total*1.20;
    }
    if(salary >120_000)
        return salary* 1.3;
    return salary*1.25;
};


