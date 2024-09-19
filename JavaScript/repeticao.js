const prompt = require('prompt-sync')();

// Necessária a instalação do pacote:
// npm install prompt-sync via prompt

var numero = prompt("Insira um valor: ");

if (numero > 10) {
    console.log("É maior que 10")
} else if (numero == 10) {
    console.log("É igual a 10")
} else {
    console.log("É menor que 10")
}