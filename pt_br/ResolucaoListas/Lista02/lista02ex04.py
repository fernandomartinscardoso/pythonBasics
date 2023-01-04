"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 04
   Programador: Fernando Martins Cardoso
"""

print('###'*15)
print('# O quadrado e a raiz quadrada de um número #'.upper())
print('###'*15)
num = float(input('Digite um número positivo: '))
if num < 0:
    print("Inválido! Número tem que ser positivo.")
else:
    quad = num**2
    raiz = num**0.5
    print('''Quadrado de {} = {}
Raiz quadrada de {} = {}'''.format(num, quad, num, raiz))
