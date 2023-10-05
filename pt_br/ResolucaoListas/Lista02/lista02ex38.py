"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 38
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#          Avaliador de datas         #'.upper())
print('###'*13)

data = str(input('Digite a data no formato DD.MM.AAAA: \n '))

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

# Ano bissexto: 
# -Se é divisível por 100, deve ser divisível por 400 também;
# -Do contrário, basta ser divisível por 4. 

if ano%400==0:
    bissexto = 'S'
elif ano%100!=0 and ano%4==0:
    bissexto = 'S'
else:
    bissexto = 'N'

if bissexto == 'N':
    if dia <= 0:
        print('Data inválida!')
    elif (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia>31:
        print('Data inválida!')
    elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
        print('Data inválida!')
    elif mes==2 and dia>28:
        print('Data inválida!')
    else:
        print('Data válida!')
else:
    if dia <= 0:
        print('Data inválida!')
    elif (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia>31:
        print('Data inválida!')
    elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
        print('Data inválida!')
    elif mes==2 and dia>29:
        print('Data inválida!')
    else:
        print('Data válida!')
