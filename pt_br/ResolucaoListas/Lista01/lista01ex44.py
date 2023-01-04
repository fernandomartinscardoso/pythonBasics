"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 44
   Programador: Fernando Martins Cardoso
"""

print('###'*9)
print('#  altura em uma escada   #'.upper())
print('###'*9)
deg = float(input('Altura do degrau (em cm): '))
alt = float(input('Altura que o usuário deseja alcançar (em m): '))
num_deg = alt/(deg/100)
print('Para atingir a altura de {} m, o usuário deverá subir {:.0f} degraus da escada'.format(alt, num_deg))
