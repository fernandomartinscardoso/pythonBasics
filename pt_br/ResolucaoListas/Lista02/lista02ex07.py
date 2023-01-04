"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 07 - Versão Melhorada do Exercício 01
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('# Verificando o maior de dois números #'.upper())
print('#   Versão melhorada do exercício 01  #')
print('###'*13)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1>n2:
    print('Entre {} e {}, o maior número é {}.'.format(n1, n2, n1))
elif n2>n1:
    print('Entre {} e {}, o maior número é {}.'.format(n1, n2, n2))
else:
    print('Os dois números são iguais.')
