"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 11
   Programador: Fernando Martins Cardoso
"""

print('###'*22)
print('#    Soma dos algarismos de um número inteiro de três dígitos    #'.upper())
print('###'*22)

n = int(input('Insira um número inteiro positivo de até três dígitos: '))

if n > 0:
    u = n%10
    d = (n%100)//10
    c = n//100
    soma = u + c + d
    print('A soma dos algarismos de {} é igual a {}.'.format(n, soma))
else:
    print('Número inválido!')


