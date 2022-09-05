// A variable is a container for storing data
// A variable behaves as if it was the value that it contains 

// Two steps:
//1. Declare (var, let, const)
//2. Assign (= assignment operator)
// Number
/*let age; can be done on two lines or one
age = 21;*/

let age = 21;

//string (letters)
let firstName = "Kyle";

//Boolean (True or False)
/* if student ||
//let student = true;*/

//if not student ||
let student = false;

console.log(firstName);
console.log(age);
console.log(student);

document.getElementById("p1").innerHTML = "Hello " + firstName;
document.getElementById("p2").innerHTML = "You are " + age + " years old";
document.getElementById("p3").innerHTML = "Enrolled: " + student;