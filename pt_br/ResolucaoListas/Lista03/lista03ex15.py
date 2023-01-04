"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 15
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#   Inteiros positivos ímpares em ordem crescente    #'.upper())
print('###'*18)

n = int(input('Até qual inteiro ímpar você quer imprimir? '))

# Teste para verificar se o número inserido é ímpar e positivo:
while n%2==0 or n<0:
    print('Número inserido não é par ou positivo. Tente Novamente')
    n = int(input('Até qual inteiro ímpar você quer imprimir? '))

for i in range(1, n+1, 2):
    print(i)