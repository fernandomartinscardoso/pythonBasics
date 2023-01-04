"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 42
   Programador: Fernando Martins Cardoso
"""

print('###'*19)
print('#        Pagamento de salário de um funcionário         #'.upper())
print('# Gratificação de 5% e imposto de 7% sobre salário-base #'.upper())
print('###'*19)
sal_base = float(input('Digite o valor do salário-base: R$'))
salario = sal_base + (5/100)*sal_base - (7/100)*sal_base
print('O salário a receber é igual a R${:.2f}'.format(salario))
