"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 40
   Programador: Fernando Martins Cardoso
"""

print('###'*22)
print('#        O maior e o menor de números inteiros positivos         #'.upper())
print('#      Ao digitar um número negativo o programa se encerra       #')
print('###'*22)

n = int(input('Digite um número inteiro positivo: '))  
while n <= 0:
    print('Inválido! O primeiro número deve ser inteiro positivo.')
    n = int(input('Digite um número inteiro positivo: '))    
    maior = n
    menor = n 

while True:
    n = int(input('Digite um número inteiro positivo: '))
    if n < 0:
        break
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('Maior número digitado =', maior)
print('Menor número digitado =', menor)
        