print('###'*16)
print('#  Avaliando o Índice de Massa Corporal (IMC)  #')
print('###'*16)
peso = float(input('Insira o peso (em kg): '))
altura = float(input('Insira a altura (em m): '))
imc = peso/(altura**2)
print('IMC = {:.1f}'.format(imc))
if imc < 18.5:
    print('Avaliação: Abaixo do peso')
elif imc < 25:
    print('Avaliação: Peso ideal')
elif imc < 30:
    print('Avaliação: Sobrepeso')
elif imc < 40:
    print('Avaliação: Obesidade')
else:
    print('Avaliação: Obesidade Mórbida')
# Complementando a informação com a faixa de peso ideal:
p_min = 18.5*altura**2
p_max = 25*altura**2
print('Para a altura de {:.2f} m, a faixa de peso ideal está entre {:.1f} e {:.1f} kg.'.format(altura, p_min, p_max))
