"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 17
   Programador: Fernando Martins Cardoso
"""

print('###'*16)
print('#       Cálculo da área de um  trapézio        #'.upper())
print('#      Bases e altura devem ser positivas      #')
print('###'*16)

bmenor = float(input('Insira o valor da base menor: '))
bmaior = float(input('Insira o valor da base maior: '))
h = float(input('Insira o valor da altura: '))

if bmaior>0 and bmenor>0 and h>0:
    area = (bmaior + bmenor)*h/2
    print('Área = {:.1f}'.format(area))
else:
    print('Erro! Todos os valores inseridos devem ser positivos.')
