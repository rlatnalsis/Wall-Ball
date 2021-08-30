# Unit PYG05: Pygame Wall Ball Game_draw shape
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Wall Ball Game")
GOLD = 255, 215, 0
RED = pygame.Color('red')

r1rect = pygame.draw.rect(screen, GOLD, (100, 100, 200, 100), 5)
r2rect = pygame.draw.rect(screen, RED, (210, 210, 200, 100), 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()