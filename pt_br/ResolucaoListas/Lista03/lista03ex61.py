"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 61
   Programador: Fernando Martins Cardoso
"""

print('###'*14)
print('#   Maior palíndromo entre produtos de   #'.upper())
print('#     dois números de três algarismos    #'.upper())
print('###'*14)

i = 999
while i >= 100:
    j = 999
    while j >= 100:
        m = i*j
        u = m%10
        d = (m//10)%10
        c = (m//100)%10
        um = (m//1000)%10
        dm = (m//10000)%10
        cm = m//100000
        w = cm + 10*dm + 100*um + 1000*c + 10000*d + 100000*u
        if cm == 0:
            w = w/10
        if m == w:
            print('\nO maior palíndromo resultante do produto de dois \nnúmeros de três algarismos é: {} = {} x {}'.format(m, i, j))
            break
        j = j-1
    if m == w:
        break
    i = i-1
