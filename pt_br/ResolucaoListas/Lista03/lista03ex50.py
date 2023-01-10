"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 50
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#          Pessoas com taxas de crescimento diferentes           #'.upper())
print('#       Comparando dois indivíduos com alturas diferentes        #')
print('###'*22)

print('''Chico tem 1,50 de altura e cresce dois centímetros por ano. 
Zé tem 1,10 e cresce três centímetros por ano.
Quantos anos são necessários para que Zé seja maior que Chico?''')

chico = 1.5
ze = 1.1
anos = 0

while ze < chico:
    chico = chico + 0.02
    ze = ze + 0.03
    anos = anos + 1

print('''Após {} anos, Zé ultrapassou a altura de Chico.
Agora Zé tem {:.2f} m  e Chico tem {:.2f} m.'''.format(anos, ze, chico))
