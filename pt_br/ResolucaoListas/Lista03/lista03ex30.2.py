"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 30 - Série alternada dos números naturais
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#   Somatório dos n números naturais conforme:    #'.upper())
print('#      S(n)=1-2+3-4+5-6+7-...+n*(-1)**(n+1)       #')
print('###'*17)

n = int(input('Digite quantos termos da série devem ser somados: '))
c=1
s=0
while c<=n:
    s = s + c*(-1)**(c+1)
    c = c + 1
print('S({}) = {}'.format(n, s))
