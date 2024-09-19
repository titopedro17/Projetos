from math import hypot
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjascente: '))
hipotenusa= hypot(cat_op, cat_adj)
print('A medida da hipotenusa é {:.2f}:'.format(hipotenusa))