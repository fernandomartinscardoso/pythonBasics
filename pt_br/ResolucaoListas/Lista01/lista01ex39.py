"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 39
   Programador: Fernando Martins Cardoso
"""

print('###'*20)
print('# Distribuição de um prêmio de R$780.000,00 de um concurso #'.upper())
print('###'*20)
g1 = 780000*(46/100)
g2 = 780000*(32/100)
g3 = 780000 - g1 - g2
print('Primeiro colocado (46% do prêmio): R${:.2f}'.format(g1))
print('Segundo colocado (32% do prêmio): R${:.2f}'.format(g2))
print('Terceiro colocado (22% do prêmio: R${:.2f}'.format(g3))
