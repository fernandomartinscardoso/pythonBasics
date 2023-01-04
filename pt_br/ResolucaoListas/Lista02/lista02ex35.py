"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 35
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#          Avaliador de Datas         #'.upper())
print('###'*13)

print('Este programa avalia se uma data inserida é válida.')


ano = int(input('Insira o ano: '))
if ano < 1:
    print('Ano inserido inválido.')
else:
    mes = int(input('Insira o mês: '))
    if mes<1 and mes>12:
        print('Mês inserido inválido.')
    else:
        dia = int(input('Insira o dia: '))
        if dia<1 and dia>31:
            print('Dia inserido inválido.')
        elif mes==4 or mes==6 or mes==9 or mes==11 and dia>30:
            print('Dia inserido inválido.')
        elif mes==2:
            if dia>29 and ano%4==0 and ano%100!=0:
                print('Dia inserido inválido.')
            elif dia>28 and (ano%4!=0 or ano%100==0):
                print('Dia inserido inválido.')
            else:
                print('A data {}/{}/{} é válida.'.format(dia, mes, ano))
        else:
            print('A data {}/{}/{} é válida.'.format(dia,mes,ano))
