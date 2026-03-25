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

# 🔥 Screen shake variables
shake_intensity = 0
shake_duration = 0

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

    # Collision
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        shake_intensity = 10
        shake_duration = 20
        game_over = True

    # 💥 Near-miss shake
    distance = abs(player_pos[0] - enemy_pos[0]) + abs(player_pos[1] - enemy_pos[1])
    if distance < 120 and not player_rect.colliderect(enemy_rect):
        shake_intensity = 3
        shake_duration = 5

    # 🎥 Apply shake
    if shake_duration > 0:
        shake_x = random.randint(-int(shake_intensity), int(shake_intensity))
        shake_y = random.randint(-int(shake_intensity), int(shake_intensity))
        shake_duration -= 1
        shake_intensity = max(0, shake_intensity - 0.5)  # smooth fade
    else:
        shake_x = 0
        shake_y = 0

    # Drawing
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, RED, (enemy_pos[0] + shake_x, enemy_pos[1] + shake_y, enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0] + shake_x, player_pos[1] + shake_y, player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()