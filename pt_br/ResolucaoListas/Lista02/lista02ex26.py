"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 26
   Programador: Fernando Martins Cardoso
"""

print('###'*11)
print('#     Consumo de um veículo     #'.upper())
print('###'*11)

dist = float(input('Distância percorrida (em km): '))
comb = float(input('Quantidade de combustível consumida (em litros): '))

cons = dist/comb

print("\nConsumo = {:.1f} km/l".format(cons))
if cons < 8:
    print('Alto consumo! Venda o carro!')
elif cons >= 8 and cons <= 14:
    print('Veículo econômico!')
else:
    print('Veículo super econômico!')
