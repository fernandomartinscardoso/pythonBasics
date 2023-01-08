"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 44
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#                    Sequência de Fibonacci                      #'.upper())
print('#   Inserir o número mais próximo do limite superior da série    #')
print('###'*22)

s0 = 0
s1 = 1
fib = '{} {}'.format(s0,s1)

n = int(input('Digite um número inteiro positivo: '))

while n <= 0:
   print('Entrada inválida. Tente novamente.')
   n = int(input('Digite um número inteiro positivo: '))

i = 1
f = s0 + s1
while i <= n:
   i = i + f
   fs = str(i)
   fib = fib + ' ' + fs

print(fib) 
