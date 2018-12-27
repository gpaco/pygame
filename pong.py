# ------------------------------------------------------------------------------
# J.Rene Ortega Jr. >> @ https://github.com/eclipse-jro/
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, .=./ ........................................

# Source: https://youtu.be/gykTkxzku3Y

import pygame
import random
import sys
from pygame.locals import *

pygame.init()

width = 640
height = width / 16 * 9 # 360
fps = 30
timer = pygame.time.Clock()
screen = pygame.display.set_mode((width, int(height)))
keys = [None]*275

paddleSpeed = 9
paddleMargin = 50
paddleWidth = 25
paddleHeight = 120

# Player paddles
paddleOne = {'x':paddleMargin, 'y':50}
paddleTwo = {'x':width - (paddleWidth + paddleMargin), 'y':50}

ballXSpeed = ballYSpeed = 5
ball = {'x':random.randint(0, width), 'y':random.randint(0, height), 'radius': 16}

BLACK = (0,0,0)
WHITE = (255,255,255)

while True:
    screen.fill(BLACK)
    timer.tick(fps)

    pygame.draw.rect(screen, WHITE, (paddleOne['x'], paddleOne['y'], paddleWidth, paddleHeight)) # Paddle one
    pygame.draw.rect(screen, WHITE, (paddleTwo['x'], paddleTwo['y'], paddleWidth, paddleHeight)) # Paddle two
    pygame.draw.circle(screen, WHITE, (ball['x'], ball['y']), ball['radius'])

    if (ball['x'] - (ball['radius'] / 2)) <= 0:
        ballXSpeed = 5
    elif ball['x'] + (ball['radius'] / 2) >= width:
        ballXSpeed = -5
    if (ball['y'] - (ball['radius'] / 2)) <= 0:
        ballYSpeed = 5
    elif (ball['y'] + (ball['radius'] / 2)) >= height:
        ballYSpeed = -5

    ball['x'] += ballXSpeed
    ball['y'] += ballYSpeed

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit(0)
        elif event.type == KEYDOWN:
            keys[event.key] = True
        elif event.type == KEYUP:
            keys[event.key] = False

    # Player controls
    # Player one
    if keys[K_w] and paddleOne['y'] > 0:
        paddleOne['y'] -= paddleSpeed
    elif keys[K_s] and (paddleOne['y'] + paddleHeight) < height:
        paddleOne['y'] += paddleSpeed

    # Player two
    if keys[K_UP] and paddleTwo['y'] > 0:
        paddleTwo['y'] -= paddleSpeed
    elif keys[K_DOWN] and (paddleTwo['y'] + paddleHeight) < height:
        paddleTwo['y'] += paddleSpeed

    # End player controls

    pygame.display.update()
