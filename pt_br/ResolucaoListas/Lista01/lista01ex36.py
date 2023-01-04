"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 36
   Programador: Fernando Martins Cardoso
"""

from math import pi
print('** '*12)
print('Cálculo do Volume de um Cilindro')
print('** '*12)
r = float(input('Digite o raio da base (em cm): '))
h = float(input('Digite a altura do cilindro (em cm): '))
vol = pi*r**2*h
print('O volume do cilindro de altura {} cm e raio da base {} cm é igual a {:.2f} cm³.'.format(h, r, vol))
