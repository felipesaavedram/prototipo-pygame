# CLASSES/platform.py

import pygame
import os

class PlataformaGravedad(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        # --- Carga de la imagen de la plataforma ---
        try:
            platform_img_path = os.path.join("assets", "imgs", "platform.png")
            self.image = pygame.image.load(platform_img_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
        except pygame.error as e:
            print(f"Error al cargar la imagen de la plataforma: {e}")
            self.image = pygame.Surface([width, height])
            self.image.fill((0, 100, 200))
            print("Usando un rectángulo azul como marcador de posición para la plataforma.")

        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass