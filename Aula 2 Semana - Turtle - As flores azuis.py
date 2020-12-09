from turtle import *
import random

for n in range(60):

    penup()  # penup-(i) esta funcao executa o modo de levantar a caneta sem escrever, movendo
                    # para acima e abaixo;
                    #(ii) esta funcao gera como resultado dois numeros aleatorios;

    i = random.randint(-200, 200)  # random.randint()- esta funcao executa dois numeros aletorios no
    j = random.randint(-200, 200)  # no plano cartesiano;

    goto(i, j) # goto() - (i) esta funcao utliza um par de coordenadas (x,Y) num sistema carteziano,
                            # onde a coordenada (0,0) da variavel (x,y) ocorrer nomeio do plano
                            # para uso de duas variáveis ​ usando as entradas horizontal e vertical,
                            # para mover a caneta naquela cordenada
                        #(ii) mas apenas uma das entradas funciona por vez;
                        #(iii) neste caso ela se move indo ate a cordanada indicada e abaixa a caneta;

    pendown()  #pendown - esta funcao puxa a caneta para baixo - desenhando ao mover;

    red_amount	= random.randint(	0,	30) / 100.0 # red_amount - defini a quantidade de cor vermelha;
    blue_amount	= random.randint(50, 100)	/	100.0 # blue_amount - defini a quantidade de cor azul;
    green_amount = random.randint(	0,	30)	/	100.0 # green_amount - defini a quantidade de cor verde;

    pencolor( (red_amount, green_amount, blue_amount) ) #pencolor - esta funcao defini a cor da caneta;

    circle_size = random.randint(10, 40)   #circle_size - esta variavel defini o tamanho do circulo;

    pensize(random.randint(1, 5)) # pensize- (i) esta funcao definir o tamanho da caneta;

    for i in range(6):        # esta funcao executa uma quantidade de circulos num determinado angulo;
        circle(circle_size)
        left(60)
done()