"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 21
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#    Somando pares e multiplicando ímpares de     #'.upper())
print('#        um intervalo de números inteiros         #'.upper())
print('###'*17)

min = int(input('\nInsira o menor valor do intervalo: '))
max = int(input('Insira o maior valor do intervalo: '))

soma_par = 0        # Acumulador da soma dos pares
mult_impar = 1      # Acumulador da multiplicação dos ímpares
for i in range(min, max+1):
    if i%2 == 0:
        soma_par = soma_par + i
    else:
        mult_impar = mult_impar*i
print('''\nNo intervalo de {} até {}, temos  que:
Soma dos pares = {}
Produto dos ímpares = {}'''.format(min, max, soma_par, mult_impar))
