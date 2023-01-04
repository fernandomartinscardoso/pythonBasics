"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 37
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#       Tarifa de Estacionamento      #'.upper())
print('###'*13)

horcheg = str(input('Digite o horário de chegada na forma HH:MM \n '))
horsaid = str(input('Digite o horário de saída na forma HH:MM \n '))

hc = int(horcheg[0:2])
mc = int(horcheg[3:])
tc = hc*60+mc

hs = int(horsaid[0:2])
ms = int(horsaid[3:])
ts = hs*60+ms


tp = ts-tc

if tp <= 120:
    print('Tarifa: R$ 1,00')
    elif