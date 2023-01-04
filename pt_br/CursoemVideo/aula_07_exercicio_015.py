print('Cálculo do valor do aluguel de um carro')
d = int(input('Quantos dias de uso do carro? '))
kr = float(input('Quantos km rodados? '))
aluguel = d*60 + kr*0.15
print('O total a pagar é de R${:.2f}'.format(aluguel))
