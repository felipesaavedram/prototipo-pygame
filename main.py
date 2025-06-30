### 1 - IMPORTS:

import pygame
from pygame.locals import *

#-----------------------------------------------------------------------------
### 5 - CLASES:

# from classes.player import Player
# from classes.platform import Platform
# from classes.coin import Coin



#-----------------------------------------------------------------------------
### 2 - VARIABLES GLOBALES

# TAMAÑO PANTALLA

HEIGHT = 1000
WIDTH = 700

# FPS

FPS = 60

# ICONO DE PROGRAMA
ICON = pygame.image.load("assets/imgs/icon.jpg")

# FONDO DE PROGRAMA

BACKGROUND =  pygame.image.load("assets/imgs/background.jpg")

# IMAGEN DE PERSONAJE

PLAYER = pygame.image.load("assets/imgs/player.png")

#-----------------------------------------------------------------------------
### 3 - INICIALIZACIÓN:
 
pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_icon(ICON)

pygame.display.set_caption("  /ᐠ - ˕ -マ Ⳋ  Fortunyan  ")
def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                break

                
        window.blit(BACKGROUND, (0,-300))


        pygame.display.update()

    pygame.quit()
if __name__=="__main__":
    main()


#-----------------------------------------------------------------------------
### 6 - INSTANCIA DE OBJETOS:


#-----------------------------------------------------------------------------