"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 07
   Programador: Fernando Martins Cardoso
"""

print('***'*19)
print('conversor de temperaturas (graus fahrenheit para celsius)'.title())
print('***'*19)
f = float(input('Digite a temperatura em graus Fahrenheit: '))
c = 5*(f - 32)/9
print('{}°F = {}°C'.format(f, c))
