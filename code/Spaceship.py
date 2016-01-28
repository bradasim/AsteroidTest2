
import pygame, sys
from pygame.locals import *

class Spaceship:
    def __init__(self, DisplaySurf, spaceshipSpritePath, ScreenWidth, ScreenHeight):
        self.spaceship = pygame.image.load(spaceshipSpritePath)
        self.ScreenWidth = ScreenWidth
        self.ScreenHeight = ScreenHeight
        self.DisplaySurf = DisplaySurf
        self.Rect = self.spaceship.get_rect()

    def Move(self):

        if( pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
            self.Rect = self.Rect.move(3, 0)
        elif( pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
            self.Rect = self.Rect.move(-3, 0)
        elif( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
            self.Rect = self.Rect.move(0, -3)
        elif( pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
            self.Rect = self.Rect.move(0, 3)

        self.DisplaySurf.blit(self.spaceship, self.Rect)