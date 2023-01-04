"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 19
   Programador: Fernando Martins Cardoso
"""

print('###'*15)
print('#  Conversor de litros para metros cúbicos  #')
print('###'*15)
l = float(input('Digite o valor em litros: '))
mc = l/1000
print('{} l = {:.3f} m³'.format(l, mc))
