"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 37
   Programador: Fernando Martins Cardoso
"""

print('###'*23)
print('#    Números entre 1000 e 9999 que seguem a propriedade abaixo:     #'.upper())
print('#                Ex.: 3025 -> 30+25=55 -> 55²=3025                  #'.upper())
print('###'*23)

print('\nOs números que seguem a propriedade do exemplo são:')
for i in range(1000, 10000):
    sup = i//100
    inf = i%100
    j = (sup + inf)**2
    if i==j:
        print(i)
