print('Programa de avaliação de empréstimo para compra de uma casa'.title())
casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o salário do comprador: R$'))
anos = int(input('Em quantos anos a casa vai ser paga? '))
prest = casa/(anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(casa, anos, prest))
if prest >= 0.3*sal:
    print('Empréstimo NEGADO.')
else:
    print('Empréstimos CONCEDIDO.')
