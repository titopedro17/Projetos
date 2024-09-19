from math import sin,cos,tan, radians
a = float(input('Digite o valor do ângulo em graus: '))
sen = sin(radians(a))
cos = cos(radians(a))
tg = tan(radians(a))
print('O valor do seno é {:.2f}'.format(sen))
print('O valor do cosseno é {:.2f}'.format(cos))
print('O valor da tangente é {:.2f}'.format(tg))