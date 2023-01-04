"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 12
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#   Impressão de N números naturais   #'.upper())
print('#          Ordem decrescente          #')
print('###'*13)

n = int(input('\nA partir de qual natural você quer ver impresso? '))
c=n
while c>=0:
    print(c)
    c=c-1
