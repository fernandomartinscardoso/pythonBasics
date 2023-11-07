'''
Para encontrar todos os números primos de 2 até n pelo método de Eratóstenes, segue-se os passos:
1. Criar a lista de inteiros consecutivos de 2 até n: (2, 3, 4, ..., n).
2. Inicialmente, tome p igual a 2, o menor dos números primos.
3. Enumere os múltiplos de p, contando-os em incrementos de p, a partir de 2p até n, e marque os incrementos na lista, sem marcar o próprio p.
4. Ache o menor número da lista que não foi marcado. Se o número já foi marcado, pare. Caso contrário, tome este número como o novo valor de p (que será o novo primo), e repita a partir do passo 3.
5. Quando o algoritmo terminar, os números não marcados na lista são os primos menores que n.

Como refinamento da busca, é suficiente marcar os números no passo 3 a partir de p**2, já que os menores múltiplos de p já estarão marcados.
Isso significa que o algoritmo pode terminar no passo 4 quando p**2 é maior que n.

algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding sqrt(n) do
        if A[i] is true
            for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n do
                set A[j] := false

    return all i such that A[i] is true.
'''

print('###'*23)
print('#                      Detector de número primo                     #'.upper())
print('#       Detectando primos de 2 a n pelo método de Eratóstenes       #')
print('###'*23)

n = int(input("Digite o limite superior n do intervalo: \n"))
while n <= 2:
    print("Número inválido. Tente novamente!")
    n = int(input("Digite o limite superior n do intervalo: \n"))

lista = []
for a in range(0, n):
    lista.append(True)

parada = int(n**0.5)+1
for i in range(2,parada):
    if lista[i] == True:
        for j in range(i**2,n,i):
            lista[j] = False

primos = []
for k in range(2,n):
    if lista[k] == True:
        primos.append(k)

print('\nOs números primos menores que {} são: \n{}'.format(n,primos))

arquivo = open("numeros_primos.txt",'w')
arquivo.write("Os números primos menores que {} são: \n{}".format(n,primos))
arquivo.close()

# Espirais dos números primos: https://jaketae.github.io/study/prime-spirals/

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
for l in range(len(primos)):
    x.append(primos[l]*np.cos(primos[l]))
    y.append(primos[l]*np.sin(primos[l]))

plt.style.use('dark_background')
plt.figure(figsize=(10, 10))
plt.axis("off")
plt.scatter(x, y, s=0.5)
plt.show()