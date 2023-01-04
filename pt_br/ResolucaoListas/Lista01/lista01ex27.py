"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 27
   Programador: Fernando Martins Cardoso
"""

print('+++'*11)
print('+ Conversor de hectares para m² +')
print('+++'*11)
ha = float(input('Digite a área em hectares: '))
m2 = ha/0.0001
print('{:.2f} ha = {:.0f} m²'.format(ha, m2))