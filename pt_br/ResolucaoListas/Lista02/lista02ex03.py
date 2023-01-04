"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 03
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#  Calculando a raiz quadrada de um número positivo  #'.upper())
print('#        ou o quadrado de um número negativo         #'.upper())
print('###'*18)

n = float(input('Digite um número: '))
if n<0:
    quad = n**2
    print('O quadrado de {} é igual a {}.'.format(n, quad))
elif n>0:
    raiz = n**0.5
    print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, raiz))
else:
    print('A raiz ou o quadrado de 0 é igual a 0.')
