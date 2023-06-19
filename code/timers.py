import pygame
import random

pygame.init()

#? Timmers 
clock = pygame.time.Clock()

#? Timer de ususario 
milis_50 = pygame.USEREVENT + 1
pygame.time.set_timer(milis_50, 10)

milis_random = pygame.USEREVENT + 2
pygame.time.set_timer(milis_random, random.randint(2, 5) * 1000) #? 2 a 5 segundos
