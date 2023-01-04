print('Este programa verifica se o nome de uma cidade começa com a palavra "Santo".')
cidade = str(input('Digite o nome da cidade: '))
cidadenormal = cidade.strip().capitalize().split()
print('O nome da cidade começa com "Santo"?', 'Santo' in cidadenormal[0])
