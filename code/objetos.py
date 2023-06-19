from config import *
import crear 

#? Objetos del juego 
CARRETERA = crear.Superficie(CARRETERA_PATH, (ANCHO_VENTANA, ALTO_VENTANA * 2), (CENTER_X, 0))
MANCHA = crear.Obstaculo(MANCHA_PATH, (115, 120), POS_PLAYER)
PLAYER = crear.Personaje(PLAYER_PATH, DIMENSIONES_AUTO, POS_PLAYER)
ENEMY = crear.Obstaculo(ENEMY_PATH, DIMENSIONES_AUTO, POS_PLAYER)

texto_jugar = crear.Texto(FUENTE, "Jugar", rgb.AMARILLO, (142, 477))
texto_home = crear.Texto(FUENTE, "Volver", rgb.BLANCO, (142, 477))
texto_ranking = crear.Texto(FUENTE, "Ranking", rgb.GRIS_300, (121.5, 554))

menu_principal = crear.Menu() 
#? Dimensiones de los rectangulos 
MANCHA.rect.width = ANCHO_AUTO
MANCHA.rect.height /= 2