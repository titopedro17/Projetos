const prompt = require("prompt-sync")();

var numero = prompt("Insira um valor: ")

result = numero > 10 ? 'maior' : 'menor';
console.log(result)