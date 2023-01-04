"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 18
   Programador: Fernando Martins Cardoso
"""

print('###'*19)
print('#   Este programa pede para inserir números e mostra    #'.upper())
print('#     qual o maior e quantas vezes ele foi inserido     #'.upper())
print('###'*19)

n = int(input('Quantos números você quer inserir? '))
maior = 0
c=1
for i in range(1, n+1):
    num = int(input('Digite o {}º número: '.format(i)))
    if i==1:
        maior = num
    else:
        if num > maior:
            maior = num
            c = 1
        elif num < maior:
            c = c
        else:
            c = c+1
print('O maior número foi o {} e ele foi digitado {} vezes.'.format(maior, c))
