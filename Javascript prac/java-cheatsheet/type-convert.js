/* 
    Type  conversion = change thye data type of a value

*/

let age = window.prompt("How old are you?");
// To number
age = Number(age);
age += 1;

console.log("Happy Birthday! You are", age, "years old");
// To string
age = string(age);

// To boolean 
z = Boolean("") //empty strings mean false, could be used to  make sure someone types input with if loop 
x = Boolean("Car") //would return as true