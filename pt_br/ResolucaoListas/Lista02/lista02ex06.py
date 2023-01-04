"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 06
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#  O maior de dois números e a diferença entre eles  #'.upper())
print('###'*18)

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1>n2:
    print('Entre {} e {}, o maior é o número {} e a diferença entre eles é {}.'.format(n1, n2, n1, n1-n2))
elif n2>n1:
    print('Entre {} e {}, o maior é o número {} e a diferença entre eles é {}.'.format(n1, n2, n2, n2-n1))
else:
    print('Os dois números são iguais, logo a diferença entre eles é 0.')