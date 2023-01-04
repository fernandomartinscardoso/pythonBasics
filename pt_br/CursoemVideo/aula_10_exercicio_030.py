print('Este programa informa se um número é par ou ímpar')
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar.'.format(numero))
