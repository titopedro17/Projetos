from random import randint

velocidade = int(input('Qual é a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você excedeu o limite permitido que é de 80km/h! e terá que pagar uma multa de {} reais!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')