print('Este programa calcula o desconto no preço de um produto')
preco = float(input('Digite o preço do produto: R$'))
desc = float(input('Digite o desconto em %: '))
novopreco = preco - desc*preco/100
print('O produto que custava R${:.2f}, com o desconto de {}%, passa a custar R${:.2f}.'.format(preco, desc, novopreco))
