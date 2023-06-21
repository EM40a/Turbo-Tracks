import pygame
from config import EXPLOSION_PATH

pygame.init()

def getSurface(path:str, filas:int, columnas:int) -> list:
    '''
    Crea una lista de sprites a partir de una imagen y la cantidad de filas y columnas de la misma    
    '''
    sprites = []

    sprite_img = pygame.image.load(path)
    fotograma_ancho = int(sprite_img.get_width() / columnas) 
    fotograma_alto = int(sprite_img.get_height() / filas) 
    
    for fila in range(filas):
        for col in range(columnas):
            x = col * fotograma_ancho
            y = fila * fotograma_alto
            #? Crea un rectangulo en la posicion x, y y con el ancho y alto del sprite 
            sprite = sprite_img.subsurface(pygame.Rect(x, y, fotograma_ancho, fotograma_alto)) 
            sprites.append(sprite) #? Agrega el sprite a la lista de sprites
    return sprites

def explosion_animation(ventana:pygame.Surface, posicion:int) -> None:
    '''
    Crea una animacion de explosion en la posicion indicada.
    '''
    explosion_sprites = getSurface(EXPLOSION_PATH, 2, 5)
    
    for sprite in explosion_sprites:
        sprite_rect = sprite.get_rect()
        sprite_rect.x = posicion[0]
        sprite_rect.y = posicion[1]
        ventana.blit(sprite, sprite_rect)
        pygame.display.update(sprite_rect) #? Actualiza solo el rectangulo del sprite
        pygame.time.delay(100)  # Pausa de 100 ms entre cada sprite