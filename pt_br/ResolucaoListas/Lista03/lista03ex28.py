"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 28
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#     Cálculo do número neperiano pela série:     #'.upper())
print('#        e=1+1/1!+1/2!+1/3!+1/4!+...+1/n!         #')
print('###'*17)

from math import factorial
n = int(input('Digite quantos termos da série devem ser somados: '))
e = 0
for i in range(0, n):
    e = e + 1/factorial(i)
print('''Para {} termos, temos que o valor aproximado do número neperiano é dado por:
e = {}'''.format(n, e))
