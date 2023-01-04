print('Este programa separa os dígitos de um número inteiro com até 4 algarismos')
n = int(input('Digite o número inteiro: '))
m = n//1000
c = (n%1000)//100
d = (n%100)//10
u = n%10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

