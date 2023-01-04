"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 35
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#           Soma dos números ímpares              #'.upper())
print('#       dentro de um intervalo solicitado         #'.upper())
print('###'*17)

i = int(input('Digite o valor inicial: '))
j = int(input('Digite o valor final: '))
if i>j:
    print('Valores inválidos!')
else:
    s = 0
    for c in range(i, j+1):
        if c%2==1:
            s = s + c
    print('A soma dos ímpares no intervalo de {} a {} é igual a {}.'.format(i, j, s))
