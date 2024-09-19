a= str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(a.count('A')))
print('A primeira letra A apareceu na posição {}'.format(a.find('A')+1))
print('A última letra A aparece pela última vez na posição {}'.format(a.rfind('A')+1))