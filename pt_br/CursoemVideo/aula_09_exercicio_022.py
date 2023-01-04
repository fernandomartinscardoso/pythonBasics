print('Este programa faz uma análise do seu nome')
n = str(input('Digite seu nome completo: '))
#Eliminando espaçamentos inúteis antes e depois do nome digitado:
nome = n.strip()
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
letras = len(nome)-nome.count(' ')
print('Seu nome tem ao todo {} letras.'.format(letras))
nome_dividido = nome.split()
nome1 = nome_dividido[0]
print('Seu primeiro nome é {} e tem ao todo {} letras.'.format(nome1, len(nome1)))
