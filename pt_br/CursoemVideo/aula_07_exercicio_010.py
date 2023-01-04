print('Conversor de moedas')
d = float(input('Digite o valor do dólar em reais na cotação de hoje: '))
r = float(input('Quantos reais você tem disponíveis? '))
dolar = r/d
print('Com R${:.2f}, você pode comprar ${:.2f}.'.format(r, dolar))
