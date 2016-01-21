import pygame, sys
import Spaceship

from pygame.locals import *


pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

DisplayWidth = 800
DisplayHeight = 600
DISPLAYSURF = pygame.display.set_mode((DisplayWidth, DisplayHeight), 0, 32)
pygame.display.set_caption('Asteroid Test')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#BGIMAGE = pygame.image.load('flippybackground.png')
spaceshipSpritePath = 'spaceship.png'
Ship = Spaceship.Spaceship(DISPLAYSURF, spaceshipSpritePath, DisplayWidth, DisplayHeight)

bContinue = True

while bContinue:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            bContinue = False
        else:

            Ship.Move(DisplayWidth/2, DisplayHeight/2)

            pygame.display.update()
            fpsClock.tick(FPS)


pygame.quit()
sys.exit()



