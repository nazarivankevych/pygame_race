# imports for game
import pygame
import random

pygame.init()

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
carImg = pygame.image.load('img/car.png')
carImg = pygame.transform.scale(carImg, (obj_width, obj_height))
# time for finish
count_time = 10
start_ticks = pygame.time.get_ticks()
# text and picture which we see after finishing
finish_text = 'You win this Crazy Racing GAME ;)'
obj_pic = pygame.image.load('img/finish_line.png')
finish_height = 80
finish_width = 540


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
        gameloop()


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


def reveal_finish(line_startx, line_starty):
    # create values for generated finish
    try:
        obs_pic = pygame.image.load('img/finish_line.png')
        obs_pic = pygame.transform.scale(obs_pic, (finish_width, finish_height))
        gameDisplay.blit(obs_pic, (line_startx, line_starty))
    except UnboundLocalError:
        gameloop()


def finish():
    largetext = pygame.font.Font('freesansbold.ttf', 40)
    textsurf, textrect = text_objects(finish_text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def gameloop():

    global obj_pic
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    obj_startx = random.randrange(165, (display_width-150))
    obj_starty = -750
    line_startx = 135
    line_starty = 10
    obj_speed = 7
    line_speed = 7
    object_width = 50
    object_height = 90
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
                    line_speed *= 2
                if event.key == pygame.K_LALT:
                    obj_speed /= 2
                    line_speed /= 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        x += x_change
        obstacle(obj_startx, obj_starty, obj)
        obj_starty += obj_speed
        car(x, y)

        # colissions with borders
        if x > (display_width - 155) - object_width or x < 108:
            crash()
        # generate cars in different places of road
        if obj_starty > display_height:
            obj_starty = 0 - object_height
            obj_startx = random.randrange(155, (display_width - 180))
            obj = random.randrange(0, 2)
        # colissions with another cars
        if y < obj_starty + object_height:
            if obj_startx < x < obj_startx + object_width or obj_startx < x + object_width < obj_startx + object_width:
                crash()
        # set timer for creating a finish line after short time
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > count_time:
            if line_starty < display_height:
                reveal_finish(line_startx, line_starty)
                line_starty += line_speed
                # Inform user about finishing
                if line_starty > y:
                    gameDisplay.blit(carImg, (x, y))
                    finish()

        pygame.display.update()
        game_clock.tick(60)


gameloop()
pygame.quit()
quit()
