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
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My Game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(600, 300))

# rectangles for easier placement
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouse down')
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('player/mouse collision')

    # place surfaces on display surface - (0,0) = top left
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect.inflate(10, 10))
    screen.blit(score_surf, score_rect)

    # draw line that follows mouse
    # pygame.draw.line(screen, 'yellow', (0, 0), pygame.mouse.get_pos(), 10)

    # snail animations
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    # print(player_rect.left)   # check player rect position
    screen.blit(player_surf, player_rect)

    # collisions - returns bool
    if player_rect.colliderect(snail_rect):
        print('snail/player collision')

    # mouse position & collision point
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print('mouse/player collision')
    #     print(pygame.mouse.get_pressed())

    # draw & update all elements
    pygame.display.update()

    # set the max frame rate
    clock.tick(60)
