"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 36
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#         Cálculo de Comissão         #'.upper())
print('###'*13)

v = float(input('Valor da venda mensal: R$'))

if v >= 100000:
    c = 700 + 0.16*v
elif v<100000 and v>=80000:
    c = 650 + 0.14*v
elif v<80000 and v>=60000:
    c = 600 + 0.14*v
elif v<60000 and v>=40000:
    c = 550 + 0.14*v
elif v<40000 and v>=20000:
    c = 500 + 0.14*v
elif v<20000 and v>=0:
    c = 400 + 0.14*v
else:
    print('Valor inserido inválido.')

print('Valor da comissão: R${:.2f}'.format(c))
