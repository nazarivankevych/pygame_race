# imports for game
import pygame
import random

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
game_clock = pygame.time.Clock()
# Sprite for car
carImg = pygame.image.load('img/car.jpeg')
carImg = pygame.transform.scale(carImg, (obj_width, obj_height))
# time for finish
count_time = 5
start_ticks = pygame.time.get_ticks()


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def obstacle(obj_startx, obj_starty, obj):
    # background image set up
    gameDisplay.blit(background, (0, 0))
    # create values for generated objects
    try:
        if obj == 0:
            obs_pic = pygame.image.load('img/car2.png')
            obs_pic = pygame.transform.scale(obs_pic, (obj_width-35, obj_height+10))
        elif obj == 1:
            obs_pic = pygame.image.load('img/car3.png')
            obs_pic = pygame.transform.scale(obs_pic, (obj_width-35, obj_height+10))
        gameDisplay.blit(obs_pic, (obj_startx, obj_starty))
    except UnboundLocalError:
        pass


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 115)
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


def finish():
    message_display('You win this Crazy Racing GAME ;)')
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
    object_width = 80
    object_height = 80
    obj = random.randrange(0, 3)

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

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        x += x_change
        gameDisplay.fill(white)

        obstacle(obj_startx, obj_starty, obj)
        obj_starty += obj_speed
        car(x, y)

        if x > display_width - object_width or x < 0:
            crash()

        if obj_starty > display_height:
            obj_starty = 0 - object_height
            obj_startx = random.randrange(150, (display_width - 150))
            obj = random.randrange(0, 2)

        if y < obj_starty + object_height:
            if obj_startx < x < obj_startx + object_width or obj_startx < x + object_width < obj_startx + object_width:
                crash()
            else:
                finish()

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > 5:
            obj_pic = pygame.image.load('img/finish_line.png')
            obj_pic = pygame.transform.scale(obj_pic, (550, 80))
            finish_line = obj_starty - 300
            gameDisplay.blit(obj_pic, (128, finish_line))
            print(seconds)

        pygame.display.update()
        game_clock.tick(60)


gameloop()
pygame.quit()
quit()
