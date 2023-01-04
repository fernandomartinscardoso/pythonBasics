"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 16
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#  Inteiros positivos ímpares em ordem decrescente   #'.upper())
print('###'*18)

n = int(input('A partir de qual inteiro ímpar você quer imprimir? '))

# Teste para verificar se o número inserido é ímpar e positivo:
while n%2==0 or n<0:
    print('Número inserido não é ímpar ou positivo. Tente Novamente')
    n = int(input('A partir de qual inteiro ímpar você quer imprimir? '))

for i in range(n, -1, -2):
    print(i)
