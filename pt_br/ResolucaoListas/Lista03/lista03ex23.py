"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 23
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#      Divisores de um número inteiro positivo       #'.upper())
print('###'*18)

num = int(input('Digite um número inteiro positivo: '))
if num <= 0:
    print('Número inválido!')
else:
    print('Os divisores de {} são:'.format(num))
    c = 1
    while c <= num:
        if num%c == 0:
            print(c)
        c = c + 1
