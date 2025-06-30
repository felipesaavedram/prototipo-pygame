### 1 - IMPORTS:
import pygame

# ------------------------------------------------------------------ #
### 2 - CLASS:

class Player:
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, color: str):
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect(center =(pos_x, pos_y))

    def draw(self, window):
        window.blit(self.surface, self.rect)
        pygame.draw.rect(self.surface, (255,255,255), self.surface.get_rect(),2)
