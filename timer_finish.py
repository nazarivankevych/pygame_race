import pygame

pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()
# Variables for timer
TIME = 5
TEXT = "You finish the game"
# make a font and connect set_timer
counter, text = TIME, str(TIME).rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30, bold=True)


# main function
def timer():
    global counter, text
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else TEXT
            if e.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)


# timer()