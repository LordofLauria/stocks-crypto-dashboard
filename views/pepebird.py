import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
GRAVITY = 0.5
JUMP_STRENGTH = -5
PIPE_WIDTH = 70
PIPE_GAP = 250
PIPE_SPEED = 4

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pepe Bird")
clock = pygame.time.Clock()

# Load bird image
bird_img = pygame.image.load("pepebatman.png")  # Ensure bird.png is in the same folder
bird_img = pygame.transform.scale(bird_img, (100, 80))  # Resize bird

# Bird properties
bird_x = 100
bird_y = HEIGHT // 5
bird_velocity = 0

# Pipes
pipes = []


def create_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.Rect(WIDTH, 0, PIPE_WIDTH, height)
    bottom_pipe = pygame.Rect(WIDTH, height + PIPE_GAP, PIPE_WIDTH, HEIGHT - height - PIPE_GAP)
    pipes.append((top_pipe, bottom_pipe))


# Game loop
running = True
score = 0
frames = 0
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = JUMP_STRENGTH

    # Bird movement
    bird_velocity += GRAVITY
    bird_y += bird_velocity
    bird_rect = bird_img.get_rect(topleft=(bird_x, bird_y))
    screen.blit(bird_img, (bird_x, bird_y))  # Draw bird image

    # Pipe movement
    if frames % 90 == 0:
        create_pipe()

    for pipe in pipes:
        pipe[0].x -= PIPE_SPEED
        pipe[1].x -= PIPE_SPEED
        pygame.draw.rect(screen, GREEN, pipe[0])
        pygame.draw.rect(screen, GREEN, pipe[1])

        # Collision detection
        if bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1]) or bird_y <= 0 or bird_y >= HEIGHT:
            running = False

        # Scoring
        if pipe[0].x == bird_x:
            score += 1

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe[0].x > -PIPE_WIDTH]

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)
    frames += 1

pygame.quit()
