
import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Spaceship:
    def __init__(self, DisplaySurf, spaceshipSpritePath, ScreenWidth, ScreenHeight):
        self.spaceship = pygame.image.load(spaceshipSpritePath)
        self.ScreenWidth = ScreenWidth
        self.ScreenHeight = ScreenHeight
        self.DisplaySurf = DisplaySurf
        self.pos = self.spaceship.get_rect()
        self.pos = self.pos.move(ScreenWidth/2 - self.pos.width/2, ScreenHeight/2 - self.pos.height/2)
        self.angle = 1

    def Move(self, font):

        if( pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
            self.pos = self.pos.move(3, 0)
        elif( pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
            self.pos = self.pos.move(-3, 0)
            #self.spaceship = pygame.transform.rotate(self.spaceship, self.angle)
        elif( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
            self.pos = self.pos.move(0, -3)
        elif( pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
            self.pos = self.pos.move(0, 3)

        text = unicode("(%s, %s)" % (self.pos.left + self.pos.width/2, self.pos.top + self.pos.height/2))
        ShipLabel = font.render(text, 2, WHITE)
        self.DisplaySurf.blit(ShipLabel, (self.pos.left + 60, self.pos.top - 20))
        self.DisplaySurf.blit(self.spaceship, self.pos)