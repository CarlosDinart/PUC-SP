# Metodo para execucao do Desenho da Matriz:

# 1 Passo - Criar uma Matriz:

# 1.1. Declarar a Matriz - criar a estrutura da matriz (definindo numero de linhas e colunas):



matriz =   [[1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0],\
            [1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1],\
            [1,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1],\
            [1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0],\
            [0,1,1,0,0,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0],\
            [0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],\
            [0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1],\
            [0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1],\
            [0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1],\
            [0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1],\
            [0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0],\
            [1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0],\
            [1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0],\
            [0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1],\
            [0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,1,1],\
            [0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1],\
            [1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1],\
            [1,1,1,0,0,0,0,1,1,0,1,0,1,1,1,0,1,1,1,1],\
            [1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,1,0,0],\
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]]  # os numeros zeros sao valores aleatrorios apenas para montar
                                                        # a estrutura da matriz;


# 1.2. Declaramos o tamanho da matriz e do quadrado:

tam_lin = len(matriz[0])
tam_col = len(matriz)
tam_matriz = len(matriz)
tam_quadrado = 20
print("Matriz = linhas {} x colunas {}".format(tam_lin, tam_col))
print(tam_matriz)
# 1.3. Declaramos o inicio do intervalo da variavel linha e coluna
lin = len(matriz[:])
col = len(matriz[:])

# 1.4.Definiremos os valores de cada elemento da matriz em coordanada turtle:

# 1.4.1. Declarar o meio da matriz:

meio_matriz = tam_matriz // 2
print(meio_matriz)

# 1.4.2. Obtendo as coordnadas turtle xt e yt:


xt = (col - meio_matriz) * tam_quadrado
yt = (meio_matriz - lin) * tam_quadrado

cordenadas = (xt, yt)
print(cordenadas)

#1.5. definindo o quadrado (celula):
from turtle import *
t= turtles()

quadrado = (xt, yt, tam_quadrado, t)
color()
up()
goto(xt,yt) #o ponto cartesiano onde vai ser desenhado o quadrado;
down()
for _ in range(4): # _ O traco entre o for e in range nao significa nada, apenas que nao estara
                       # usando variavel nehuma;
    forward(tam_quadrado)
    left(90)

#1.7.2. desenhando matriz:

desenhar = len(matriz)
for lin in range(tam_matriz):    # este comando repeticao percorrer e ler toda a matriz;
    for col in range(tam_matriz):
        print(lin, col)                 # Defini os indices nas posicoes referente ao 0 e 1 na matriz
        xt, yt = cordenadas(lin, col)   # transforma as coredandas tutler em indices da l
        quadrado(lin, col)
    up()

# Dulvida: NA execucao do codigo nao consigo montar a grade ?

