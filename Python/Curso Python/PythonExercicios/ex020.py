from random import shuffle
a = input('Digite o nome de um aluno: ')
b = input('Digite o nome de outro aluno: ')
c = input('Digite o nome de outro aluno: ')
d = input('Digite o nome de outro aluno: ')
aluno = [a, b, c, d]
shuffle(aluno)
print('A ordem de apresentação dos trabalhos será: ')
print(aluno)
