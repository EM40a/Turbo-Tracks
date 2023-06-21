import pygame, ranking
from pygame.locals import *
from config import *
from objetos import *
from sprite import explosion_animation

pygame.init()
#? Definimos el tamaño, icono y titulo de la ventana 
ventana_principal = pygame.display.set_mode(DIMENSIONES_PANTALLA)

pygame.display.set_caption(TITULO_VENTANA)
ICONO = pygame.image.load(ICONO_PATH) 
pygame.display.set_icon(ICONO)

#? Iniciamos el mixer para reproducir la musica del juego
pygame.mixer.init()
SOUNDTRACK = pygame.mixer.Sound(MUSIC_PATH)
CRASH = pygame.mixer.Sound(CRASH_PATH)
SOUNDTRACK.set_volume(0.3)
CRASH.set_volume(0.05)
SOUNDTRACK.play(-1)

#? Crea un archivo para la base de datos del ranking  
ranking.create(TITULO_BD)

while running:
    timers.clock.tick(FPS) #? FPS del juego
    lista_eventos = pygame.event.get() #? Lista de eventos que ocurren en la ventana
    CARRETERA.dibujar(ventana_principal)
    
    #? MENU PRINCIPAL 
    if menu_principal.actual == menu_principal.ventana["Inicio"]: 
        for evento in lista_eventos:                    
            if evento.type == pygame.KEYDOWN:
                ingreso = ingreso[:-1] if evento.key == K_BACKSPACE else ingreso + evento.unicode
                
            #? Si se hace click sobre los botones 
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_jugar.collidepoint(evento.pos):
                    menu_principal.actual = "Juego"
                    
                elif rect_ranking.collidepoint(evento.pos):
                    menu_principal.actual = "Ranking"
        
        #? LOS BOTONES DE JUGAR-RANKING-INPUT            
        texto_ingreso = crear.Texto(FUENTE, ingreso, rgb.GRIS_100, (62, 70))
        pygame.draw.rect(ventana_principal, rgb.GRIS_200, POS_INGRESO)
        pygame.draw.rect(ventana_principal, rgb.GRIS_100, POS_INGRESO, 4)
        
        rect_jugar = pygame.draw.rect(ventana_principal, rgb.GRIS_300, (CENTER_TEXT_X, 465, ANCHO_TEXTO, ALTO_TEXTO))
        rect_ranking = pygame.draw.rect(ventana_principal, rgb.AMARILLO, (CENTER_TEXT_X, 542, ANCHO_TEXTO, ALTO_TEXTO))

        texto_ingreso.renderizar(ventana_principal)
        texto_jugar.renderizar(ventana_principal)
        texto_ranking.renderizar(ventana_principal)    
        
    #? TABLA DE JUGADORES 
    elif menu_principal.actual == menu_principal.ventana["Ranking"]:
        
        ventana_principal.fill(rgb.GRIS_300)
        lista_ranking = ranking.select(TITULO_BD)
        
        y = 60
        for fila in lista_ranking:
            nombre = fila[1]
            puntuacion = fila[-1]
            ranking_text = crear.Texto(FUENTE, f"{nombre}: {puntuacion}", rgb.GRIS_100, (100, y))
            ranking_text.renderizar(ventana_principal)
            y += 40 #? Aumenta el espacio entre cada fila

        rect_home = pygame.draw.rect(ventana_principal, rgb.GRIS_200, (CENTER_TEXT_X, 465, ANCHO_TEXTO, ALTO_TEXTO))
        texto_home.renderizar(ventana_principal)      
        
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_home.collidepoint(evento.pos):
                    menu_principal.actual = "Inicio"

                
    #? COMIENZO DEL JUEGO 
    elif menu_principal.actual == menu_principal.ventana["Juego"]:
        texto_score = FUENTE.render(f"SCORE: {score}", True, rgb.GRIS_300, rgb.AMARILLO)
        
        #? El movimiento de los objetos en la pantalla 
        CARRETERA.actualizar(movimiento_fondo)
        ENEMY.avanzar(movimiento_obstaculo)
        MANCHA.avanzar(movimiento_fondo)   
        
        if game_over:
            #? Reinicia la posicion de los objetos
            ENEMY.mover(RANDOM, DESPLAZAMIENTO_X)
            MANCHA.mover(RANDOM, DESPLAZAMIENTO_X)
            PLAYER.rect.centerx = CENTER_X
            ENEMY.rect.y = -ENEMY.rect.height 
            game_over = False
            score = 0
            
        if PLAYER.colisionar(MANCHA):
            PLAYER.mover(RANDOM, DESPLAZAMIENTO_X) #? Mueve al jugador a una posicion aleatoria
        
        if PLAYER.colisionar(ENEMY):
            ranking.update(TITULO_BD, ingreso, score)
            explosion_animation(ventana_principal, (PLAYER.rect.x -30, PLAYER.rect.y))
            menu_principal.actual = "Inicio"
            game_over = True
            
        #? EVENTOS DEL JUEGO
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    PLAYER.mover(IZQUIERDA, DESPLAZAMIENTO_X)
                    
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    PLAYER.mover(DERECHA, DESPLAZAMIENTO_X)

            #? EVENTOS DE TIEMPO 
            if evento.type == timers.milis_50:
                score += 1
                
            if evento.type == timers.milis_random:
                ENEMY.mover(RANDOM, DESPLAZAMIENTO_X)
        
        MANCHA.dibujar(ventana_principal)                   
        ENEMY.dibujar(ventana_principal)
        PLAYER.dibujar(ventana_principal)
        ventana_principal.blit(texto_score, POS_SCORE)            
    #? Fin Del Menu 
    
    for evento in lista_eventos:        
        if evento.type == pygame.QUIT:
            running = not running
    pygame.display.flip() #? Efectuo todos los cambios de la pantalla 
pygame.quit()