# ------------------------------------------------------------------------------
# Gabriel A Paco >> @ https://github.com/eclipse-jro/
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, .=./ ........................................

import pygame
import random
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()

width = 640
height = width / 16 * 9 # 360
fps = 30
timer = pygame.time.Clock()
screen = pygame.display.set_mode((width, int(height)))
keys = [None]*275

font = pygame.font.Font('pixelFonts/slkscrb.ttf', 30)

paddleSpeed = 14
paddleMargin = 50
paddleWidth = 25
paddleHeight = 120

# Player paddles
paddleOne = {'x':paddleMargin, 'y':50, 'score': 0}
paddleTwo = {'x':width - (paddleWidth + paddleMargin), 'y':50, 'score': 0}

ballXSpeed = ballYSpeed = 18
ballDir = [-10, 10]
ball = {'x':random.randint(0, width), 'y':random.randint(0, height), 'radius': 12}

BLACK = (0,0,0)
WHITE = (255,255,255)

won = False

while True:
    scoreText = font.render(str(paddleOne['score'])+' - '+str(paddleTwo['score']), False, WHITE)
    scoreShadow = font.render(str(paddleOne['score'])+' - '+str(paddleTwo['score']), False, BLACK)
    screen.fill(BLACK)
    timer.tick(fps)

    pygame.draw.rect(screen, WHITE, (paddleOne['x'], paddleOne['y'], paddleWidth, paddleHeight)) # Paddle one
    pygame.draw.rect(screen, WHITE, (paddleTwo['x'], paddleTwo['y'], paddleWidth, paddleHeight)) # Paddle two
    pygame.draw.circle(screen, WHITE, (int(ball['x']), int(ball['y'])), ball['radius'])
    screen.blit(scoreShadow, ((width / 2)-45, 12))
    screen.blit(scoreText, ((width / 2)-50, 10))


    # Edge detection for ball
    if (ball['x'] - (ball['radius'] / 2)) <= 0:
        # reset the ball & p2 gets a point
        ball['x'] = width / 2
        ball['y'] = height / 2
        ballXSpeed = ballDir[random.randint(0, 1)]
        paddleTwo['score'] += 1
    elif ball['x'] + (ball['radius'] / 2) >= width:
        # reset the ball $ p1 gets a point
        ball['x'] = width / 2
        ball['y'] = height / 2
        ballXSpeeed = ballDir[random.randint(0, 1)]
        paddleOne['score'] += 1
    if (ball['y'] - (ball['radius'] / 2)) <= 0:
        ballYSpeed = 18
    elif (ball['y'] + (ball['radius'] / 2)) >= height:
        ballYSpeed = -18

    # Paddle detection
    if ball['x'] <= (paddleOne['x'] + paddleWidth) and (ball['y'] >= paddleOne['y'] and ball['y'] <= (paddleOne['y'] + paddleHeight)):
        ballXSpeed = 18
    if ball['x'] >= paddleTwo['x'] and ball['y'] >= paddleTwo['y'] and ball['y'] <= (paddleTwo['y'] + paddleHeight):
        ballXSpeed = -18

    if paddleOne['score'] == 5:
        winner = font.render('PLAYER ONE WINS', False, WHITE)
        again = font.render('PRESS SPACE TO PLAY AGAIN', False, WHITE)
        screen.blit(winner, ((width / 2)-160, ((height / 2)-50)))
        screen.blit(again, ((width / 2)-280, ((height / 2)+100)))
        ballXSpeed = 0
        ballYSpeed = 0
        won = True
    elif paddleTwo['score'] == 5:
        winner = font.render('PLAYER TWO WINS', False, WHITE)
        again = font.render('PRESS SPACE TO PLAY AGAIN', False, WHITE)
        screen.blit(winner, ((width / 2)-160, ((height / 2)-50)))
        screen.blit(again, ((width / 2)-280, ((height / 2)+100)))
        ballXSpeed = 0
        ballYSpeed = 0
        won = True

    if keys[K_SPACE]:
        won = False
        paddleOne['score'] = 0
        paddleTwo['score'] = 0
        ballXSpeed = ballDir[random.randint(0,1)]
        ballYSpeed = ballDir[random.randint(0,1)]

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

    # difficulty settings:
    # if keys[K_o]:
    #     difficulty += 1
    # elif keys[K_p] and difficulty >= 1:
    #     difficulty -+ 1

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
