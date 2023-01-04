"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 19
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#           Divisibilidade por 3 ou por 5            #'.upper())
print('###'*18)

n = int(input('Digite um número inteiro: '))
if n%3 == 0:
    print('{} é divisível por 3'.format(n))
else:
    print('{} não é divisível por 3'.format(n))
if n%5 == 0:
    print('{} é divisível por 5'.format(n))
else:
    print('{} não é divisível por 5'.format(n))
