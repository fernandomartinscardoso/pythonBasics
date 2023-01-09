"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 49
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#             Evolução de taxas de juros compostos               #'.upper())
print('#    Comparando dois salários evoluindo com taxas diferentes     #')
print('###'*22)

print('''João recebe um terço do salário de Carlos. 
Quanto tempo leva para uma aplicação do salário de cada se igualar nas seguintes condições:
* A aplicação de João rende 5% ao mês
* A aplicação de Carlos rende 2% ao mês''')

carlos = 1
joao = 1/3
meses = 0

while joao <= carlos:
    joao = joao*(1.05)
    carlos = carlos*(1.02)
    meses = meses + 1

print('''Aplicação de João: {:.2f}. Aplicação de Carlos: {:.2f}. 
Foram necessários {} meses para que as aplicações se equiparassem.'''.format(joao, carlos, meses))