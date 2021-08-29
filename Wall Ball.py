# Unit PYG05: Pygame Wall Ball Game --version 7
import pygame, sys

def RGBChannel(a):
    return 0 if a < 0 else (255 if a > 255 else int(a))

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
bgcolor = pygame.Color("black")
BLACK = 0, 0, 0

pygame.display.set_caption("Wall Ball Game")
icon = pygame.image.load("Wall-Ball\PYG03_flower.png")
pygame.display.set_icon(icon)

ball = pygame.image.load("Wall-Ball\PYG02_ball.gif")
ballrect = ball.get_rect()
speed = [1, 1]
fclock = pygame.time.Clock()
fps = 300
still = False

while True:
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

        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)

    if pygame.display.get_active() and not still:
        ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = - speed[1]

    bgcolor.r = RGBChannel(ballrect.left * 255 / width)
    bgcolor.g = RGBChannel(ballrect.top * 255 / height)
    bgcolor.b = RGBChannel(min(speed[0], speed[1]) * 255 / max(speed[0], speed[1], 1))

    pygame.display.update()
    screen.fill(bgcolor)
    screen.blit(ball, ballrect)
    fclock.tick(fps)