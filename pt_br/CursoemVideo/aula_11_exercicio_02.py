print('\033[34mConversor de moedas\033[m')
d = float(input('Digite o valor do dólar em reais na cotação de hoje: '))
r = float(input('Quantos reais você tem disponíveis? '))
dolar = r/d
print('Com \033[36mR${:.2f}\033[m, você pode comprar \033[32m${:.2f}\033[m.'.format(r, dolar))