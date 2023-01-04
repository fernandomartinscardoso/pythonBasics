"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 17
   Programador: Fernando Martins Cardoso
"""

print('###'*15)
print('#   Soma dos n primeiros números naturais   #'.upper())
print('###'*15)

n = int(input('Até qual número natural você deseja somar? '))
# Teste se é número natural:
while n<0:
    print('Entrada inválida! Número natural é sempre positivo. Tente novamente!')
    n = int(input('Até qual número natural você deseja somar? '))
s = 0
c = n
while c>0:
    s = s + c
    c = c - 1
print('A soma dos {} primeiros números naturais é igual a {}.'.format(n, s))
