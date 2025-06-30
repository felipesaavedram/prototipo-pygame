### 1 - IMPORTS:

import pygame
from pygame.locals import *

#-----------------------------------------------------------------------------
### 2 - VARIABLES GLOBALES

# TAMAÑO PANTALLA

HEIGHT = 600
WIDTH = 600

# FPS

FPS = 60

# COLORES
DARKRED = (pygame.Color("darkred"))

# ICONO DE PROGRAMA
ICON = pygame.image.load("assets/imgs/icon.png")

# FONDO DE PROGRAMA

BACKGROUND =  pygame.image.load("assets/imgs/background.jpg")

#-----------------------------------------------------------------------------
### 3 - INICIALIZACIÓN
 
pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_icon(ICON)

pygame.display.set_caption(" THE NYAN-CUT   /ᐠ - ˕ -マ Ⳋ")
def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                break

        window.fill(DARKRED)
        #window.fill(pygame.Color("deepskyblue4"))
        
        window.blit(BACKGROUND, (0,0))


        pygame.display.update()

    pygame.quit()
if __name__=="__main__":
    main()


#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------