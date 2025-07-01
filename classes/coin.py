import pygame
import os

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, width=30, height=30):
        super().__init__()
        # --- Carga de la imagen de la moneda ---
        try:
            coin_img_path = os.path.join("assets", "imgs", "coin.png")
            self.image = pygame.image.load(coin_img_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
        except pygame.error as e:
            print(f"Error al cargar la imagen de la moneda: {e}")
            self.image = pygame.Surface([width, height])
            self.image.fill((255, 215, 0))
            print("Usando un cuadrado dorado como marcador de posición para la moneda.")

        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass