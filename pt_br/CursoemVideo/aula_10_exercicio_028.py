from random import randint
from time import sleep
print('-=-'*19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*19)
num = int(input('Em qual número eu pensei? '))
pen = randint(0, 5)
print('Processando...')
sleep(2.5)
if num == pen:
    print('Parabéns! Você adivinhou!')
else:
    print('Você errou, eu pensei no número {}.'.format(pen))
