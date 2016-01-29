import pygame, sys
import Spaceship

from Spaceship import *

from pygame.locals import *


pygame.init()
pygame.font.init()
font = pygame.font.SysFont("monospace", 12)

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

DisplayWidth = 800
DisplayHeight = 600
screen = pygame.display.set_mode((DisplayWidth, DisplayHeight), 0, 32)
pygame.display.set_caption('Asteroid Test')



pygame.key.set_repeat(10, 10)

#BGIMAGE = pygame.image.load('flippybackground.png')
spaceshipSpritePath = 'spaceship.png'
Ship = Spaceship(screen, spaceshipSpritePath, DisplayWidth, DisplayHeight)

bContinue = True

while bContinue:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            bContinue = False
        else:

            screen.fill(BLACK)
            Ship.Move(font)


            pygame.display.flip()
            fpsClock.tick(FPS)


pygame.quit()
sys.exit()



