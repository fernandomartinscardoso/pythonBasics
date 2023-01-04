"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 38
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('# Aplicando Aumento de 25% no Salário #')
print('###'*13)
sal = float(input('Digite o salário: R$'))
novo_sal = sal*((100+25)/100)
print('Com um aumento de 25%, o salário passa a ser de R${:.2f}.'.format(novo_sal))
