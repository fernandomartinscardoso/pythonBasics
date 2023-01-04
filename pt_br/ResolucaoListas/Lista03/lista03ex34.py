"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 34
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#   Mínimo múltiplo comum de 1 a 20   #'.upper())
print('###'*13)

c = 0
m = 698377600   # Começando por um valor alto porque o mmc de 1 a 20 é gigantesco e demora convergir começando de 1

while True:
    for i in range(1, 21):
        if m%i==0:
            c+=1
        else:
            c = 0
    if c==20:
        break
    m = m+1
print('\nMMC(1,2,3,...,20) = {}'.format(m))
