km=float(input('Qual a quantidade de km percorridos? '))
dia=float(input('Qual a quantidade de dias que o carro foi alugado? '))
preço=(dia*60) + (km*0.15)
print('O total a pagar é de R${:.2f}'.format(preço))