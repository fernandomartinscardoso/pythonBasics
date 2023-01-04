"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 20
   Programador: Fernando Martins Cardoso
"""

print('###'*19)
print('#    Avaliando números inteiros e contando os pares     #'.upper())
print('###'*19)
c=0
d=0
while True:
    n = int(input('Digite um número inteiro ou 1000 para sair: '))
    if n==1000:
        break
    elif n%2==0:
        print('Número inserido é par.')
        c=c+1
    else:
        print('Número inserido não é par.')
    d = d+1

print('Quantidade de números inseridos: {}'.format(d))
print('Quantidade de números que eram pares: {}'.format(c))
