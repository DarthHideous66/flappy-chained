
import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 25)
        self.speed = 5
        self.gravity = 0.5
        self.velocity_x = 0
        self.velocity_y = 0
        self.jump_strength = -8
        self.dead = False

    def handle_inputs(self, events, left, right, up):
        keys = pygame.key.get_pressed()

        if keys[left]:
            self.velocity_x = -self.speed
        elif keys[right]:
            self.velocity_x = self.speed
        else:
            self.velocity_x *= 0.8

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == up:
                    self.velocity_y = self.jump_strength

    def update(self, collider):
        self.velocity_y += self.gravity

        # Apply velocity to movement
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.velocity_y = 0

        if (self.rect.colliderect(collider.upper_rect) or self.rect.colliderect(collider.lower_rect)):
            self.dead = True
            return self.dead
            

    def draw(self, screen, colour):
        pygame.draw.rect(screen, colour, self.rect)
