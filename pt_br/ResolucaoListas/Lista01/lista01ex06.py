"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 06
   Programador: Fernando Martins Cardoso
"""

print('***'*19)
print('conversor de temperaturas (graus celsius para fahrenheit)'.title())
print('***'*19)
c = float(input('Digite a temperatura em graus Celsius: '))
f = c*9/5 + 32
print('{}°C = {}°F'.format(c, f))
