velocidade = float(input('Qual a velocidade do carro (em km/h)? '))
if velocidade > 80:
    multa = 7*(velocidade-80)
    print("""Multado! Você excedeu o limite permitido de 80 km/h.
Você deve pagar uma multa de R${:.2f}!
Tenha um bom dia e dirija com segurança!""".format(multa))
else:
    print('Tenha um bom dia e dirija com segurança!')
