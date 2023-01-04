"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 24
   Programador: Fernando Martins Cardoso
"""

print('+++'*10)
print('| Conversor de m² para acres |')
print('+++'*10)
area = float(input('Digite a área em m²: '))
acres = 0.000247*area
print('{:.2f} m² = {:.2f} ac'.format(area, acres))
