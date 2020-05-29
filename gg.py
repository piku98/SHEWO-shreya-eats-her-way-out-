import pygame, os
import sys
from food import Food
from player import Player
from birthdayface import BirthdayFace
from happy import Happy
from birthday import Birthday
from confetti import Confetti
import random

BACKGROUND_COLOR = (255, 255, 255)
GAME_WIDTH, GAME_HEIGHT = 800, 600
FOOD_SIZE = 40
FOOD_MOTION_SPEED = 2
GAME_OVER = False

clock = pygame.time.Clock()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_WIDTH))

drawables = []

def detect_colision_and_remove(player, drawables, eat):
    if eat:
        for food in drawables:
            """ if ((food.X >= player.X and food.X < (player.X + player.SIZE)) or (player.X >= food.X and player.X < (food.X + food.SIZE))) or ((food.Y >= player.Y and food.Y < (player.Y + player.SIZE)) or (player.Y >= food.Y and player.Y < (food.Y + food.SIZE))):
                drawables.remove(food) """

            if (player.X >= food.X and player.X <= food.X + food.SIZE) or (player.Y >= food.Y and player.Y <= food.Y + food.SIZE):
                drawables.remove(food)


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

player = Player(GAME_WIDTH, GAME_HEIGHT)
PLAYER_STEP_SIZE = 50

PLAYER_MIDDLE_SCREEN_X = GAME_WIDTH / 2 - player.SIZE / 2
PLAYER_MIDDLE_SCREEN_Y = GAME_HEIGHT / 2 - player.SIZE / 2


birthdayFace = BirthdayFace(GAME_WIDTH, GAME_HEIGHT)

happy = Happy(GAME_HEIGHT, GAME_WIDTH, "happy.jpg")

birthday = Birthday(GAME_HEIGHT, GAME_WIDTH, "birthday.jpg")

confetti = []

PIZZA_CONFETTI_XS = [50, 100, 200, 220, 300, 320, 520, 750, 620]
for x in PIZZA_CONFETTI_XS:
    confetti.append(Confetti(x, 0, FOOD_SIZE, GAME_HEIGHT, GAME_WIDTH, random.randint(4, 20), "pizza.png"))

CHOCOLATE_CONFETTI_XS = [20, 60, 250, 300, 400, 420]
#for x in CHOCOLATE_CONFETTI_XS:
#    confetti.append(Confetti(x, 0, FOOD_SIZE, GAME_HEIGHT, GAME_WIDTH, random.randint(1, 5), "chocolate.png"))

ICECREAM_CONFETTI_XS = [10, 60, 150, 220, 370, 600, 620, 500, 580, 650, 700, 780]
for x in ICECREAM_CONFETTI_XS:
    confetti.append(Confetti(x, 0, FOOD_SIZE, GAME_HEIGHT, GAME_WIDTH, random.randint(3, 20), "ice_cream.png"))





while not GAME_OVER:
    eat = True
    player_steps_X, player_steps_Y = 0, 0
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                eat = True
            if event.key == pygame.K_LEFT:
                player_steps_X = -PLAYER_STEP_SIZE
            elif event.key == pygame.K_RIGHT:
                player_steps_X  = PLAYER_STEP_SIZE
            elif event.key == pygame.K_UP:
                player_steps_Y = -PLAYER_STEP_SIZE
            elif event.key == pygame.K_DOWN:
                player_steps_Y = PLAYER_STEP_SIZE
            detect_colision_and_remove(player, drawables, eat)

            
    if len(drawables) == 0:
        happy.draw(screen)
        birthday.draw(screen)
        for conf in confetti:
            conf.draw(screen)
        birthdayFace.draw(screen)
    else:
        player.draw(screen, player_steps_X, player_steps_Y)
        for i in range(len(drawables)):
            drawables[i].draw(screen)
    
    clock.tick(50)
    
    pygame.display.update()
    
    