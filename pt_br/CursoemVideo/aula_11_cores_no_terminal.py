print('\033[7;30;45mOlá, Mundo!\033[m')

nome = str(input('Digite seu nome: '))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá, muito prazer em lhe conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))