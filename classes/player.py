import pygame
import os 

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, initial_color_key="white"): # Agregamos initial_color_key
        super().__init__()
        
        self.width = width
        self.height = height
        
        # Diccionario para mapear las "claves de color" a los nombres de archivo de imagen
        self.image_files = {
            "white": "playerb.png",  # Gato blanco
            "green": "playerv.png",  # Gato verde
            "orange": "playern.png"  # Gato naranja
        }
        
        # --- Carga inicial de la imagen del jugador ---
        self.current_color_key = initial_color_key # Para saber qué imagen estamos usando
        self._load_and_scale_image(self.image_files[self.current_color_key])
        
        self.rect = self.image.get_rect(topleft=(x, y))

        self.change_x = 0 
        self.change_y = 0 
        self.gravedad = 0.5 
        self.gravedad_activa = True 
        self.on_ground = False 

    # Nuevo método auxiliar para cargar y escalar la imagen
    def _load_and_scale_image(self, filename):
        try:
            player_img_path = os.path.join("assets", "imgs", filename) 
            loaded_image = pygame.image.load(player_img_path).convert_alpha() 
            self.image = pygame.transform.scale(loaded_image, (self.width, self.height))
            self.using_image = True 
        except pygame.error as e:
            print(f"Error al cargar la imagen del jugador '{filename}': {e}")
            print("Usando un cuadrado gris como marcador de posición para el jugador.")
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill((150, 150, 150)) # Color gris de fallback
            self.using_image = False 

    def update(self):
        if self.gravedad_activa:
            self.change_y += self.gravedad 
        else: 
            self.change_y -= self.gravedad 
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 700: 
            self.rect.right = 700
        
    def move(self, dx, dy):
        self.change_x = dx
        self.change_y = dy

    def jump(self):
        if self.on_ground: 
            if self.gravedad_activa:
                self.change_y = -28 
            else:
                self.change_y = 28  
            self.on_ground = False 

    # Modificación importante del método set_color
    def set_color(self, color_key):
        """
        Cambia la imagen del jugador según la 'color_key' proporcionada.
        
        Args:
            color_key (str): Una clave que corresponde a una imagen en self.image_files 
                             ("white", "green", "orange").
        """
        if color_key in self.image_files:
            self.current_color_key = color_key
            self._load_and_scale_image(self.image_files[color_key])
        else:
            print(f"Clave de color '{color_key}' no reconocida.")

    def invert_gravity(self):
        self.gravedad_activa = not self.gravedad_activa 
        self.change_y = 0 
        self.on_ground = False