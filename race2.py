# imports for game
import pygame
import random

pygame.init()

display_width = 800
display_height = 800
car_width = 10
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# Set a width and height of screen
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Set a background
background = pygame.image.load('img/background.png')
# Name of app
pygame.display.set_caption('Crazy Racing')
# FPS of screen
clock = pygame.time.Clock()
# Sprite for car
carImg = pygame.image.load('img/car.jpeg')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load('img/tree.jpeg')
    elif obs == 1:
        obs_pic = pygame.image.load('img/ball.png')
    gameDisplay.blit(obs_pic, (obs_startx, obs_starty))


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

    obs_startx = random.randrange(200, (display_width-200))
    obs_starty = -750
    obs_speed = 7
    obs_width = 80
    obs_height = 80
    obs = random.randrange(0,2)

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            # if event.type == pygame.K_SPACE:

        # rgb = RED, GREEN, BLUE
        gameDisplay.fill((0, 0, 0))
        # background image set up
        gameDisplay.blit(background, (0, 0))

        x += x_change
        gameDisplay.fill(white)

        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obs_speed
        car(x,y)
        if x > display_width - car_width or x < 0:
            crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(150, (display_width -150))
            obs = random.randrange(0,2)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width: 
                crash()
            
        pygame.display.update()
        clock.tick(60)


gameloop()
pygame.quit()
quit()
