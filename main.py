import pygame
from sys import exit

pygame.init()

# create display surface, the user window
screen = pygame.display.set_mode((800, 400))

# set game window title
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# colored test surface
# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

# image surface
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black')

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # place surfaces on display surface - (0,0) = top left
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (330, 50))

    # draw & update all elements
    pygame.display.update()

    # set the max frame rate
    clock.tick(60)
