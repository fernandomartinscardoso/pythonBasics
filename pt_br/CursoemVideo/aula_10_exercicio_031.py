dist = float(input('Digite a distância da viagem em km: '))
if dist <= 200:
    preco = 0.5*dist
else:
    preco = 0.45*dist
print('O preço da passagem é de R${:.2f}.'.format(preco))
