""" Jogo do Adivinha o Número
    O computador escolhe um número de 1 a 1000.
    O usuário tenta adivinhar qual número o computador escolheu.
    O computador diz se a tentativa foi maior ou menor do que a resposta certa.
    O jogo termina quando o usuário acerta o número.
"""

from random import randint

comp = randint(1, 1000)

print('''Tente adivinhar o número em que estou pensando.
Pode ser qualquer número de 1 a 1000.''')

c=1
while True:
    n = int(input('Digite a {}ª tentativa: '.format(c)))
    if n < comp:
        print('Pensei em um número maior...')
    elif n > comp:
        print('Pensei em um número menor...')
    else:
        print('Parabéns! Você acertou!')
        break
    c = c + 1
    