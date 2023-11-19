"""Gabarito da Lista 4 - Vetores e Matrizes
   Exercício 02
   Programador: Fernando Martins Cardoso
"""

print('###'*19)
print('#    lendo 6 valores aleatórios e mostrando na tela     #'.upper())
print('###'*19)

from random import randint

A = []
for i in range(0,6):
    A.append(randint(0,100))

print(A)
