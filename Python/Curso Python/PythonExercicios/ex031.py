distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a comear uma viagem de {}'.format(distancia))
if distancia <= 200:
    passagem = (0.50*distancia)
    print('O preço da passagem será de {:.2f} reais'.format(passagem))
else:
    passagem = (0.45*distancia)
    print('O preço da passagem será de {:.2f} reais'.format(passagem))