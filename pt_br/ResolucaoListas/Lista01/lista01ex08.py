"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 08
   Programador: Fernando Martins Cardoso
"""

print('***'*18)
print('conversor de temperaturas (kelvin para graus celsius)'.title())
print('***'*18)
k = float(input('Digite a temperatura em kelvin: '))
c = k - 273.15
print('{} K = {:.2f}°C'.format(k, c))
