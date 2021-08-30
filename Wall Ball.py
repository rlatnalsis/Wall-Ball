# Unit PYG05: Pygame Wall Ball Game --version 8
import pygame, sys
import pygame.freetype

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wall Ball Game")
pos = [230, 160]
speed = [1, 1]
GOLD = 255, 215, 0
BLACK = 0, 0, 0
f1 = pygame.freetype.Font("C:\Windows\Fonts\Gabriola.ttf", 36)
f1rect = f1.render_to(screen, pos, "draw font", fgcolor=GOLD, size=50)
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] = - speed[0]
    if pos[1] < 0 or pos[1] + f1rect.height > height:
        speed[1] = - speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]
    
    screen.fill(BLACK)
    f1rect = f1.render_to(screen, pos, "draw font", fgcolor=GOLD, size=50)
    pygame.display.update()
    fclock.tick(fps)