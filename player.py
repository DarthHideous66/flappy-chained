
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

        self.frame_dict = {0: pygame.image.load("blue-frames/tile000.png").convert_alpha(),
                            1: pygame.image.load("blue-frames/tile001.png").convert_alpha(),
                              2: pygame.image.load("blue-frames/tile002.png").convert_alpha(),
                                3: pygame.image.load("blue-frames/tile003.png").convert_alpha(),
                                  4: pygame.image.load("blue-frames/tile004.png").convert_alpha(),
                                    5: pygame.image.load("blue-frames/tile005.png").convert_alpha()
                           }

        for key in self.frame_dict:
            self.frame_dict[key] = pygame.transform.scale(self.frame_dict[key], (40, 30))

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
            self.frame_index = (self.frame_index + 1) % len(self.frame_dict)

        self.image = self.frame_dict[self.frame_index]

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
            

    def reset(self, x, y, speed=5, gravity=0.5, jump_strength=-8, velocity_x=0, velocity_y=0):
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
        