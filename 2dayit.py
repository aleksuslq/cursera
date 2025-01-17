import random
import pygame

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

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)

player_rect = player.get_rect()
main_display.blit(player, player_rect)
#main_display.fill((COLOR_BLACK))

def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (15, 15)
    bonus = pygame.Surface(bonus_size)
    bonus.fill(COLOR_GREEN)
    bonus_x = random.randint(0, WIDTH - bonus_size[0]) 
    bonus_rect = pygame.Rect(bonus_x, 0, *bonus_size)  
    bonus_move = [0, random.randint(1, 6)]
    return [bonus, bonus_rect, bonus_move]


CREATE_ENEMY = pygame.USEREVENT +1
CREATE_BONUS = pygame.USEREVENT +2
pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 500)
enemies = []
bonuses = []

score = 0

player_move_down = [0, 1]
player_move_up = [0, -1]
player_move_right = [1, 0]
player_move_left = [-1, 0]
player_speed_right = [0, -1]

playing = True

while playing:
   
    FPS.tick(230)
    

    
  
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

          
    main_display.fill(COLOR_BLACK)
    
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
 
    main_display.blit(FONT.render(str(score),True, COLOR_WHITE), (WIDTH - 50, 20))
    main_display.blit(player, player_rect)
    
  #  main_display.blit(enemy, enemy_rect)

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

    
    