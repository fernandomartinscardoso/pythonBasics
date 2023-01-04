nome = str(input('Qual é o seu nome? '))
if nome == 'Fernando':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Rafael' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Wilka Fernanda Petúnia':
    print('Que lindo nome feminino!')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))
