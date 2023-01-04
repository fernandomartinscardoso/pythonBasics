"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 15
   Programador: Fernando Martins Cardoso
"""

from math import pi
print('+++'*15)
print('Conversor de ângulos em radianos para graus')
print('+++'*15)
r = float(input('Digite o ângulo em graus: '))
g = r*180/pi
print('{} rad = {:.2f}°'.format(r, g))
