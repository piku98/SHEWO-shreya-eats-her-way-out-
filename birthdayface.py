import pygame
import os

class BirthdayFace:
    def __init__(self, gameWidth, gameHeight):
        self.GAME_WIDTH = gameWidth
        self.GAME_HEIGHT = gameHeight
        self.SIZE = 200
        self.X = gameWidth / 2 - self.SIZE / 2
        self.Y = gameHeight / 2 - self.SIZE / 2
        self.image = self.image = pygame.image.load(os.path.join("./resources/" + 'circle-cropped.png'))
    
    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (int(self.SIZE), int(self.SIZE)))
        screen.blit(self.image, (self.X, self.Y))