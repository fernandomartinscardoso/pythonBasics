"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 41
   Programador: Fernando Martins Cardoso
"""

print('###'*22)
print('#        Cálculo do resistor equivalente para associação         #'.upper())
print('#                 de dois resistores em paralelo                 #'.upper())
print('###'*22)

print('\nSe for inserido o valor 0 para qualquer resistência, o programa finaliza.')      

while True:
    r1 = float(input('Digite o valor do primeiro resistor (em ohms): '))
    if r1 == 0:
        break
    r2 = float(input('Digite o valor do segundo resistor (em ohms): '))
    if r2 == 0:
        break
    req = (r1*r2)/(r1+r2)
    print('\nResistor equivalente igual a: {:.1f} ohms'.format(req))
    print('===========================================')