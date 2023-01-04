"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 45
   Programador: Fernando Martins Cardoso
"""

print('###'*16)
print('#     Invertendo números de três dígitos       #'.upper())
print('###'*16)
n = int(input('Digite um número inteiro de três dígitos: '))
u = n%10
d = (n%100 - u)/10
c = (n%1000 - d*10 - u)/100
n_inv = u*100 + d*10 + c
print('Número Lido: {}'.format(n))
print('Número Gerado: {:.0f}'.format(n_inv))

