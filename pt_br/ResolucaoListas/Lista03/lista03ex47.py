"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 47
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#                      Calculadora simples                       #'.upper())
print('#     Escolha uma operação no menu e opere com dois números      #')
print('###'*22)

print('''Opções:
# Digite 1 para a adição
# Digite 2 para a subtração 
# Digite 3 para a multiplicação
# Digite 4 para a divisão
# Digite 5 para sair''')

while True:
   opt = input("Digite a opção de operação: ")
   if opt == '1':
      n1 = float(input("Insira o primeiro número: "))
      n2 = float(input("Insira o segundo número: "))
      soma = n1 + n2
      print("{} + {} = {}".format(n1, n2, soma))
   elif opt == '2':
      n1 = float(input("Insira o primeiro número: "))
      n2 = float(input("Insira o segundo número: "))
      sub = n1 - n2
      print("{} - {} = {}".format(n1, n2, sub))
   elif opt == '3':
      n1 = float(input("Insira o primeiro número: "))
      n2 = float(input("Insira o segundo número: "))
      prod = n1 * n2
      print("{} * {} = {}".format(n1, n2, prod))
   elif opt == '4':
      n1 = float(input("Insira o primeiro número: "))
      n2 = float(input("Insira o segundo número: "))
      while n2 == 0:
         print("O divisor não pode ser nulo.")
         n2 = float(input("Insira o segundo número: "))
      div = n1 / n2
      print("{} / {} = {}".format(n1, n2, div))
   elif opt == '5':
      print("Até breve!")
      break
   else:
      print("Opção inválida. Tente novamente!")
   