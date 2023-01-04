"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 31
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#    Somatório dos n termos da seguinte série:    #'.upper())
print('#         S(n)=1/1+3/2+5/3+...+(2n-1)/n           #')
print('###'*17)

n = int(input('Digite quantos termos da série devem ser somados: '))
c=1
s=0
while c<=n:
    s = s + (2*c-1)/c
    c = c + 1
print('S({}) = {}'.format(n, s))