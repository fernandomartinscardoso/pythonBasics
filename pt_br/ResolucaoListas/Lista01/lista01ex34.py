"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 34
   Programador: Fernando Martins Cardoso
"""

from math import pi
print('---'*11)
print('| Cálculo da Área de um Círculo |')
print('---'*11)
r = float(input('Digite o raio do círculo (em cm): '))
a = pi*r**2
print('A área do círculo de raio {} cm é igual a {:.2f} cm².'.format(r, a))
