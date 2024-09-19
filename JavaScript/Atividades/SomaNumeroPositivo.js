;

let soma = 0

while(true){
    let numero = parseInt(prompt("Insira um numero: "))
    if(numero >= 0){
        soma += numero
        console.log(numero)
}
else {
    console.log("A soma dos valores é: "+ soma)
    break
}
}