const fizzBuzz = (number:number):string =>{
    if (number%3 ===0 && number%5 ===0)
        return"fizzBuzz";
    if(number%3) 
        return "fizz";
    if (number%5) 
        return "buzz";
    return "no fizz opr buzz";
}

