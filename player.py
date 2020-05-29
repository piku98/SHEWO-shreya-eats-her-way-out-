import pygame
import sys, os

class Player:
    def __init__(self, gameWidth, gameHeight):
        self.GAME_WIDTH = gameWidth
        self.GAME_HEIGHT = gameHeight
        self.SIZE = 40
        self.X = gameWidth / 2 - self.SIZE / 2
        self.Y = gameHeight / 2 - self.SIZE / 2
        self.image = self.image = pygame.image.load(os.path.join("./resources/" + 'circle-cropped.png'))
    
    def draw(self, screen, move_X, move_Y):
        self.image = pygame.transform.scale(self.image, (int(self.SIZE), int(self.SIZE)))
        self.X = (self.X + move_X) % self.GAME_WIDTH
        self.Y = (self.Y + move_Y) % self.GAME_HEIGHT
        rect = self.image.get_rect()
        rect = rect.move((self.X, self.Y))
        screen.blit(self.image, rect)