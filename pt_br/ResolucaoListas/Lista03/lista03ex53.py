"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 53
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                         Triângulo de Floyd                        #'.upper())
print('#    Linha 1: 1; linha 2: 2 3; linha 3: 4 5 6; linha 4: 7 8 9 10    #')
print('###'*23)

n = int(input("Quantas linhas você deseja plotar do Triângulo de Floyd?\n"))

valor = 1

for b in range(1,n+1):
    elementos = " "
    for c in range(valor, valor+b):
        elementos = elementos + str(c) + " "
        valor = valor + 1
    print(elementos)
