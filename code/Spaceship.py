
import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Spaceship:
    def __init__(self, DisplaySurf, spaceshipSpritePath, ScreenWidth, ScreenHeight):
        self.spaceship = pygame.sprite.Sprite()
        self.spaceship.image = pygame.image.load(spaceshipSpritePath)
        self.ScreenWidth = ScreenWidth
        self.ScreenHeight = ScreenHeight
        self.DisplaySurf = DisplaySurf
        self.pos = self.spaceship.image.get_rect()
        self.pos = self.pos.move(ScreenWidth/2 - self.pos.width/2, ScreenHeight/2 - self.pos.height/2)
        self.angle = 0

        self.spaceshipTransformed = self.spaceship

    def Move(self, font):

        if( pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
            self.pos = self.pos.move(3, 0)
        #    self.angle = self.angle - 1
        #    orig_rect = self.pos
        #    self.spaceshipTransformed.image = pygame.transform.rotate(self.spaceship.image, self.angle)
        #    self.pos = self.spaceshipTransformed.image.get_rect()
        #    self.pos.center = orig_rect.center
        elif( pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
            self.pos = self.pos.move(-3, 0)
        #    self.angle = self.angle + 1
        #    orig_rect = self.pos
        #    self.spaceshipTransformed.image = pygame.transform.rotate(self.spaceship.image, self.angle)
        #    self.pos = self.spaceshipTransformed.image.get_rect()
        #    self.pos.center = orig_rect.center
        elif( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
            self.pos = self.pos.move(0, -3)
        elif( pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
            self.pos = self.pos.move(0, 3)

        text = unicode("(%s, %s, %s)" % (self.pos.left + self.pos.width/2, self.pos.top + self.pos.height/2, self.angle))
        ShipLabel = font.render(text, 2, WHITE)
        self.DisplaySurf.blit(ShipLabel, (self.pos.left + 60, self.pos.top - 20))
        self.DisplaySurf.blit(self.spaceshipTransformed.image, self.pos)