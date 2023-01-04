from math import sin, cos, tan, pi
print('Cálculo de seno, cosseno e tangente de um ângulo em graus\n')
grau = float(input('Digite o valor do ângulo em graus: '))
ang = grau*pi/180 # A função math.radians() faz esta conversão diretamente
seno = sin(ang)
cosseno = cos(ang)
tangente = tan(ang)
print('='*18)
print('sen({}°)={:.3f} \ncos({}°)={:.3f} \ntg({}°)={:.3f}'.format(grau, seno, grau, cosseno, grau, tangente))
print('='*18)
