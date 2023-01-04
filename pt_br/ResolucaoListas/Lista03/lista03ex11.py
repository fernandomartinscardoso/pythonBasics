"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 11
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#   Impressão de N números naturais   #'.upper())
print('#           Ordem crescente           #')
print('###'*13)

n = int(input('\nAté qual número natural você quer ver impresso? '))
c=0
while c<=n:
    print(c)
    c=c+1
