"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 29
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#     Cálculo dos 5 primeiros termos da série:    #'.upper())
print('#       S=0+1/2!+2/4!+3/6!+4/8!+...+n/(2n)!       #')
print('###'*17)

from math import factorial
c = 0
s = 0
while c<5:
    s = s + c/factorial(2*c)
    c = c + 1
print('S = {}'.format(s))

