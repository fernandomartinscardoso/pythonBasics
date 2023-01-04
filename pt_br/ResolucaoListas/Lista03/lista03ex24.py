"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 24
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#     Este programa calcula a soma dos divisores     #'.upper())
print('#       de um número, com exceção dele próprio       #'.upper())
print('###'*18)

num = int(input('Digite um número inteiro positivo: '))
if num <= 0:
    print('Número inválido!')
else:
    c = 1
    s = 0
    while c < num:
        if num%c == 0:
            s = s + c
        c = c + 1
print('A soma dos divisores de {}, com exceção dele mesmo, é igual a {}.'.format(num, s))
