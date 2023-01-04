"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 06
   Programador: Fernando Martins Cardoso
"""

print('###'*10)
print('#    Média de 10 inteiros    #'.upper())
print('###'*10)
s = 0
for c in range(1, 11):
    n = int(input('Digite o {}º valor: '.format(c)))
    s = s + n
media = s/c
print('Média = {:.1f}'.format(media))
