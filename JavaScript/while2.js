const prompt = require("prompt-sync")();

cont = 0

a = prompt("Insira um valor: ")
while(cont <=10){
    console.log(cont, " * ", a, " = ", cont*a);
    cont++
}