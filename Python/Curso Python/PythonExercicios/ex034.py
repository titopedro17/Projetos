salario = float(input('Digite o seu salário: R$'))
if salario > 1250.00:
    novo_salario = (salario*0.1)+salario
    print('Seu novo salário é de R${:.2f}'.format(novo_salario))
else:
    novo_salario = (salario*0.15)+salario
    print('Seu novo salário é de R${:.2f}'.format(novo_salario))