"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 34
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#        Conceito de Estudantes       #'.upper())
print('###'*13)

n = float(input('Digite a nota do(a) estudante: '))
f = int(input('Digite o número de faltas: '))

if n>=9 and n<=10:
    if f > 20:
        print('Conceito B')
    else:
        print('Conceito A')
elif n>=7.5 and n<9:
    if f > 20:
        print('Conceito C')
    else:
        print('Conceito B')
elif n>=5 and n<7.5:
    if f > 20:
        print('Conceito D')
    else:
        print('Conceito C')
elif n>=4 and n<5:
    if f > 20:
        print('Conceito E')
    else:
        print('Conceito D')
else:
    print('Conceito E')
