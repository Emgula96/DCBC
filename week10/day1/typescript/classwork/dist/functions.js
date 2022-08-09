"use strict";
//parameters, arguments, body, return value
const returnTwelve = () => {
    return 12;
};
const returnNumArray = () => {
    return [123, 123, 567];
};
const returnNumArray2 = (num1, num2) => {
    return [num1, num2];
};
const parsePassword = (password) => {
    if (password) {
        return true;
    }
    return false;
};
const clacIncomeTax = (salary, state) => {
    if (state) {
        const total = salary * 1.30;
        return total * 1.20;
    }
    if (salary > 120000)
        return salary * 1.3;
    return salary * 1.25;
};
