# imports for game
import pygame
import random
from timer_finish import timer

pygame.init()
# create a key pressed
key_input = pygame.key.get_pressed()
# set up dimensions
display_width = 800
display_height = 800
obj_width = 100
obj_height = 100
# RGB colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# Set a width and height of screen
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Set a background
background = pygame.image.load('img/background.png')
background = pygame.transform.scale(background, (display_width, display_height))
# Name of app
pygame.display.set_caption('Crazy Racing')
# FPS of screen
clock = pygame.time.Clock()
# Sprite for car
carImg = pygame.image.load('img/car.jpeg')
carImg = pygame.transform.scale(carImg, (obj_width, obj_height))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def obstacle(obs_startx, obs_starty, obs):
    global obj_pic
    # background image set up
    gameDisplay.blit(background, (0, 0))
    if obs == 0:
        obj_pic = pygame.image.load('img/car2.png')
        obj_pic = pygame.transform.scale(obj_pic, (obj_width-35, obj_height+10))
    elif obs == 1:
        obj_pic = pygame.image.load('img/car3.png')
        obj_pic = pygame.transform.scale(obj_pic, (obj_width-35, obj_height+10))
    gameDisplay.blit(obj_pic, (obs_startx, obs_starty))


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf',115)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textsurf, textrect)

    pygame.display.update()


def crash():
    message_display('You Crashed')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def gameloop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    obj_startx = random.randrange(200, (display_width-200))
    obj_starty = -750
    obj_speed = 7
    obj_width = 80
    obj_height = 80
    obj = random.randrange(0, 2)

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Events for keybords Up, Right, Left, SPACE, Left ALT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_SPACE:
                    obj_speed *= 2
                if event.key == pygame.K_LALT:
                    obj_speed /= 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        obstacle(obj_startx, obj_starty, obj)
        obj_starty += obj_speed
        car(x, y)
        if x > display_width - obj_width or x < 0:
            crash()
        if obj_starty > display_height:
            obj_starty = 0 - obj_height
            obj_startx = random.randrange(150, (display_width - 150))
            obj = random.randrange(0, 2)

        if y < obj_starty + obj_height:
            if obj_startx < x < obj_startx + obj_width or obj_startx < x + obj_width < obj_startx + obj_width:
                crash()
            
        pygame.display.update()
        clock.tick(60)


gameloop()
pygame.quit()
quit()
