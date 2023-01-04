nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2)/2
print('Sua média foi {:.1f}.'.format(m))
if m >= 6.0:
    print('Parabéns, você está aprovad@!')
else:
    print('Você está reprovad@.')
