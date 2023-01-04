"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 51
   Programador: Fernando Martins Cardoso
"""

print('###'*14)
print('''#    repartindo um prêmio de loteria     #
#       bolão entre 3 apostadores        #'''.upper())
print('###'*14)
# Este programa divide o prêmio proporcionalmente ao
# total investido por cada apostador
premio = float(input('Digite o valor do prêmio: R$'))
g1 = float(input('Quanto o primeiro ganhador apostou? R$'))
g2 = float(input('Quanto o segundo ganhador apostou? R$'))
g3 = float(input('Quanto o terceiro ganhador apostou? R$'))
total = g1 + g2 + g3
p1 = (g1/total)*premio
p2 = (g2/total)*premio
p3 = (g3/total)*premio
print('''Quem apostou R${:.2f} deve receber R${:.2f}.
Quem apostou R${:.2f} deve receber R${:.2f}.
Quem apostou R${:.2f} deve receber R${:.2f}.'''.format(g1, p1, g2, p2, g3, p3))
