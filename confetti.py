import pygame
import os
import math

class Confetti:
    def __init__(self, X, Y, size, gameHeight, gameWidth, moveFactor, imagename):
        self.GAME_WIDTH = gameWidth
        self.GAME_HEIGHT = gameHeight
        self.SIZE = size
        self.X = X
        self.Y = Y
        self.MOVE_FACTOR_Y = moveFactor
        self.image = pygame.image.load(os.path.join("./resources/" + imagename))
        self.image = pygame.transform.scale(self.image, (self.SIZE, self.SIZE))
    
    def draw(self, screen):    
        self.Y = (self.Y + self.MOVE_FACTOR_Y) % self.GAME_HEIGHT
        self.image = pygame.transform.rotate(self.image, 90)
        screen.blit(self.image, (self.X, self.Y))
