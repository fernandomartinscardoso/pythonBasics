"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 01
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('# Verificando o maior de dois números #'.upper())
print('###'*13)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1>n2:
    print('Entre {} e {}, o maior número é {}.'.format(n1, n2, n1))
else:
    print('Entre {} e {}, o maior número é {}.'.format(n1, n2, n2))
