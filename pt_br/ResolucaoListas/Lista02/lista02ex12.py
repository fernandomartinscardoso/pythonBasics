"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 12
   Programador: Fernando Martins Cardoso
"""

print('###'*16)
print('#    Logaritmo de números em qualquer base     #'.upper())
print('###'*16)

from math import log
x = float(input('Digite o logaritmando: '))
base = float(input('Digite a base do logaritmo: '))
if x>0 and base>0:
    log = log(x, base)
    print('O logaritmo de {} na base {} é igual a {:.2f}'.format(x, base, log))
else:
    print('Erro! Tanto o logaritmando quanto a base devem ser positivos.')
