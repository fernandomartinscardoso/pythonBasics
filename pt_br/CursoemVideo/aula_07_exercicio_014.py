print('Conversão de temperaturas\n')
temp = float(input('Digite a temperatura em °C: '))
far = 1.8*temp + 32
kel = temp + 273.15
print('A temperatura de {:.1f}°C equivale a {:.1f}°F e a {:.1f} K.'.format(temp, far, kel))
