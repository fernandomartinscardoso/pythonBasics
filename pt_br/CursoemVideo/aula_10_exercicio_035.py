print('-=-'*12)
print('Analisando os lados de um triângulo')
print('-=-'*12)

a = float(input('Informe o valor do primeiro lado: '))
b = float(input('Informe o valor do segundo lado: '))
c = float(input('Informe o valor do terceiro lado: '))

if a > b+c or b > a+c or c > a+b:
    print('Os lados {}, {} e {} NÃO formam um triângulo.'.format(a, b, c))
else:
    print('Os lados {}, {} e {} formam um triângulo.'.format(a, b, c))
    if a == b and b == c:
        print('O triângulo que eles formam é equilátero.')
    else:
        if a != b and b != c and c != a:
            print('O triângulo que eles formam é escaleno.')
        else:
            if a == b or b == c or c == a:
                print('O triângulo que eles formam é isósceles.')
print('===FIM===')