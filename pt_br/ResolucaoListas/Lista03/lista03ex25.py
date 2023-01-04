"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 25
   Programador: Fernando Martins Cardoso
"""

print('###'*15)
print('#     Soma dos naturais menores que 1000    #'.upper())
print('#         que são múltiplos de 3 ou 5       #'.upper())
print('###'*15)

s = 0
for c in range(0, 1001):
    if c%3==0 or c%5==0:
        s = s + c
print('A soma dos naturais de 0 a 1000 que são múltiplos de 3 ou 5 é igual a {}.'.format(s))
