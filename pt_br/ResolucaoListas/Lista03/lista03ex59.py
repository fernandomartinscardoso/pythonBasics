"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 59
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                 Informação de consumo de energia                  #'.upper())
print('#             Dados de consumo por código de consumidor             #')
print('###'*23)

habitantes = int(input("Informe o número de habitantes da cidade: "))
while habitantes < 1:
    print("Número inválido. Tente novamente!")
    habitantes = int(input("Informe o número de habitantes da cidade: "))

maior_consumo = 0
menor_consumo = 0
consumo_cat_1 = 0
consumo_cat_2 = 0
consumo_cat_3 = 0
total_consumo = 0
for i in range(1,habitantes+1):
    consumo = float(input('Informe o consumo mensal do habitante {} em kWh: '.format(i)))
    codigo = int(input('Informe o código do consumidor (1-Residencial, 2-Comercial. 3-Industrial): '))
    if consumo > maior_consumo:
        maior_consumo = consumo
    if i == 1:
        menor_consumo = consumo
    if consumo < menor_consumo:
        menor_consumo = consumo
    total_consumo = total_consumo + consumo
    if codigo == 1:
        consumo_cat_1 = consumo_cat_1 + consumo
    elif codigo == 2:
        consumo_cat_2 = consumo_cat_2 + consumo
    elif codigo == 3:
        consumo_cat_3 = consumo_cat_3 + consumo
    else:
        print('Código inválido.')
        break

media_consumo = total_consumo/habitantes

print('Maior consumo: {} kWh'.format(maior_consumo))
print('Menor consumo: {} kWh'.format(menor_consumo))
print('Média de consumo: {} kWh'.format(media_consumo))
print('Consumo da categoria Residencial: {} kWh'.format(consumo_cat_1))
print('Consumo da categoria Comercial: {} kWh'.format(consumo_cat_2))
print('Consumo da categoria Industrial: {} kWh'.format(consumo_cat_3))
