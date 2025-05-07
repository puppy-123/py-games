import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Clone")

# Bird settings
bird_y = HEIGHT // 2
bird_vel = 0
gravity = 0.5
jump_strength = -10

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill((135, 206, 250))  # Sky blue background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = jump_strength

    # Apply gravity
    bird_vel += gravity
    bird_y += bird_vel

    # Draw bird
    pygame.draw.rect(screen, (255, 255, 0), (50, bird_y, 30, 30))  # Yellow square as bird

    pygame.display.flip()

pygame.quit()
sys.exit()
