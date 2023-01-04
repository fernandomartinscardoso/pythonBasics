print('Conversor de Número Decimal para as',end='')
print(' Bases Binária, Octal ou Hexadecimal')
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão: ')
print('''[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
esc = int(input('Sua opção: '))
if esc == 1:
    bin = bin(num)
    print('{} em BINÁRIO é igual a {}'.format(num, bin[2:]))
elif esc == 2:
    oct = oct(num)
    print('{} em OCTAL é igual a {}'.format(num, oct[2:]))
elif esc == 3:
    hex = hex(num)
    print('{} em HEXADECIMAL é {}'.format(num, hex[2:]))
else:
    print('Opção inválida')
