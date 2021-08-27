# Unit PYG03: Pygame Wall Ball Game --version 5
import pygame, sys

# Global Function & Vairable
pygame.init()
# vInfo = pygame.display.Info() # for FULLSCREEN mode
size = width, height = 600, 400 # = vInfo.current_w, vInfo.current_h # for FULLSCREEN mode
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
BLACK = 0, 0, 0

pygame.display.set_caption("Wall Ball Game")
icon = pygame.image.load("Pygame\PYG03_flower.png")
pygame.display.set_icon(icon)

ball = pygame.image.load("Pygame\PYG02_ball.gif")
ballrect = ball.get_rect()
speed = [1, 1]
fclock = pygame.time.Clock()
fps = 300

# Event
while True: # ball moves one step per cycle, so control cycle interval to control speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))

            elif event.key == pygame.K_ESCAPE:
                sys.exit()
            
        elif event.type == pygame.VIDEORESIZE: # for RESIZABLE mode
            size = width, height = event.size[0], event.size[1]

    if pygame.display.get_active():
        ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

# Read-only
    pygame.display.update()
    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    fclock.tick(fps)