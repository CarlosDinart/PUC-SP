from turtle import *

penup()

for i in range(30, -1, -1):
    stamp() #Esta funcao defini execultar o Carimbo uma cópia da forma da tartaruga na tela
            # na posição atual da tartaruga.

    left(i)
    forward(20)

done()