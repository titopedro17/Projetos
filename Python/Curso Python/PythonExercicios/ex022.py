nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome possui: {} letras'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))