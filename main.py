import pygame
from player import Player
import random
import math

from pipe import Pipe

pygame.init()
pygame.font.init()

score_font = pygame.font.SysFont('comic sans', 24)
WIDTH, HEIGHT = 800, 600
MAX_DISTANCE = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
game_over = False
game_started= False

# Clock for controlling FPS
clock = pygame.time.Clock()

player = Player(375, 275)
player2 = Player(300, 275)
pipe = Pipe(350, random.randint(30, 550))



def reset_game():
    global game_over
    player.reset(375, 275)
    player2.reset(300, 275)
    pipe.reset(350, random.randint(30, 200))
    game_over = False




# Main game loop
running = True
while running:
    if player.dead or player2.dead:
        game_over = True
        screen.fill((255, 255, 255))
        game_over_text = score_font.render("Game Over! Press R to Restart or ESC to Quit", 1, (0, 0, 0))
        screen.blit(game_over_text, (170, 120))
        pygame.display.flip()
    
    events = pygame.event.get()

   
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_started and event.key == pygame.K_SPACE:
                game_started = True

            elif game_over:
                if event.key == pygame.K_r:
                    reset_game()

                elif event.key == pygame.K_ESCAPE:
                    running = False

        
    if game_started and not game_over:     

        player.handle_inputs(events, pygame.K_a, pygame.K_d, pygame.K_w) 
        player.update(pipe)
        player2.handle_inputs(events, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP) 
        player2.update(pipe)
        score = pipe.update(player, player2)

        pipe.highscore(player.dead, player2.dead)

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
        scoreboard = score_font.render(f"{score}", 1, (0, 0, 0))
        screen.blit(scoreboard, (250, 250))


        

        pygame.display.flip()
        clock.tick(60)

pygame.quit()