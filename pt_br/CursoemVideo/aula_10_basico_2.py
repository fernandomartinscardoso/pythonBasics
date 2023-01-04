'''Estrutura simplificada de condicional'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2)/2
print('Sua média foi {:.1f}.'.format(m))
print('Parabéns!' if m>= 6.0 else 'Estude mais!')
