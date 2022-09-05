// How to accet user input 
// Easy way with a window prompt
let username = window.prompt("What's your name?");
console.log(username);



// Difficult way with HTML Textbox

document.getElementById("myButton").onclick = function(){

    username = document.getElementById("myText").value;
    console.log(username);
    document.getElementById("myLabel").innerHTML = "Hello " + username;
}