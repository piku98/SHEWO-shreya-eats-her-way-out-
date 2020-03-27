import pygame, os
import sys
from food import Food
import random

BACKGROUND_COLOR = (255, 255, 255)
GAME_WIDTH, GAME_HEIGHT = 800, 600
FOOD_SIZE = 40
FOOD_MOTION_SPEED = 5
GAME_OVER = False

clock = pygame.time.Clock()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_WIDTH))

drawables = []

def fill_drawables(X, Y, n, FOOD_MOTION_SPEED, name):
    for i in range(0, n):
        drawables.append(Food(X[i], Y[i], FOOD_SIZE, GAME_HEIGHT, GAME_WIDTH, FOOD_MOTION_SPEED, name))
        FOOD_MOTION_SPEED = -FOOD_MOTION_SPEED
    FOOD_MOTION_SPEED = abs(FOOD_MOTION_SPEED)



N_ICECREAMS = 5
ICREAM_X = [400, 10, 210, 500, 700]
ICREAM_Y = [20, 100, 300, 10, 200]
fill_drawables(ICREAM_X, ICREAM_Y, N_ICECREAMS, FOOD_MOTION_SPEED, "ice_cream.png")



N_PIZZAS = 3
PIZZA_X = [600, 300, 100]
PIZZA_Y = [120, 200, 400]
fill_drawables(PIZZA_X, PIZZA_Y, N_PIZZAS, FOOD_MOTION_SPEED, "pizza.png")


N_CHOCOLATES = 6
CHOCOLATE_X = [750, 650, 150, 350, 50, 630]
CHOCOLATE_Y = [60, 500, 300, 180, 65, 200]
fill_drawables(CHOCOLATE_X, CHOCOLATE_Y, N_CHOCOLATES, FOOD_MOTION_SPEED, "chocolate.png")





while not GAME_OVER:
    
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    for i in range(len(drawables)):
        drawables[i].draw(screen)
    clock.tick(40)
    
    pygame.display.update()
    
    