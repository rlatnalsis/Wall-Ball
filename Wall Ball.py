# Unit PYG02: Pygame Wall Ball Game --version 1
import pygame, sys

# Global Function & Vairable
pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wall Ball Game")
ball = pygame.image.load("Pygame\PYG02_ball.gif")
speed = [1, 1] # tuple[horizontal axis ratio, vertical axis ratio]
BLACK = 0, 0, 0
ballrect = ball.get_rect()

# Event
while True: # ball moves one step per cycle, so control cycle interval to control speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed) # 'speed' is the rate for two tuples, so this function consists of two tuples, speed[0] and speed[1]
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

# Read-only
    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.update()