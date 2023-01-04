"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 05
   Programador: Fernando Martins Cardoso
"""

print('###'*10)
print('#     Soma de 10 valores     #'.upper())
print('###'*10)
c=1     # Contador
s=0     # Acumulador
while c<=10:
    n = float(input('Digite o {}º valor: '.format(c)))
    s = s + n
    c = c + 1
print('Soma = {}'.format(s))
