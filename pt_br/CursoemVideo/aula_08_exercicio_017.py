'''print('Cálculo da hipotenusa do triângulo retângulo')
c1 = float(input('Digite o primeiro cateto: '))
c2 = float(input('Digite o segundo cateto: '))
hip = (c1**2 + c2**2)**(1/2)
print('A hipotenusa desse triângulo retângulo é igual a {:.2f}.'.format(hip))'''

#Outra forma de resolver
import math
print('Cálculo da hipotenusa do triângulo retângulo')
c1 = float(input('Digite o primeiro cateto: '))
c2 = float(input('Digite o segundo cateto: '))
hip = math.hypot(c1, c2)
print('A hipotenusa desse triângulo retângulo é igual a {:.2f}.'.format(hip))
