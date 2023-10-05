"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 41
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#       índice de massa corporal      #'.upper())
print('###'*13)

altura = float(input('Digite sua altura em metros: '))
massa = float(input('Digite sua massa em kg: '))

imc = massa/((altura)**2)

if imc<18.5:
    print('IMC: {:.2f} \nClassificação: Abaixo do peso'.format(imc))
elif imc>=18.5 and imc<25:
    print('IMC: {:.2f} \nClassificação: Saudável'.format(imc))
elif imc>=25 and imc<30:
    print('IMC: {:.2f} \nClassificação: Peso em excesso'.format(imc))
elif imc>=30 and imc<35:
    print('IMC: {:.2f} \nClassificação: Obesidade Grau I'.format(imc))
elif imc>=35 and imc<40:
    print('IMC: {:.2f} \nClassificação: Obesidade Grau II (Severa)'.format(imc))
else:
    print('IMC: {:.2f} \nClassificação: Obesidade Grau III (Mórbida)'.format(imc))
