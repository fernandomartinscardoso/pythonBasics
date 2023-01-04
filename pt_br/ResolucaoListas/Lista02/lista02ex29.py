"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 29
   Programador: Fernando Martins Cardoso
"""

from random import randint

print('###'*12)
print('#     Teste de soma de números     #'.upper())
print('###'*12)

print('''\nEste programa pergunta a soma de dois números entre 1 e 100.
Serão feitas 5 perguntas e seu desempenho será mostrado no final.''')

c = 0   # Contador de respostas corretas

na1 = randint(1, 100)
na2 = randint(1, 100)
somaa = na1 + na2
respa = int(input('1-Qual a soma de {} e {}?\n'.format(na1, na2)))
if somaa == respa:
    print('Certa resposta!')
    c = c + 1
else:
    print('Incorreto!' )
    print('A resposta certa é igual a {}.'.format(somaa))
    
nb1 = randint(1, 100)
nb2 = randint(1, 100)
somab = nb1 + nb2
respb = int(input('2-Qual a soma de {} e {}?\n'.format(nb1, nb2)))
if somab == respb:
    print('Certa resposta!')
    c = c + 1
else:
    print('Incorreto!' )
    print('A resposta certa é igual a {}.'.format(somab))

nc1 = randint(1, 100)
nc2 = randint(1, 100)
somac = nc1 + nc2
respc = int(input('3-Qual a soma de {} e {}?\n'.format(nc1, nc2)))
if somac == respc:
    print('Certa resposta!')
    c = c + 1
else:
    print('Incorreto!' )
    print('A resposta certa é igual a {}.'.format(somac))

nd1 = randint(1, 100)
nd2 = randint(1, 100)
somad = nd1 + nd2
respd = int(input('4-Qual a soma de {} e {}?\n'.format(nd1, nd2)))
if somad == respd:
    print('Certa resposta!')
    c = c + 1
else:
    print('Incorreto!' )
    print('A resposta certa é igual a {}.'.format(somad))

ne1 = randint(1, 100)
ne2 = randint(1, 100)
somae = ne1 + ne2
respe = int(input('5-Qual a soma de {} e {}?\n'.format(ne1, ne2)))
if somae == respe:
    print('Certa resposta!')
    c = c + 1
else:
    print('Incorreto!' )
    print('A resposta certa é igual a {}.'.format(somae))

if c == 0:
    print('\nVocê não acertou nenhuma operação.')
elif c == 1:
    print('\nVocê acertou uma operação.')
elif c == 5:
    print('\nParabéns! Você acertou todas as operações!')
else:
    print('\nVocê acertou {} operações.'.format(c))