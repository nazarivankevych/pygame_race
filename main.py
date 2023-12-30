import random
import pygame

pygame.init()

# set up dimensions
DISPLAY_WIDTH = 800
DISPLAY_HEIGTH = 800
OBJ_WIDTH = 100
OBJ_HEIGTH = 100
# RGB colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# Set a width and height of screen
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGTH))
# Set a background
background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background, (DISPLAY_WIDTH, DISPLAY_HEIGTH))
# Name of app
pygame.display.set_caption("Crazy Racing")
# FPS of screen
game_clock = pygame.time.Clock()
# Sprite for car
carImg = pygame.image.load("img/car.png")
carImg = pygame.transform.scale(carImg, (OBJ_WIDTH, OBJ_HEIGTH))
# time for finish
COUNT_TIME = 10
start_ticks = pygame.time.get_ticks()
# text and picture which we see after finishing
FINISH_TEXT = "You win this Crazy Racing GAME ;)"
obj_pic = pygame.image.load("img/finish_line.png")
FINISH_HEIGTH = 80
FINISH_WIDTH = 540


# set a car on the ground
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


# configure an obstacles for the car
def obstacle(obj_startx, obj_starty, obj):
    # background image set up
    gameDisplay.blit(background, (0, 0))
    # create values for generated objects
    try:
        if obj == 0:
            obs_pic = pygame.image.load("img/car2.png")
            obs_pic = pygame.transform.scale(obs_pic, (OBJ_WIDTH - 35, OBJ_HEIGTH + 10))
        elif obj == 1:
            obs_pic = pygame.image.load("img/car3.png")
            obs_pic = pygame.transform.scale(obs_pic, (OBJ_WIDTH - 35, OBJ_HEIGTH + 10))
        gameDisplay.blit(obs_pic, (obj_startx, obj_starty))
    except UnboundLocalError:
        gameloop()


# render objects on the ground
def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


# set a message acording to the situation with player
def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 115)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGTH / 2))
    gameDisplay.blit(textsurf, textrect)

    pygame.display.update()


# set a message after crashing from objects
def crash():
    message_display("You Crashed")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


# after some time reveal a finish line for winning
def reveal_finish(line_startx, line_starty):
    # create values for generated finish
    try:
        obs_pic = pygame.image.load("img/finish_line.png")
        obs_pic = pygame.transform.scale(obs_pic, (FINISH_WIDTH,FINISH_HEIGTH))
        gameDisplay.blit(obs_pic, (line_startx, line_starty))
    except UnboundLocalError:
        gameloop()


# set a text message for winning
def finish():
    largetext = pygame.font.Font("freesansbold.ttf", 40)
    textsurf, textrect = text_objects(FINISH_TEXT, largetext)
    textrect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGTH / 2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


# running whole game with cars and abstacles parameters for the player
def gameloop():

    global obj_pic
    x = DISPLAY_WIDTH * 0.45
    y = DISPLAY_HEIGTH * 0.8

    x_change = 0

    obj_startx = random.randrange(165, (DISPLAY_WIDTH - 150))
    obj_starty = -750
    line_startx = 135
    line_starty = 10
    obj_speed = 7
    line_speed = 7
    object_width = 50
    object_height = 90
    obj = random.randrange(0, 2)

    game_exit = False

    while not game_exit:
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
        if x > (DISPLAY_WIDTH - 155) - object_width or x < 108:
            crash()
        # generate cars in different places of road
        if obj_starty > DISPLAY_HEIGTH:
            obj_starty = 0 - object_height
            obj_startx = random.randrange(155, (DISPLAY_WIDTH - 180))
            obj = random.randrange(0, 2)
        # colissions with another cars
        if y < obj_starty + object_height:
            if (
                obj_startx < x < obj_startx + object_width
                or obj_startx < x + object_width < obj_startx + object_width
            ):
                crash()
        # set timer for creating a finish line after short time
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > COUNT_TIME:
            if line_starty < DISPLAY_HEIGTH:
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
