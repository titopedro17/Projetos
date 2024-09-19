const prompt = require('prompt-sync')();

var semaforo = prompt("Insira uma cor: ");

if (semaforo === 'verde') {
    console.log('Pode passar')
    // Pode passar
} else if (semaforo === 'vermelho') {
    console.log('Pare')
} else if (semaforo === 'amarelo') {
    console.log('Atenção')
} else {
    console.log('Cor inválida')
}