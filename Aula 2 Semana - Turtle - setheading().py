from turtle import *

for angle in range(0, 360, 15):

    setheading(angle) #setheading() - esta funcao defjni a direcao da tartaruga nos anglos definidos;

    forward(100)

    write(str(angle) + '°') #write() - esta funcao defini a execucao para escrever na tela do turtle;

    backward(100) #backward() - esta funcao executa que mova a tartaruga para trás na distância ,
                  # no sentido oposto à direção que a tartaruga está indo;

done() # esta funcao defini um limitador na execucao da tartaruga;
