print('{:=^23}'.format('Lojas Martins').upper())
valor = float(input('Insira o valor da compra: R$'))
print('''Insira a condição de pagamento:
[1] À vista no dinheiro ou cheque
[2] À vista no cartão
[3] Em até 2 parcelas no cartão
[4] Em 3 ou mais parcelas no cartão''')
escolha = int(input('Condição escolhida: '))
if escolha==1:
    valorfinal = 0.9*valor
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valorfinal))
elif escolha==2:
    valorfinal = 0.95*valor
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valorfinal))
elif escolha==3:
    prest = valor/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(prest))
elif escolha==4:
    valorfinal = 1.2*valor
    parcelas = int(input('Qual a quantidade de parcelas?\n'))
    prest = valorfinal/parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, prest))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valorfinal))
else:
    print('Opção de condição inválida!')
