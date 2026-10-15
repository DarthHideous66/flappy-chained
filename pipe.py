import pygame
import random

class Pipe:
    def __init__(self, gap, gap_y):
        self.gap = gap
        self.gap_y = gap_y
        self.upper_rect = pygame.Rect(650, 0, 50, gap_y)
        self.lower_rect = pygame.Rect(650, gap_y + gap, 50, 1000)
        self.stop_updating = False
        self.speed = 5

   
        

    def update(self):
        if self.stop_updating == False:
            if self.upper_rect.x < -50:
                self.upper_rect.x = 650
                self.lower_rect.x = 650
                self.speed += 1

                self.gap_y = random.randint(30, 550)
                self.upper_rect.height = self.gap_y
                self.lower_rect.y = self.gap_y + self.gap
                
            self.upper_rect.x -= self.speed
            self.lower_rect.x -= self.speed

        


    def draw(self, screen):
        if self.stop_updating == False:
            pygame.draw.rect(screen, (0, 255, 0), self.upper_rect)
            pygame.draw.rect(screen, (0, 255, 0), self.lower_rect)