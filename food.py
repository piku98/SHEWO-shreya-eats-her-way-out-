import pygame, os, random

class Food:
    def __init__(self, X, Y, size, gameHeight, gameWidth, moveFactor, imagename):
        self.GAME_WIDTH = gameWidth
        self.GAME_HEIGHT = gameHeight
        self.SIZE = size
        self.X = X
        self.Y = Y
        self.MOVE_FACTOR_X = moveFactor
        self.MOVE_FACTOR_Y = moveFactor
        self.image = pygame.image.load(os.path.join("./resources/" + imagename))
        self.image = pygame.transform.scale(self.image, (size, size))
    
    def draw(self, screen):
        if self.X <= 0 or self.X >= self.GAME_WIDTH - self.SIZE:
            self.MOVE_FACTOR_X = -self.MOVE_FACTOR_X
        if self.Y <= 0 or self.Y >= self.GAME_HEIGHT - self.SIZE:
            self.MOVE_FACTOR_Y = -self.MOVE_FACTOR_Y
        
        self.X += self.MOVE_FACTOR_X
        self.Y += self.MOVE_FACTOR_Y
        screen.blit(self.image, (self.X, self.Y))
