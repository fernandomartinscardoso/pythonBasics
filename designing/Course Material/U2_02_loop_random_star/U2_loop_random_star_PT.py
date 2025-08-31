"""
Este exemplo mostra:
- laço de repetição "for" para desenhar uma sequência de elementos
- random_int() para selecionar um número inteiro
- random_choice() para selecionar de uma coleção de itens
- random_seed() para fixar o ponto inicial do gerador aleatório
- estrutura condicional if/elif/else para decidir qual forma desenhar
- Uma definição de função de estrela de n pontas que você pode usar: star()
"""

def setup():
    size(600, 600)
    background(200)
    no_stroke()
    fill(0)
    # ransom_seed() define o início do gerador aleatório
    random_seed(100) # altere ou desligue para resultados diferentes
    for x in range(50, 600, 100): # x -no laço-> 50, 150, 250, 350, 450, 550
        n = random_int(1, 7)             # n -sorteado-> 1, 2, 3, 4, 5, 6, 7
        r = random_choice((10, 25, 40))  # r -sorteado-> 10, 25, 40
        if n == 1:                       # se n for igual a 1:
            circle(x, 300, 50)           # círculo em x, 300 com diâmetro 50
        elif n == 2:                     # senão se n for igual a 2:
            square(x - 25, 300 - 25, 50) # podia usado rect_mode(CENTER)!
        else:                            # senão, n não é 1 nem 2, então:
            star(x, 300, r, 50, n)       # x, y, raio_a, raio_b, pontas
        

def star(cx, cy, ra, rb, n, start_ang=0): # "estrela"
    step = TWO_PI / n  # 360° / número de pontos estrela (externos)
    begin_shape()      # inicia a forma poligonal
    for i in range(n): # para cada ponta da estrela
        ang = start_ang + step * i # ângulo para calcular a posição do vértice
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay) # adiciona o vértice calculado a partir do raio ra
        bx = cx + cos(ang + step / 2.0) * rb # note meio passo adicionado
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by) # adiciona o vértice calculado a partir do raio rb
    end_shape(CLOSE) # termina a forma e conecta ao primeiro vértice    
