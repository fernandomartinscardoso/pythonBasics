"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 45
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#                    Conversor de Velocidade                     #'.upper())
print('#   Escolha se quer converter de km/h para m/s ou vice-versa     #')
print('###'*22)

print("Digite k2m para converter de km/h para m/s, m2k para converter de m/s para km/h ou qualquer outra opção para encerrar o programa.")

while True:
    opt = input("Digite a opção escolhida: ")
    if opt == 'k2m':
        kmph = float(input('Insira a velocidade em km/h: '))
        mps = 3.6*kmph
        print("{} km/h = {} m/s".format(kmph, mps))
    elif opt == 'm2k':
        mps = float(input('Insira a velocidade em m/s: '))
        kmph = mps/3.6
        print("{} m/s = {} km/h".format(mps, kmph))
    else:
        break
