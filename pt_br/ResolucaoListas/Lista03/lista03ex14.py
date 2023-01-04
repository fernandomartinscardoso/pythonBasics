"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 14
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#   Inteiros positivos pares em ordem decrescente    #'.upper())
print('###'*18)

n = int(input('A partir de qual inteiro par você quer imprimir? '))

# Teste para verificar se o número inserido é par e positivo:
while n%2==1 or n<0:
    print('Número inserido não é par ou positivo. Tente Novamente')
    n = int(input('A partir de qual inteiro par você quer imprimir? '))

for i in range(n, -1, -1):
    if i%2==0:
        print(i)
