salario = float(input('Qual o salário do funcionário? R$'))
if salario > 1250:
    novo_sal = salario*1.1
else:
    novo_sal = salario*1.15
print('Quem recebia R${:.2f} passa a receber R${:.2f}.'.format(salario, novo_sal))
