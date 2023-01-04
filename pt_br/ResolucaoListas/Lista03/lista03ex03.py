"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 03
   Programador: Fernando Martins Cardoso
"""
from time import sleep      # O uso dessa biblioteca é opcional, só para deixar a contagem mais lenta
print('###'*12)
print('#  Contagem Regressiva de 10 a 0   #'.upper())
print('###'*12)

print('\nIniciando contagem regressiva:')
sleep(2)
for k in range(10, -1, -1):
    print(k)
    sleep(0.5)              # A função sleep adiciona uma parada na execução do código (neste caso, de 0.5 segundos)
print('FIM!')
