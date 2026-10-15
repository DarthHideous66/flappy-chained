import pygame
from player import Player
import random
import math

from pipe import Pipe

pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
MAX_DISTANCE = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# Clock for controlling FPS
clock = pygame.time.Clock()

player = Player(375, 275)
player2 = Player(300, 275)
pipe = Pipe(350, random.randint(30, 550))

# Main game loop
running = True
while running:
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    player.handle_inputs(events, pygame.K_a, pygame.K_d, pygame.K_w) 
    player.update(pipe)
    player2.handle_inputs(events, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP) 
    player2.update(pipe)
    pipe.update()


    distance = math.hypot(
    player.rect.centerx - player2.rect.centerx,
    player.rect.centery - player2.rect.centery
    )

        

    if distance > MAX_DISTANCE:
        # Direction from player 1 to player 2
        dx = player2.rect.centerx - player.rect.centerx
        dy = player2.rect.centery - player.rect.centery

        dx /= distance
        dy /= distance

        # How far the players exceed the chain length
        stretch = distance - MAX_DISTANCE

        # Strength of the chain
        force = stretch * 0.05

        # Pull player 1 toward player 2
        player.velocity_x += dx * force
        player.velocity_y += dy * force

        # Pull player 2 toward player 1
        player2.velocity_x -= dx * force
        player2.velocity_y -= dy * force

    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (80, 80, 80), player.rect.center, player2.rect.center, 5)
    player.draw(screen, (0, 0, 255))
    player2.draw(screen, (255, 0, 0))
    pipe.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


