"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 30 - Série dos números naturais
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#   Somatório dos n números naturais conforme:    #'.upper())
print('#            S(n)=1+2+3+4+5+6+7+...+n             #')
print('###'*17)

n = int(input('Digite quantos termos da série devem ser somados: '))
c=1
s=0
while c<=n:
    s = s + c
    c = c + 1
print('S({}) = {}'.format(n, s))
