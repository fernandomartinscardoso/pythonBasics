"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 32
   Programador: Fernando Martins Cardoso
"""

print('###'*19)
print('#       Lançamento de dois dados d1 e d2 n vezes:       #'.upper())
print('#  Informa o valor de cada dado e a relação entre eles  #')
print('###'*19)

from random import randint

n = int(input('\nDigite quantos lançamentos deseja simular: '))
for i in range(1, n+1):
    d1=randint(1, 6)
    d2=randint(1, 6)
    if d1>d2:
        print('Lançamento {}: D1={}, D2={}, D1 maior do que D2.'.format(i, d1, d2))
    elif d1<d2:
        print('Lançamento {}: D1={}, D2={}, D2 maior do que D1.'.format(i, d1, d2))
    else:
        print('Lançamento {}: D1={}, D2={}, D1 igual a D2.'.format(i, d1, d2))