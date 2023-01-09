"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 48
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#           Soma dos pares da sequência de Fibonacci             #'.upper())
print('#       Restrição: elementos pares menores que 4 milhões         #')
print('###'*22)

s0 = 0
s1 = 1
fib = s0 + s1
soma_par = 0

while fib < 4000000:
    s0 = s1
    s1 = fib
    fib = s0 + s1
    if fib%2 == 0:
        soma_par = soma_par + fib

print("A soma dos elementos pares da série de Fibonacci menores que 4 milhões é igual a {}".format(soma_par))