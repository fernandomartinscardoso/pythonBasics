'''
Para encontrar todos os números primos de 2 até n pelo método de Eratóstenes, segue-se os passos:
1. Criar a lista de inteiros consecutivos de 2 até n: (2, 3, 4, ..., n).
2. Inicialmente, tome p igual a 2, o menor dos números primos.
3. Enumere os múltiplos de p, contando-os em incrementos de p, a partir de 2p até n, e marque os incrementos na lista, sem marcar o próprio p.
4. Ache o menor número da lista que não foi marcado. Se o número já foi marcado, pare. Caso contrário, tome este número como o novo valor de p (que será o novo primo), e repita a partir do passo 3.
5. Quando o algoritmo terminar, os números não marcados na lista são os primos menores que n.

Como refinamento da busca, é suficiente marcar os números no passo 3 a partir de p**2, já que os menores múltiplos de p já estarão marcados.
Isso significa que o algoritmo pode terminar no passo 4 quando p**2 é maior que n.
'''