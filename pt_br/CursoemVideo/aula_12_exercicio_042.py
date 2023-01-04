print('Analisando Triângulos'.upper())
print('Digite o tamanho dos lados para analisar o triângulo')
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Os lados inseridos formam um triângulo', end=' ')
    if l1!=l2 and l1!=l3 and l2!=l3:
        print('escaleno.')
    elif l1==l2 and l1==l3 and l2==l3:
        print('equilátero.')
    else:
        print('isósceles.')
else:
    print('Os lados inseridos não formam um triângulo.')
