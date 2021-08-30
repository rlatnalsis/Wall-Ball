# Unit PYG05: Pygame Wall Ball Game_draw font as a surface
import pygame, sys
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Wall Ball Game")
GOLD = 255, 215, 0

f1 = pygame.freetype.Font('C:\Windows\Fonts\Gabriola.ttf', 36)
f1surf, f1rect = f1.render("draw font", fgcolor=GOLD, size=50)
f1rect = f1.render_to(screen, (200, 100), "draw font", fgcolor=GOLD, size=50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(f1surf, (200, 160))
    pygame.display.update()