# Unit PYG05: Pygame Wall Ball Game_draw more shapes
import pygame, sys
from math import pi

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Wall Ball Game")
GOLD = 255, 215, 0
RED = pygame.Color('red')
WHITE = 255, 255, 255
GREEN = pygame.Color('green')

e1rect = pygame.draw.ellipse(screen, GREEN, (50, 50, 500, 300), 3)
c1rect = pygame.draw.circle(screen, GOLD, (200, 180), 30, 5)
c2rect = pygame.draw.circle(screen, GOLD, (400, 180), 30)
r1rect = pygame.draw.rect(screen, RED, (170, 130, 60, 10), 3)
r2rect = pygame.draw.rect(screen, RED, (370, 130, 60, 10))
plist = [(295, 170), (285, 250), (260, 280), (340, 280), (315, 250), (305, 170)]
# l1rect = pygame.draw.lines(screen, GOLD, True, plist, 2)
al1rect = pygame.draw.aalines(screen, GOLD, True, plist, 2)
alrect = pygame.draw.arc(screen, RED, (200, 220, 200, 100), 1.4 * pi, 1.9 * pi, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()