"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 10
   Programador: Fernando Martins Cardoso
"""

print('###'*15)
print('#   Soma dos 50 primeiros inteiros pares    #'.upper())
print('###'*15)
s = 0
for c in range(1, 51):
    n = 2*c
    s = s + n
print('A soma dos {} primeiros inteiros pares é igual a {}.'.format(c, s))
