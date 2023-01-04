"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 48
   Programador: Fernando Martins Cardoso
"""

print('###'*14)
print('#     horário final de um experimento    #'.upper())
print('###'*14)
print('Digite o horário do início do experimento')
he = int(input('Hora: '))
me = int(input('Minuto: '))
se = int(input('Segundo: '))
seg = int(input('Digite a duração do experimento (em segundos): '))
h = seg//3600
m = (seg%3600)//60
s = seg - m*60 - h*3600

hf = (he + (m+me+(s+se)//60)//60 + h)%24
mf = (me + m + (s+se)//60)%60
sf = (s+se)%60
print('''Início do experimento: {:0>2.0f}:{:0>2.0f}:{:0>2.0f}
Fim do experimento: {:0>2.0f}:{:0>2.0f}:{:0>2.0f}'''.format(he, me, se, hf, mf, sf))
