"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 51
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#               Evolução salarial de um indivíduo                #'.upper())
print('#       Obedecendo regras de crescimento anual dinâmicas         #')
print('###'*22)

import datetime

hoje = datetime.date.today()
ano_atual = hoje.year

print('''Em 1995, o salário do funcionário era de R$ 2000,00.
Em 1996, houve reajuste de 1,5%. O reajuste foi dobrado a cada ano seguinte.''')

salano = 2000
taxa = 0.015
ano = 1996

while ano <= ano_atual:
    salano = salano*(1 + taxa)
    taxa = 2*taxa
    ano = ano + 1

print("O salário atual do funcionário é de R$ {:.2f}.".format(salano))
