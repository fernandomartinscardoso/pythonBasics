"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 40
   Programador: Fernando Martins Cardoso
"""

print('###'*16)
print('#      custo ao consumidor de um automóvel     #'.upper())
print('###'*16)

custo_fabrica = float(input('Digite o custo de fábrica: \nR$ '))

if custo_fabrica <= 12000:
    custo_consumidor = 1.05*custo_fabrica
elif custo_fabrica > 12000 and custo_fabrica <= 25000:
    custo_consumidor = 1.25*custo_fabrica
else:
    custo_consumidor = 1.35*custo_fabrica

print('O custo para o consumidor será de R$ {:.2f}'.format(custo_consumidor))
