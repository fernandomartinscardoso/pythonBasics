"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 36
   Programador: Fernando Martins Cardoso
"""

print('###'*23)
print('#     Diferença entre o quadrado da soma e a soma dos quadrados     #'.upper())
print('#                Dos 100 primeiros números naturais                 #'.upper())
print('###'*23)
sq = 0
s = 0
for i in range(1, 101):
    s = s + i
    sq = sq + i**2
s2 = s**2

print('\n(1+2+3+...+100)² - (1²+2²+3²+...+100²) = {}'.format(s2-sq))
