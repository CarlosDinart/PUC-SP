import numpy as np
import turtle
from turtle import *
t= turtle.Screen()


#1) Criar matriz
def matriz_aleatoria():

    return np.random.randint(2, size=(20,20))


#3) cordenadas turtle
def em_coord_turtle(lin, col):

    xt = (col - meio_matriz) * tam_celular
    yt = (meio_matriz - lin) * tam_celular

    return xt, yt


#4) Desenhar celular
def desenhar_celular(xt, yt, cor):


    color(cor)
    up()
    goto(xt,yt)
    down()
    begin_fill()
    for _ in range(4):
        forward(tam_celular)
        left(90)

    end_fill()
    up()


#5) adicionar agente

def adicionar_agente():

    lin, col = celular_aleatoria()
    xt, yt = em_coord_turtle(lin, col)
    desenhar_agente(xt, yt, "yellow")


#6) celula aleatoria:

def celular_aleatoria():
    
    lin, col = np.random.randint(dim, size=(2))

    while (not eh_caminho(lin, col) == 1):

        lin, col = np.random.randint(dim, size=(2))

    return lin, col
    
#7) definir caminho

def eh_caminho(lin, col):

    return matriz[lin] [col] == 1

#8) desenhar agente
def desenhar_agente(xt, yt, cor):

    up()
    goto(xt + meio_celular, yt + meio_celular)
    down()
    dot(15, cor)

#9) desenhar pastilha
def desenhar_pastillha(xt, yt, cor):

    up()
    goto(xt + meio_celular, yt + meio_celular)
    down()
    dot(3, cor)


#10) desenhar labirinto

def criar_labirinto(p1=420, p2=420, p3=370, p4=0):

    tracer(False)
    bgcolor("black")
    hideturtle()
    t.setup(p1, p2, p3, p4)

    for lin in range(dim):
        for col in range(dim):

            xt, yt = em_coord_turtle(lin, col)
            if (matriz [lin] [col] ==1):

                desenhar_celular(xt, yt, "green")

                desenhar_pastillha(xt, yt, "white")

    update()


#2) Ler matriz


matriz = matriz_aleatoria()
print(matriz)


dim = len(matriz)
print(dim)

lin = len(matriz[:])
print(lin)

col = len(matriz[:])
print(col)

meio_matriz = dim //2
print(meio_matriz)

tam_celular = 20
meio_celular = tam_celular //2





def main():

   matriz_aleatoria()
   criar_labirinto()
   adicionar_agente()

   done()


main()










