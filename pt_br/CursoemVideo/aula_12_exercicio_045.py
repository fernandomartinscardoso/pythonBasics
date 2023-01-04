from random import randint
from time import sleep

print('{:=^45}'.format(' PEDRA + PAPEL + TESOURA ').upper())
print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
computador = randint(1,3)
jogador = int(input('Qual é sua jogada?\n'))
sleep(0.5)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
if jogador==1 and computador==3:
    print('*'*25)
    print('Computador jogou TESOURA!')
    print('Você jogou PEDRA!')
    print('*' * 25)
    print('\nVOCÊ VENCE!')
elif jogador==1 and computador==2:
    print('*' * 25)
    print('Computador jogou PAPEL!')
    print('Você jogou PEDRA!')
    print('*' * 25)
    print('\nCOMPUTADOR VENCE!')
elif jogador==1 and computador==1:
    print('*' * 25)
    print('Computador jogou PEDRA!')
    print('Você jogou PEDRA!')
    print('*' * 25)
    print('\nEMPATE!')
elif jogador==2 and computador==1:
    print('*' * 25)
    print('Computador jogou PEDRA!')
    print('Você jogou PAPEL!')
    print('*' * 25)
    print('\nVOCÊ VENCE!')
elif jogador==2 and computador==2:
    print('Computador jogou PAPEL!')
    print('Você jogou PAPEL!')
    print('EMPATE!')
elif jogador==2 and computador==3:
    print('*' * 25)
    print('Computador jogou TESOURA!')
    print('Você jogou PAPEL!')
    print('*' * 25)
    print('\nCOMPUTADOR VENCE!')
elif jogador==3 and computador==1:
    print('*' * 25)
    print('Computador jogou PEDRA!')
    print('Você jogou TESOURA!')
    print('*' * 25)
    print('\nCOMPUTADOR VENCE!')
elif jogador==3 and computador==2:
    print('*' * 25)
    print('Computador jogou PAPEL!')
    print('Você jogou TESOURA!')
    print('*' * 25)
    print('\nVOCÊ VENCE!')
elif jogador == 3 and computador == 3:
    print('*' * 25)
    print('Computador jogou TESOURA!')
    print('Você jogou TESOURA!')
    print('*' * 25)
    print('\nEMPATE!')
else:
    print('Jogada inválida!')
