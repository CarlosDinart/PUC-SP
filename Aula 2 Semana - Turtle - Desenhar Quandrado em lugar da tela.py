# 1- Metodo especifico:
from turtle import *

t= turtles()
""""tamanho_quadrado= 20
up() #Esta funcao puxa a caneta para cima;
goto(-200, 180)
down() #Esta funcao abaixa a caneta;

for _ in range(4): #desenha o quandrado;
    forward(tamanho_quadrado)
    left(90)

done()

# 2- Metodo Generico (para uso cotidiano):"""


def quadrado (x, y, lado, t): # t= tartaruga; Lado = tamanho do quadrado
    color()
    up()
    goto(x,y) #o ponto cartesiano onde vai ser desenhado o quadrado;
    down()
    for _ in range(4): # _ O traco entre o for e in range nao significa nada, apenas que nao estara
                       # usando variavel nehuma;
        forward(lado)
        left(90)

lado= 20
quadrado(10,40, lado, t)
done()



