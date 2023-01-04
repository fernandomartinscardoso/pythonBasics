from random import randint
from time import sleep
print('\033[34m-=-'*19)
print('\033[33mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[34m-=-'*19)
num = int(input('\033[1;35mEm qual número eu pensei? '))
pen = randint(0, 5)
print('\033[31mProcessando.')
sleep(1)
print('\033[33mProcessando..')
sleep(1)
print('\033[32mProcessando...')
sleep(1)
if num == pen:
    print('\033[4;34mParabéns! Você adivinhou!')
else:
    print('\033[4;31mVocê errou, eu pensei no número {}.'.format(pen))