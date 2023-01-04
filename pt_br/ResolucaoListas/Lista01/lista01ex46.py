"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 46
   Programador: Fernando Martins Cardoso
"""

print('###'*16)
print('#   Descrevendo um número de quatro dígitos    #'.upper())
print('###'*16)
n = int(input('Digite um número de quatro dígitos: '))
m = n//1000
c = (n%1000)//100
d = (n%100)//10
u = n%10
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(u, d, c, m))
