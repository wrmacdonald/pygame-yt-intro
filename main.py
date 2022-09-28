import pygame
from sys import exit
from random import randint


def display_score():
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:                     # draw fly or snail
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    """
    Check for collisions between player & any obstacles
    :param player:
    :type player:
    :param obstacles:
    :type obstacles:
    :return:
    :rtype:
    """
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


pygame.init()

screen = pygame.display.set_mode((800, 400))                    # display surface - the user window
pygame.display.set_caption('Runner')                            # set game window title

clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# game state
game_active = False
start_time = 0
score = 0

# Surfaces & rectangles for easier placement
# test_surface = pygame.Surface((100, 200))                     # colored test surface
# test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('My Game', False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(400, 50))

# Enemy Obstacles
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
obstacle_rect_list = []

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_gravity = 0
player_rect = player_surf.get_rect(midbottom=(80, 300))

# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', True, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# Game runner
while True:
    # Event Loop - general dealing with inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:                # Mouse Click on Player -> Player Jump
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:                        # Space Bar -> Player Jump
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:   # Space Bar -> Player Jump
                game_active = True
                start_time = pygame.time.get_ticks() // 1000
        if game_active and event.type == obstacle_timer:
            if randint(0, 2):                                       # randomly add snail or fly enemy
                obstacle_rect_list.append(snail_surf.get_rect(bottomleft=(randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomleft=(randint(900, 1100), 210)))

    if game_active:
        # Place surfaces on display surface - (0,0) = top left
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect.inflate(10, 10))
        # screen.blit(score_surf, score_rect)

        # draw line that follows mouse
        # pygame.draw.line(screen, 'yellow', (0, 0), pygame.mouse.get_pos(), 10)

        # Snail
        # snail_rect.x -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surf, snail_rect)

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Player
        # print(player_rect.left)   # check player rect position
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # keyboard inputs - other way, better for working with classes
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('Jump')

        # Collision
        game_active = collisions(player_rect, obstacle_rect_list)
        # if player_rect.colliderect(snail_rect):
        #     game_active = False

    else:                                                           # game not active
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # mouse position & collision point
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print('mouse/player collision')
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()                                     # Draw & update all elements
    clock.tick(60)                                              # set the max frame rate
