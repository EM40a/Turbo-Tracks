from config import *
import pygame
import traceback
import random

class Superficie:
    def __init__(self, imagen:str, dimensiones:tuple|list, posicion:tuple|list=(0, 0)) -> None:
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, dimensiones)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = posicion[0]
        self.rect.centery = posicion[1]
        
    def dibujar(self, ventana:pygame.Surface) -> None:
        '''
        Dibuja la superficie en la ventana recibida como parametro.
        En caso de error, lo muestra en pantalla.
        '''
        try:
            ventana.blit(self.imagen, self.rect)
            
        except Exception as error:
            print(f"Error al dibujar la imagen: {error}")
            
    def actualizar(self, velocidad:int) -> None:
        '''
        Actualiza la posicion de la superficie de forma vertical a la velocidad recibida por parametro.
        Si la superficie sale de la pantalla, se reposiciona en la parte superior de la pantalla.   
        En caso de error, lo muestra en pantalla.
        '''
        try:
            self.rect.y += velocidad
            
            #* Reposicionamiento de la superficie 
            if self.rect.y >= 0:
                self.rect.y = -ALTO_VENTANA
                
        except TypeError as error:
            print("Error al actualizar la posicion: ", error)
        
    
    def colisionar(self, enemigo:object) -> bool:
        '''
        Devuelve True si la superficie colisiona con el enemigo recibido como parametro. De lo contrario, devuelve False.
        '''
        try:
            #* Colision con el rectangulo del enemigo 
            if self.rect.colliderect(enemigo.rect):
                return True
            return False
        
        except:
            traceback.print_exc()

class Personaje(Superficie):
    def mover(self, direccion:int, desplazamiento:int) -> None:
        '''
        Mueve el personaje en la direccion recibida como parametro a la velocidad recibida como parametro dentro de los limites de la pantalla segun la direccion:
        
        * 0: Movimiento aleatorio.
        * 1: Movimiento hacia la derecha.
        * -1: Movimiento hacia la izquierda.

        En caso de error, lo muestra en pantalla.
        '''
        try:
            #? Movimiento aleatorio
            if direccion == 0:
                direccion = random.choice([-1, 1])
            
            #? Movimiento hacia la izquierda
            if direccion == -1:
                nueva_x = self.rect.x - desplazamiento
                if nueva_x >= 0:
                    self.rect.x = nueva_x

            #? Movimiento hacia la derecha
            elif direccion == 1:
                nueva_x = self.rect.centerx + desplazamiento
                if nueva_x <= ANCHO_VENTANA - ANCHO_AUTO / 2:
                    self.rect.centerx = nueva_x
        except:
            traceback.print_exc()
                
            
class Obstaculo(Personaje):
    def avanzar(self, velocidad:int):
        #? Posicion aleatoria en y para simular que aparece desde arriba
        y_random = random.randrange(-400, -self.imagen.get_height(), 25) 

        self.rect.y += velocidad 
        if self.rect.y > ALTO_VENTANA:
            self.rect.y = y_random
            self.aparecerRandom()
            
    def aparecerRandom(self):
        '''
        Aparece el obstaculo en una posicion aleatoria de la pantalla.
        
        Posiciones: (Left, Center, Right)
        '''
        
        #? sample devuelve una lista con un elemento aleatorio de la lista recibida como parametro 
        POS_RANDOM = random.sample(POSICIONES, 1)
        self.rect.centerx = POS_RANDOM[0]
        
class Texto:
    def __init__(self, fuente, texto:str, color:tuple, posicion:tuple) -> None:
        self.fuente = fuente
        self.texto = texto
        self.color = color
        self.posicion = posicion

    def renderizar(self, superficie:pygame.Surface) -> None:
        '''
        Renderiza el texto en la superficie recibida como parametro.
        
        En caso de error, lo muestra en pantalla.
        '''
        try:
            texto_surface = self.fuente.render(self.texto, True, self.color)
            superficie.blit(texto_surface, self.posicion)
        except:
            traceback.print_exc()

class Menu:
    def __init__(self) -> None:
        self.ventana = {"Inicio": 0, "Ranking": 1, "Juego": 2}
        self._ventana_actual = self.ventana["Inicio"]
    
    #? Propiedad para acceder a la ventana actual 
    @property
    def actual(self):
        return self._ventana_actual
    
    #? Setter para cambiar la ventana actual
    @actual.setter
    def actual(self, nueva_ventana:str):
        '''
        Cambia la ventana actual por la ventana recibida como parametro.
        
        En caso de error, lo muestra en pantalla.
        '''
        try:
            self._ventana_actual = self.ventana[nueva_ventana]
        
        except:
            traceback.print_exc()
            