#--------------------------------------------------#
#
#                   INTEGRANTES
#
#                   Paola Leiva
#                   Felipe Saavedra
#
#
#----------------------------------------------------#


### 1 - IMPORTS
import pygame
import os

from pygame.locals import *

from classes.player import Player
from classes.platform import PlataformaGravedad
from classes.coin import Coin


#-----------------------------------------------------------------------------
### 2 - VARIABLES GLOBALES

HEIGHT = 1000 
WIDTH = 700   

FPS = 60 

# Nota: Los colores GREEN, ORANGE, WHITE ya no se usan directamente para el fill del jugador
# pero se mantienen si los necesitas para otras visualizaciones o lógicas.
GREEN = (0, 255, 0)     
ORANGE = (255, 165, 0)  
WHITE = (255, 255, 255) 

ICON = pygame.image.load(os.path.join("assets", "imgs", "icon.jpg")) 
BACKGROUND = pygame.image.load(os.path.join("assets", "imgs", "background.jpg")) 
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT)) 

pygame.mixer.init() 
pygame.mixer.music.load(os.path.join("assets", "audio.mp3")) 
pygame.mixer.music.set_volume(0.4) 
pygame.mixer.music.play(-1)  

#-----------------------------------------------------------------------------
### 3 - INICIALIZACIÓN DE PYGAME Y VENTANA
 
pygame.init() 
pygame.font.init() 

window = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_icon(ICON) 
pygame.display.set_caption("  /ᐠ - ˕ -マ Ⳋ  Fortunyan  ") 

def main():
    global font, small_font 
    font = pygame.font.SysFont(None, 48) 
    small_font = pygame.font.SysFont(None, 32) 

    clock = pygame.time.Clock() 
    
#-----------------------------------------------------------------------------
    ### 6 - INSTANCIA DE OBJETOS Y GRUPOS DE SPRITES

    # El jugador ahora se inicializa con una "clave de color" por defecto ("white")
    player = Player(x=WIDTH // 2 - 25, y=HEIGHT // 2 - 25, width=100, height=100, initial_color_key="white")

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player) 

    coins_group = pygame.sprite.Group() 
    num_coins = 6 
    coin_positions = [
        (100, 200), (250, 350), (400, 250),
        (550, 400), (150, 500), (600, 600)
    ]
    for i in range(num_coins):
        coin = Coin(coin_positions[i][0], coin_positions[i][1])
        all_sprites.add(coin)     
        coins_group.add(coin)     

    score = 0 

    gravity_platform = PlataformaGravedad(x=WIDTH // 2 - 150, y=450, width=300, height=80)
    all_sprites.add(gravity_platform) 
    
    platforms_group = pygame.sprite.Group() 
    platforms_group.add(gravity_platform) 


    #-----------------------------------------------------------------------------
    ### 4 - BUCLE PRINCIPAL DEL JUEGO

    run = True 
    while run:
        clock.tick(FPS) 
        
        for event in pygame.event.get():
            if event.type == QUIT: 
                run = False 
                break 
            
            if event.type == KEYDOWN:
                if event.key == K_LEFT: 
                    player.change_x = -5
                if event.key == K_RIGHT:
                    player.change_x = 5
                if event.key == K_SPACE: 
                    player.jump()

                # CAMBIO DE IMAGEN DEL JUGADOR SEGÚN LA TECLA PRESIONADA
                if event.key == K_b: # Tecla 'B' para el gato verde (playerV.png)
                    player.set_color("green") 
                if event.key == K_n: # Tecla 'N' para el gato naranja (playerN.png)
                    player.set_color("orange") 
                if event.key == K_m: # Tecla 'M' para el gato blanco (playerB.png)
                    player.set_color("white") 

            if event.type == KEYUP:
                if event.key == K_LEFT and player.change_x < 0:
                    player.change_x = 0
                if event.key == K_RIGHT and player.change_x > 0:
                    player.change_x = 0

        #-----------------------------------------------------------------------------
        ### 5 - LÓGICA DEL JUEGO (ACTUALIZACIONES Y COLISIONES)

        player.on_ground = False 
        
        player.update() 
        
        player.rect.x += player.change_x 
        platform_hit_list = pygame.sprite.spritecollide(player, platforms_group, False)
        for platform in platform_hit_list:
            if player.change_x > 0: 
                player.rect.right = platform.rect.left 
            elif player.change_x < 0: 
                player.rect.left = platform.rect.right 
            player.change_x = 0 

        player.rect.y += player.change_y 
        platform_hit_list = pygame.sprite.spritecollide(player, platforms_group, False)
        for platform in platform_hit_list:
            if player.change_y > 0: 
                player.rect.bottom = platform.rect.top 
                player.change_y = 0 
                player.on_ground = True 
            elif player.change_y < 0: 
                player.rect.top = platform.rect.bottom 
                player.change_y = 0 
                if not player.gravedad_activa:
                    player.on_ground = True

            if isinstance(platform, PlataformaGravedad): 
                player.invert_gravity() 

        if player.rect.bottom > HEIGHT:
            player.rect.bottom = HEIGHT 
            player.change_y = 0 
            player.on_ground = True 
            
        if player.rect.top < 0:
            player.rect.top = 0 
            player.change_y = 0 
            player.on_ground = True 
        
        coins_collected = pygame.sprite.spritecollide(player, coins_group, True)
        for coin in coins_collected:
            score += 1 

        #-----------------------------------------------------------------------------
        ### 7 - DIBUJAR EN PANTALLA

        window.blit(BACKGROUND, (0,0)) 

        all_sprites.draw(window) 

        score_text = small_font.render(f"Monedas: {score}", True, WHITE) 
        window.blit(score_text, (10, 10)) 

        pygame.display.update() 

    #-----------------------------------------------------------------------------
    ### 8 - SALIR DEL JUEGO
    pygame.quit() 

if __name__=="__main__":
    main()

#-----------------------------------------------------------------------------