from turtle import *
#from math import floor
from freegames import floor


def Matriz():
    return [[1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], \
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], \
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1], \
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0], \
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], \
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1], \
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1], \
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], \
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0], \
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0], \
            [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], \
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1], \
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1], \
            [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], \
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], \
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1], \
            [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0], \
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]


# Dados da matriz:
matriz = Matriz()
tam_matriz = len(matriz)
meio_matriz = tam_matriz // 2
# print(meio_matriz)
lin = len(matriz[:])
col = len(matriz[:])
tam_celula = 20


def em_coord_turtle():
    """ Esta função definir Dada uma coordenada de indice da matriz (lin, col) transforma em coordenada Turtle """
    xt = (col - meio_matriz) * tam_celula  # xt refere -se ao coluna da matriz
    yt = (meio_matriz - lin) * tam_celula  # yt refere -se a linha da matriz

    #return xt, yt

    print(xt, yt)


#def em_coord_matriz(xt, yt):

    """Verificando o problema da transformacao das coordandas turtle me indices das matriz"""


    lin_indice = int(meio_matriz + (yt / tam_celula))  # Note-se que para cada coordenada turtle a variavel lin e col,
    col_indice = int(meio_matriz - (xt/ tam_celula))  # recebe o valor correspondente para indice da matriz que corresponde
    print("Para Coordenada Turtle", (xt, yt))  # celular;
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (0 / tam_celula))
    col_indice = int(meio_matriz - (0 / tam_celula))
    print("Para Coordenada Turtle: (0,0)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (10 / tam_celula))
    col_indice = int(meio_matriz - (10 / tam_celula))
    print("Para Coordenada Turtle: (10,10)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (5 / tam_celula))
    col_indice = int(meio_matriz - (5 / tam_celula))
    print("Para Coordenada Turtle: (5,5)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (7 / tam_celula))
    col_indice = int(meio_matriz - (7 / tam_celula))
    print("Para Coordenada Turtle: (7,7)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (19 / tam_celula))
    col_indice = int(meio_matriz - (19 / tam_celula))
    print("Para Coordenada Turtle: (19,19)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (20 / tam_celula))
    col_indice = int(meio_matriz - (20 / tam_celula))
    print("Para Coordenada Turtle: (20,20)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (30 / tam_celula))
    col_indice = int(meio_matriz - (30 / tam_celula))
    print("Para Coordenada Turtle: (30,30)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (39 / tam_celula))
    col_indice = int(meio_matriz - (39 / tam_celula))
    print("Para Coordenada Turtle: (39,39)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (40 / tam_celula))
    col_indice = int(meio_matriz - (40 / tam_celula))
    print("Para Coordenada Turtle: (40,40)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (180 / tam_celula))
    col_indice = int(meio_matriz - (20 / tam_celula))
    print("Para Coordenada Turtle: (180,20)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (180 / tam_celula))
    col_indice = int(meio_matriz - (0 / tam_celula))
    print("Para Coordenada Turtle: (180,0)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    lin_indice = int(meio_matriz + (185 / tam_celula))
    col_indice = int(meio_matriz - (0 / tam_celula))
    print("Para Coordenada Turtle: (185,0)")
    print("transformamos indices matriz", (col_indice, lin_indice))

    # return lin, col

    # obs): I) NOTE-SE PARA cada par ordenado da matriz (Lin, Col) é mapeado para pois cada celula e definida por duas
    # coordenadas turtle que representam toda area da celular. Somente o ponto central da matriz será mapeado
    # para a coordenada turtle (0,0), que é a coordenada (10,10) numa matriz quadrada…

    # II) NOTE-SE QUE ESSA SOLUCAO DEIXA UM PROBLEMA os exmplos ponteados na grade na imagem que cood turtle
    # exemplos (5, 5) = [9] [10]; (19,19) = [9] [10]; (20, 20) = [ 9, 11], (39, 39) = [8] [11]; (40, 40) = [8] [12]
    # , os indices referente ao col= xt, sempre esta tendente ficar fora do inicio da celula ou fora da celular
    # ao inves inserir dentro da celular, esta acao de transformacao a def coor matriz ja executa. PARA RESOLVER
    # ESTE PROBLEMA UTLIZAREMOS A FUNÇAO FLOOR DA freegames. Vejamos na funcao chao de celular, a seguir;


#def chao_da_celula(xt, yt):

    """ COMO RELATADOR ANTERIORMENTE NA FUNCAO TRANSFORMACAO TURTLLE EM INIDICES DA MATRIZ, Dados os índices da matriz (lin, col)
        , retorna as coordenadas do Turtle correspondentes.
        Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20, a chamada de função 
        'em_coord_turtle(0,0)' deve retornar (-200,200), E A chamada de função 'em_coord_turtle(10,10)' deverIA retornar 
        (0,0), POREM ESTA SOOLUCAO DEIXOU UM PROBLEMA COM lin DOS INDICES DA MATRIZ SEMPRE ESTA tendente ficar fora do 
        inicio da celula ou fora da celular ao inves inserir dentro da celular. PARA SOLUCIONAR USAREMOS : 
        
        Quem vai alinha o lin para dentro da celular turtle origem sera a execucao do floor q execulta a maior numero 
        da menor parte interia do intervalo do ponto lin dentro da area da celula = 20, e retornara a maior parte menor 
        inteira com referencia ao col turtle para o ponto da turtle da origem da celula. Vejamos a solucao:
        
        Exemplo 1:
        
        Chaox = int( floor( 5= col tutle, 20 = tam celular);
        
        Logo, o maior numero menor de col turtle = 5 / 20 => 0,25, assim, 0x 20= 0.
        
        Entao, 0 = col turtle da celular turtle corresponde ao [10], indice da matriz. 
        
        Exemplo 2:
        
        Chaox = int( floor( 187= col tutle, 20 = tam celular);

        Logo, o maior numero menor de col turtle = 187 / 20 => 0,25, assim, 9x 20= 180.

        Entao, 0 = col turtle da celular turtle [180], indice matriz.
        
        Testando exaustivamente:
        
        >>> (5//20)*20
        0
        >>> (10//20)*20
        0
        >>> (19//20)*20
        0
        >>> (20//20)*20
        20
        >>> (21//20)*20
        20
        >>> (21//20)*20
        20
        >>> (25//20)*20
        20
        >>> (30//20)*20
        20
        >>> (35//20)*20
        20
        >>> (39//20)*20
        20
        >>> (40//20)*20
        40
        >>> (45//20)*20
        40
        >>> (59//20)*20
        40
        >>> (187//20)*20 coodenada na turtle 187
        180 ------------> retornar a maior numero da menor parte interia do ponto turtle       
        
        """

    chao_xt = int(floor(xt, tam_celula))
    chao_yt = int(floor(yt, tam_celula))

    print("Coordenas Chao de celular turtle ", (chao_xt, chao_yt))


    chao_x0 = int(floor(5, tam_celula))
    print("Coordenada Chao de celular turtle (5):", (chao_x0))

    chao_x1 = int(floor(19, tam_celula))
    print("Coordenada Chao de celular turtle (19):", (chao_x1))

    chao_x2 = int(floor(20, tam_celula))
    print("Coordenada Chao de celular  turtle (20):", (chao_x2))

    chao_x3 = int(floor(39, tam_celula))
    print("Coordenada Chao de celular turtle (39):", (chao_x3))

    chao_x4 = int(floor(40, tam_celula))
    print("Coordenada Chao de celular turtle (40):", (chao_x4))

    chao_x5 = int(floor(187, tam_celula))
    print("Coordenada Chao de celular turtle (187):", (chao_x5))

    #return chao_xt, chao_yt



#def em_coord_matriz_chao_celular(chao_xt, chao_yt):

    """ Dada uma coordenada do chao Turtle (x,y), retorna os índices correspondentes␣
    ,→da matriz. Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula␣
    ,→20, a chamada de função 'em_coord_matriz_chao_celular(-200, 200)' deve retornar (0,0) e a
    chamada de função 'em_coord_matriz_chao_celular(0, 0)' deve retornar (10,10)."""

    #xt, yt = chao_xt, chao_yt
    chao_lin = int(meio_matriz + (chao_yt / tam_celula))
    chao_col = int(meio_matriz - (chao_xt / tam_celula))

    # Vejamos que retornar os inidices da matriz (chao_lin, chao_col) para a chamada da função
    # 'em_coord_matriz_chao_celular(-200, 200)'

    print("Coordenada turtle (200, -200) -> Coord Chao de celular matriz: ", (chao_lin, chao_col))

    chao_lin_xO = int(meio_matriz + (chao_x0 / tam_celula))
    chao_col_x0 = int(meio_matriz - (chao_x0 / tam_celula))

    print("Coordenada turtle (5,5) -> Chao de celular matriz:", (chao_lin_xO, chao_col_x0))

    chao_lin_x1 = int(meio_matriz + (chao_x1 / tam_celula))
    chao_col_x1 = int(meio_matriz - (chao_x1 / tam_celula))

    print("Coordenada turtle (19,19) -> Chao de celular matriz:", (chao_lin_x1, chao_col_x1))

    chao_lin_x2 = int(meio_matriz + (chao_x2 / tam_celula))
    chao_col_x2 = int(meio_matriz - (chao_x2 / tam_celula))

    print("Coordenada turtle (20,20) -> Chao de celular matriz:", (chao_lin_x2, chao_col_x2))

    chao_lin_x3 = int(meio_matriz + (chao_x3 / tam_celula))
    chao_col_x3 = int(meio_matriz - (chao_x3 / tam_celula))

    print("Coordenada turtle (39,39) -> Chao de celular matriz:", (chao_lin_x3, chao_col_x3))

    chao_lin_x4 = int(meio_matriz + (chao_x4 / tam_celula))
    chao_col_x4 = int(meio_matriz - (chao_x4 / tam_celula))

    print("Coordenada turtle (40,40) -> Chao de celular matriz:", (chao_lin_x4, chao_col_x4))

    chao_lin_x5 = int(meio_matriz + (chao_x5 / tam_celula))
    chao_col_x5 = int(meio_matriz - (chao_x5 / tam_celula))

    print("Coordenada turtle (187,187) -> Chao de celular matriz:", (chao_lin_x5, chao_col_x5))

def main():

    em_coord_turtle()
    #em_coord_matriz()
    #chao_da_celula()


main()
