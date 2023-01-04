"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 50
   Programador: Fernando Martins Cardoso
"""

from math import sqrt
print('###'*18)
print('''#  este programa lê as coordenadas de um ponto no R² #
#  e calcula sua distância até a origem (0,0)        #'''.upper())
print('###'*18)
x = float(input('Insira a coordenada x do ponto: '))
y = float(input('Insira a coordenada y do ponto: '))
d = sqrt(x**2 + y**2)
print('A distância do ponto ({},{}) até a origem é de {:.1f} u. c.'.format(x, y, d))
