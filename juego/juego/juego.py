import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 5  
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 5  

    # Enemy movement
    enemy_pos[1] += enemy_speed

    if enemy_pos[1] > HEIGHT:
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
        score += 1
        print(f"Score: {score}")

    # ✅ Collision (NOW INSIDE LOOP)
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        game_over = True

    # ✅ Drawing (ALWAYS RUNS)
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()