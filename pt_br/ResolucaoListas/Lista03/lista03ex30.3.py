"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 30 - Série dos números naturais ímpares
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#   Somatório dos n naturais ímpares conforme:    #'.upper())
print('#           S(n)=1+3+5+7+9+...+(2n-1)             #')
print('###'*17)

n = int(input('Digite quantos termos da série devem ser somados: '))
c=1
s=0
while c<=n:
    s = s + (2*c-1)
    c = c + 1
print('S({}) = {}'.format(n, s))
