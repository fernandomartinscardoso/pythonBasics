"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 14
   Programador: Fernando Martins Cardoso
"""

from math import pi
print('+++'*15)
print('Conversor de ângulos em graus para radianos')
print('+++'*15)
g = float(input('Digite o ângulo em graus: '))
r = g*pi/180
print('{}° = {:.2f} rad'.format(g, r))
