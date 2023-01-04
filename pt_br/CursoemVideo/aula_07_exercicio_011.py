print('Este programa calcula a área de uma parede e a quantidade de tinta para pintá-la')
print('Considera-se, pelo fabricante, que 1 l de tinta pinta 15 m² de parede.\n')
l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
a = l*h
litros = a/15
print('A parede tem {:.2f} m². Você precisa de {:.1f} l de tinta para pintá-la.'.format(a, litros))
