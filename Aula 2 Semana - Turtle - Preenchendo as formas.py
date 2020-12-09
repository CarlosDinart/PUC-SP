from turtle import *

fillcolor('purple') # fillcolor() - esta funcao retorna ou defina a cor de preenchimento;

pensize(10) #pensize()- esta funcao defina a espessura da linha para a largura ou retorne-a.
                # Se resizemode for definido como “auto” e a forma de tartaruga for um polígono,
                # esse polígono será desenhado com a mesma espessura de linha. Se nenhum argumento
                # for fornecido, o pensize atual é retornado.

pencolor('black')  #pencolor() - esta funcao defini a cor da caneta;
forward(100)
begin_fill() # begin_fill() - Para ser chamado antes de desenhar uma forma a ser preenchida;
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill() #end_fill() -Esta funcao Preenche a forma desenhada após a última chamada para begin_fill();

done()


