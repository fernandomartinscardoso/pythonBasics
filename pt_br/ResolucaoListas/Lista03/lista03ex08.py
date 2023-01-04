"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 08
   Programador: Fernando Martins Cardoso
"""

print('###'*14)
print('#    O menor e o maior de 10 números     #'.upper())
print('###'*14)

menor = 0
maior = 0
c = 1
while c<=10:
    n = int(input('Digite o {}º número: '.format(c)))
    if c==1:
        menor=n
        maior=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    c=c+1
print('O maior número digitado foi igual a {}.'.format(maior))
print('O menor número digitado foi igual a {}.'.format(menor))
