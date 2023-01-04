"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 11
   Programador: Fernando Martins Cardoso
"""

print('-=-'*9)
print('Conversor de m/s para km/h')
print('-=-'*9)
v_ms = float(input('Digite a velocidade em m/s: '))
v_kmh = v_ms*3.6
print('{} m/s = {:.1f} km/h'.format(v_ms, v_kmh))