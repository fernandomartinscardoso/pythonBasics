"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 49
   Programador: Fernando Martins Cardoso
"""

print('###'*14)
print('#    cálculo do ano de nascimento    #'.upper())
print('###'*14)
from datetime import datetime
idade = int(input('Quantos anos você tem? '))
ano_atual = datetime.now()
print('Você nasceu em {}.'.format((ano_atual.year)-idade))
