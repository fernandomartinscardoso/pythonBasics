"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 33
   Programador: Fernando Martins Cardoso
"""

print('###'*21)
print('#           N primeiros múltiplos de dois números:            #'.upper())
print('#   O múltiplo pode ser apenas de um ou de ambos os números   #')
print('###'*21)

n = int(input('Digite quantos múltiplos deseja gerar: '))
i = int(input('Digite o primeiro número: '))
j = int(input('Digite o segundo número: '))

s = '0'     # Acumulador de string
c = 1       # Contador de múltiplos
m = 1       # Primeiro múltiplo comum a ser analisado
while c<n:
    if m%i==0 or m%j==0:
        sm = str(m)
        s = s + ', ' + sm
        c = c + 1
    m = m + 1
print('Os {} primeiros múltiplos de {} e/ou {} são: {}.'.format(n, i, j, s))
