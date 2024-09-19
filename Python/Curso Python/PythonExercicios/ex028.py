from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Bem vindo ao Guess the Number!Vou pensar em um número de 0 a 5 e você tentará adivinhar!')
print('-=-' * 20)
chute = int(input('Em que número eu pensei? '))
if chute == computador:
    print('Parabéns! Você conseguiu me vencer! O número processado foi {}'.format(computador))
else:
    print('Você perdeu! O número processado foi {}'.format(computador))

