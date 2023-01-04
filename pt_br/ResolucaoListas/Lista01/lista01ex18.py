"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 18
   Programador: Fernando Martins Cardoso
"""

print('###'*15)
print('#  Conversor de metros cúbicos para litros  #')
print('###'*15)
mc = float(input('Digite o valor em metros cúbicos: '))
l = 1000*mc
print('{} m³ = {:.0f} l'.format(mc, l))
