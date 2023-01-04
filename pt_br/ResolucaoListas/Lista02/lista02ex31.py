"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 31
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#   Classificação de peso e altura    #'.upper())
print('###'*13)

print('''Este programa classifica pessoas em categorias conforme tabela abaixo:
_______________________________________________________________________
                 |_________________________Peso________________________
Altura           |  Até 60  |  Entre 60 e 90 (Inclusive) | Acima de 90
_________________|__________|____________________________|_____________                             
Menor que 1,20   |    A     |              D             |      G
De 1,20 a 1,70   |    B     |              E             |      H
Maior que 1,70   |    C     |              F             |      I
''')

alt = float(input('Insira a altura (em metros): '))
peso = float(input('Insira o peso (em kg): '))

if peso < 60:
    if alt < 1.2:
        print('Classificação: A')
    elif alt >= 1.2 and alt <= 1.7:
        print('Classificação: B')
    else:
        print('Classificação: C')
elif peso >=60 and peso <= 90:
    if alt < 1.2:
        print('Classificação: D')
    elif alt >= 1.2 and alt <= 1.7:
        print('Classificação: E')
    else:
        print('Classificação: F')
else:
    if alt < 1.2:
        print('Classificação: G')
    elif alt >= 1.2 and alt <= 1.7:
        print('Classificação: H')
    else:
        print('Classificação: I')