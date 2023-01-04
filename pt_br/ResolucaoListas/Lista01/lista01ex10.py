"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 10
   Programador: Fernando Martins Cardoso
"""

print('-=-'*9)
print('Conversor de km/h para m/s')
print('-=-'*9)
v_kmh = float(input('Digite a velocidade em km/h: '))
v_ms = v_kmh/3.6
print('{} km/h = {:.1f} m/s'.format(v_kmh, v_ms))
