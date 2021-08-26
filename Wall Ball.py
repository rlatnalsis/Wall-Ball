# Unit PYG02: Pygame Wall Ball Game --version 3
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
fps = 300 # frames per second
fclock = pygame.time.Clock()

# Event
while True: # ball moves one step per cycle, so control cycle interval to control speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
                # if paragraph: cannot subract 0 offset # else paragraph: abs(distance - 1) * (maintain direction)
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1 # all: (distrance + 1) cause addition cannot produce 0 offset
                # if paragraph: maintain direction # else paragraph: chagne direction
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))

    ballrect = ballrect.move(speed) # 'speed' is the rate for two tuples, so this function consists of two tuples, speed[0] and speed[1]
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

# Read-only
    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)