import pygame
import os

class Birthday:
    def __init__(self, gameHeight, gameWidth, imagename):
        self.GAME_WIDTH = gameWidth
        self.GAME_HEIGHT = gameHeight
        self.SIZE = 300
        self.X = (gameWidth / 2 - self.SIZE / 2) - 5
        self.Y = gameHeight - 2
        self.image = pygame.image.load(os.path.join("./resources/" + imagename))
        self.image = pygame.transform.scale(self.image, (self.SIZE, self.SIZE))

    def draw(self, screen):
        if self.Y >= (self.GAME_HEIGHT / 2 + 30):
            self.Y -= 5
        screen.blit(self.image, (self.X, self.Y))