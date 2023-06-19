import rgb
import timers 
import pygame

#? Variables globales    
TITULO_VENTANA = "Turbo Tracks"
TITULO_BD = "database/bd_btf.db"
running = True
FPS = 60

#? Dimensiones de la pantalla
ANCHO_VENTANA = 375
ALTO_VENTANA =  667

DIMENSIONES_PANTALLA = (ANCHO_VENTANA, ALTO_VENTANA)
CENTER_X, CENTER_Y = ANCHO_VENTANA / 2, ALTO_VENTANA / 2

#? Recusos del juego
ICONO_PATH = "assets/img/logo.png"
CARRETERA_PATH = "assets/img/carretera.jpg"
PLAYER_PATH = "assets/img/player.png"
ENEMY_PATH = "assets/img/enemy.png"
MANCHA_PATH = "assets/img/oil.png"
MUSIC_PATH = "assets/aud/The-Perfect-Girl.mp3" 
CRASH_PATH = "assets/aud/car_explosion.wav"

#? Propiedades del Auto
ANCHO_AUTO, ALTO_AUTO = 75, 160
DIMENSIONES_AUTO = (ANCHO_AUTO, ALTO_AUTO)
movimiento_fondo = 12 #? Movimiento de la carretera
movimiento_obstaculo = movimiento_fondo *  .8

#? Posicion del vehiculo 
DESPLAZAMIENTO_X = 100
POSICIONES = [CENTER_X - DESPLAZAMIENTO_X, CENTER_X, CENTER_X + DESPLAZAMIENTO_X]
POS_PLAYER = (CENTER_X, ALTO_VENTANA - 140)
#? Movimientos verticales del auto
RANDOM = 0
IZQUIERDA = -1
DERECHA = 1 

#? Variables 
ingreso = ""
score = 0
game_over = True

#? TEXTO
ANCHO_TEXTO = 300
ALTO_TEXTO = 65

CENTER_TEXT_X = CENTER_X - ANCHO_TEXTO / 2
POS_SCORE = (20, ALTO_VENTANA - 40)
POS_INGRESO = (CENTER_TEXT_X, 60, ANCHO_TEXTO, ALTO_TEXTO)


#? Definimos la fuente y el tamaño de la misma 
FUENTE = pygame.font.SysFont("Arial", 36)
