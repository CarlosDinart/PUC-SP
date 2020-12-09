#maze - labirinto mova-se de um lado para o outro
# Inspirado por um universo em uma linha de código com 10 IMPRESSÕES.
# Toque na tela para traçar um caminho de um lado a outro.

import pygame
import random

# definir a largura e altura da tela
screenWidth, screenHeight = (800, 800) #screen - é um integrado que representa a exibição da janela;
                                       # Width - este operador controlar a largura;
                                       # Height - este operador controlar a altura de sua janela;
                                       # obs: O código define o tamanho da janela como 300 pixels
                                            # em cada dimensão.

pygame.init() # pygame.init()- é responsável por inicializar todos os módulos do pygame;

pygame.display.set_caption("10 PRINT in Pygame") #Esta funcao define a legenda da janela atual
screen = pygame.display.set_mode((screenWidth, screenHeight)) # Esta funcao executar inicializar uma janela
                                                # ou tela para exibição;

running = True

#define cores da janela do jogo;
white = (255, 255, 255)
black = (0, 0, 0)

# tamanho do quadrado, em pixels
square = 20

def drawScreen():  #drawScreen() - Esta função e definir as dimensões da janela.
    screen.fill(black) # Esta funcao chamada do método preenche a tela com uma cor sólida,
                        # especificada como uma tupla de cor;

    #
    for x in range(0, screenWidth, square):
        for y in range(0, screenHeight, square):
            if random.random() > 0.5:
                pygame.draw.line(screen, white, (x, y), (x + square, y + square))
                #draw.line - esta funcao desenha uma linha entre os 2 pontos fornecidos;

            else:
                pygame.draw.line(screen, white, (x, y + square), (x + square, y))

while running:
    key = pygame.key.get_pressed()
    # only draw if user presses spacebar
    if key[pygame.K_SPACE]:
        drawScreen()
    # quit if user presses q
    if key[pygame.K_q]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # this updates the display
    pygame.display.flip()