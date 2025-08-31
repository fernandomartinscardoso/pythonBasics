"""
Este exemplo mostra:
- Como definir uma função que desenha um olho (eye) e como usar essa função
- Vocabulário de programação:
    - "chamar" uma função, "passar valores ou argumentos" 
    - "cabeçalho" e "corpo" da definição de uma função
    - "parâmetros", nomes designados na definição da função
"""

def setup():
    size(600, 600)
    background(0, 0, 100)
    eye(200, 150, 100) # chamando a função eye (para desenhar um olho) 
    eye(300, 400, 150) # <- valores (argumentos) passados para x, y e h do olho 
    eye(500, 200, 50)  # quando chamamos uma função seu nome tem parenteses
                       # que podem ou não precisar de argumentos
                       # fill(255) <- 255 é o argumento "passado"
                       # no_fill() <- a função no_fill não recebe argumentos
   
#       x, y, h       < - são os nomes dos parâmetros (que recebem os valores)
def eye(x, y, h):   # <- este é "cabeçalho" da definição da função eye (olho)
    no_stroke()     # <- aqui começa o "corpo" da função eye (com a indentação)              
    fill(255)       # preenchimento branco       
    ellipse(x, y, h * 3, h)
    fill(255, 0, 0) # preenchimento vermelho
    ellipse(x, y, h, h)
    fill(0)         # preenchimento preto
    ellipse(x, y, h * 0.2, h * 0.2)
#                     <-  aqui termina o "corpo" da função eye