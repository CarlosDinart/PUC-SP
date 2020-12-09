from turtle import *

for i in range(10):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)

for i in range(30):
    undo() # Esta funcao Desfaz (repetidamente) a(s) última(s) ação(ões) da tartaruga. O número de ações
            # desfazer disponíveis é determinado pelo tamanho do undobuffer.

done()

