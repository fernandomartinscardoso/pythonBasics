"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 47
   Programador: Fernando Martins Cardoso
"""

print('###'*19)
print('#   COnvertendo segundos em horas, minutos e segundos   #'.upper())
print('###'*19)
seg = int(input('Digite o tempo em segundos: '))
h = seg//3600
m = (seg%3600)//60
s = seg - m*60 - h*3600
print('{} segundos equivale a {} horas, {} minutos e {} segundos.'.format(seg, h, m, s))
