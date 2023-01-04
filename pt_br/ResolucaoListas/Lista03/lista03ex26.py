"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 26
   Programador: Fernando Martins Cardoso
"""

print('###'*15)
print('#     Primeiro múltiplo de 11, 13 ou 17     #'.upper())
print('#            após um número dado            #'.upper())
print('###'*15)

num = int(input('Insira um número inteiro: '))
c = num
while True:
    c = c + 1
    if c%11==0 or c%13==0 or c%17==0:
        print('Após o número {}, o primeiro múltiplo de 11, 13 ou 17 é igual a {}.'.format(num, c))
        break