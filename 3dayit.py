import random
import pygame
import os

from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
pygame.init()


FPS = pygame.time.Clock()



HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load("bg.png"),(WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

IMAGE_PATH ='G'
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player_size = (20, 20)
player = pygame.image.load("g2.png").convert_alpha()#pygame.Surface(player_size)
#player.fill(COLOR_BLACK)

player_rect = player.get_rect()
main_display.blit(player, player_rect)
#main_display.fill((COLOR_BLACK))

def create_enemy():
    enemy_size = (10, 10)
    enemy = pygame.image.load("enem.png").convert_alpha()#pygame.Surface(enemy_size)
 #   enemy.fill(COLOR_BLUE)
    #enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT-enemy.get_height() ), *enemy_size)
    enemy_x = random.randint(0, HEIGHT - enemy_size[0]) 
    enemy_rect = pygame.Rect(enemy_x, 0, *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    main_display.blit(enemy, enemy_rect)
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (15, 15)
    bonus = pygame.image.load("bon.png").convert_alpha()#pygame.Surface(bonus_size)
   # bonus.fill(COLOR_GREEN)
    bonus_x = random.randint(0, WIDTH - bonus_size[0]) 
    bonus_rect = pygame.Rect(bonus_x, 0, *bonus_size)  
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]


CREATE_ENEMY = pygame.USEREVENT +1
CREATE_BONUS = pygame.USEREVENT +2
pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 500)


CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []
bonuses = []

score = 0

image_index = 0

player_move_down = [0, 4]
player_move_up = [0, -4]
player_move_right = [4, 0]
player_move_left = [-4, 0]
player_speed_right = [0, -4]

playing = True

while playing:
   
    FPS.tick(120)
    

    
  
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())


        if event.type == CHANGE_IMAGE :
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    bg_X1 -= bg_move
    bg_X2 -= bg_move
          

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()
   # main_display.fill(COLOR_BLACK)
    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up) 

    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)



   # enemy_rect = enemy_rect.move(enemy_move)
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])   
        main_display.blit(enemy[0], enemy[1])     

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])   
        main_display.blit(bonus[0], bonus[1])
 
    main_display.blit(FONT.render(str(score),True, COLOR_BLACK), (WIDTH - 50, 20))
    main_display.blit(player, player_rect)
    
    

#    player_rect = player_rect.move(player_speed)
    print(len(enemies))
    print(len(bonuses))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if player_rect.colliderect(enemy[1]):
            
            playing = False

    for bonus in bonuses:
        if bonus[1].bottom == 0:
            bonuses.pop(bonuses.index(bonus))

        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))

    
    