print('Este programa calcula a soma de dois números inteiros \n')
n1=int(input('Digite o primeiro número: '))
print('O primeiro número é do tipo: ',type(n1))
n2=int(input('\nDigite o segundo número: '))
print('O segundo número é do tipo: ',type(n2))
s=n1+n2
print('\nA soma entre {} e {} vale {}'.format(n1,n2,s))