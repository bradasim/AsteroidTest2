
import pygame, sys
from pygame.locals import *

class Spaceship:
    def __init__(self, DisplaySurf, spaceshipSpritePath, ScreenWidth, ScreenHeight):
        self.spaceship = pygame.image.load(spaceshipSpritePath)
        self.ScreenWidth = ScreenWidth
        self.ScreenHeight = ScreenHeight
        self.DisplaySurf = DisplaySurf

    def Move(self, x, y):
        if (x>0 and x<self.ScreenWidth):
            self.DisplaySurf.blit(self.spaceship, (x, y))