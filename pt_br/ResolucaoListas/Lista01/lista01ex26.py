"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 26
   Programador: Fernando Martins Cardoso
"""

print('+++'*11)
print('+ Conversor de m² para hectares +')
print('+++'*11)
m2 = float(input('Digite a área em m²: '))
ha = m2*0.0001
print('{:.2f} m² = {:.3f} ha'.format(m2, ha))
