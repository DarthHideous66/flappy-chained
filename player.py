
import pygame
import os

class Player:
    def __init__(self, x, y, animation_folder):
        self.width = 80
        self.height = 50
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed = 5
        self.gravity = 0.5
        self.velocity_x = 0
        self.velocity_y = 0
        self.jump_strength = -8
        self.dead = False

        # Load all animation frames from the chosen folder
        self.frame_dict = {}

        files = sorted(
            file for file in os.listdir(animation_folder)
            if file.endswith(".png")
        )

        for index, file in enumerate(files):
            image = pygame.image.load(
                os.path.join(animation_folder, file)
            ).convert_alpha()

            image = pygame.transform.scale(
                image, (self.width, self.height)
            )

            self.frame_dict[index] = image

        self.frame_index = 0
        self.animation_speed = 0.15
        self.animation_timer = 0
        self.image = self.frame_dict[0]

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

    def animate(self):
        self.animation_timer += self.animation_speed

        if self.animation_timer >= 1:
            self.animation_timer = 0
            self.frame_index = (
                self.frame_index + 1
            ) % len(self.frame_dict)

        self.image = self.frame_dict[self.frame_index]

    def update(self, collider):
        self.velocity_y += self.gravity

        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.velocity_y = 0

        if (
            self.rect.colliderect(collider.upper_rect)
            or self.rect.colliderect(collider.lower_rect)
        ):
            self.dead = True

        return self.dead

    def reset(
        self, x, y, speed=5, gravity=0.5,
        jump_strength=-8, velocity_x=0, velocity_y=0
    ):
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.gravity = gravity
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.jump_strength = jump_strength
        self.dead = False

    def draw(self, screen, colour=None):
        screen.blit(self.image, self.rect)
