a = int(input('Digite um número: '))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 % 10
print('Analisando o número: {}'.format(a))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))



#separar os números em decimais, milhar, dezena, centena etc