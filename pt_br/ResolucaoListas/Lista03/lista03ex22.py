"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 22
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#     Média de notas cujos valores estejam entre     #'.upper())
print('#              um intervalo de 10 a 20               #'.upper())
print('###'*18)

print('\nInsira notas de 10 a 20 ou uma nota fora do intervalo para sair\n')
c = 0       # Contador de notas válidas inseridas
s = 0       # Acumulador de notas válidas
while True:
    n = float(input('Digite a {}ª nota: '.format(c+1)))
    if (n<10 or n>20) and c == 0:
        print('Nenhuma nota válida inserida!')
        break
    elif n>=10 and n<=20:
        s = s + n
        c = c + 1
    else:
        print('Última nota inserida inválida.\n')
        print('Média = {:.1f}'.format(s/c))
        break
