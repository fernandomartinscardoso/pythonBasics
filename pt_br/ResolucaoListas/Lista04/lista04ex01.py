"""Gabarito da Lista 4 - Vetores e Matrizes
   Exercício 01
   Programador: Fernando Martins Cardoso
"""

print('###'*19)
print('# Atribuição de valores e operações simples em um vetor #'.upper())
print('###'*19)

A = [1,0,5,-2,-5,7]
print('Vetor A={}'.format(A))

soma = A[0] + A[1] + A[5]
print('Soma dos elementos A[0], A[1] e A[5] é igual a {}'.format(soma))

A[4] = 100
print('Vetor alterado na posição 4: \nA={}'.format(A))

print('Valor dos elementos do vetor por linha:')
for i in range(0,len(A)):
    print(A[i])
