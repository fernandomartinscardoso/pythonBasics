"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 46
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#              Adivinha número inteiro de 1 a 1000               #'.upper())
print('#   Você chuta que número o programa pensou e ele te dá dicas    #')
print('###'*22)

from random import randint

numero_pensado = randint(1, 1000)
tentativas = 0

while True:
    chute = int(input("Adivinha o número que pensei: "))
    if chute > numero_pensado:
        print("O número que pensei é menor")
        tentativas = tentativas + 1
    elif chute < numero_pensado:
        print("O número que pensei é maior")
        tentativas = tentativas +1
    else:
        print("Parabéns, você acertou usando {} tentativas!".format(tentativas))
        break
