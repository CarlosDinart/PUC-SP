from turtle import *

cores = ["red", 'purple', 'blue', 'green', 'yellow', 'orange', 'black'] # e uma lista

speed(0) #speed - é a funcao que executa a velocidade da caneta;
# ou speed('fastest') #fastest - defini a velocidade da caneta sem atribuicao de valor:

for x in range(360): # utiliza o o comando for que vai variar entre 0 e 359;
                     # x - sera a variaca da caneta;

    pencolor( cores[x % 7] ) #pencolor -(i) e a funcao que defini a cor da escrita da caneta;
                                       #(ii) que tera a funcao de utlizar cada uma cor da lista de cores;

                             # % - é um operador do modulo do resto divisor,

                             # x % 7- (i) este operador defini qeu o resto da divisao estara entre 0 e 6;
                                     #(ii) esta operação definira que o resto da divisão estará entre 0 e 6,
                                     # executando as cores da lista através da variável (x) aplicando cada cores
                                     # que correspondem a cada uma posição da lista respeitado a sua  sequencia
                                     # distribuída na lista, e executando a partir variável inicial até a final,
                                     # quando atingira a última variável da lista retornara para variável inicial
                                     # de cor, realizando, assim, sucessivos laços de execução de repetição;



    width(x / 100 + 1)  #width - e a funcao que defini o comprimento da caneta;
                        # (x / 100 + 1)- definira a espessura da caneta na sua avariacao atraves de (x);

    forward(x) #ditancia da reta;
    left(59) # 59 graus - e para que aconteca um lopp perfeito e tenho efeito na vizualizacao;

done()

#Dulvida: Não conseguir executar a função type no código?






