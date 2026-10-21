import pygame
import random

class Pipe:
    def __init__(self, gap, gap_y):
        self.width = 100
        self.gap = gap
        self.gap_y = gap_y
        self.upper_rect = pygame.Rect(650, 0, self.width, gap_y)
        self.lower_rect = pygame.Rect(650, gap_y + gap, self.width, 1000)
        self.stop_updating = False
        self.speed = 5
        self.score = 0
        self.passed = False
        self.image = pygame.image.load("pipe.png").convert_alpha()
        

   
        

    def update( self, player, player2):
        if self.stop_updating == False:
            if self.upper_rect.right < 0:
                self.upper_rect.x = 650
                self.lower_rect.x = 650
                self.passed = False
                self.speed += 0.1

                self.gap_y = random.randint(30, 550)
                self.upper_rect.height = self.gap_y
                self.lower_rect.y = self.gap_y + self.gap
                
            self.upper_rect.x -= self.speed
            self.lower_rect.x -= self.speed

        if player.rect.x and player2.rect.x > self.upper_rect.x and self.passed == False:
            self.score += 1
            self.passed = True
        return self.score


    def highscore(self, dead, dead2):
        if dead or dead2:
            with open("high_score.txt", "r") as h:
                if self.score > int(h.read()):

                    with open("high_score.txt", "w") as h:
                        h.write(str(self.score))
            

    

    def reset(self, gap, gap_y, upper_x=650, lower_x=650, upper_height=0):
        self.gap = gap
        self.gap_y = gap_y
        self.upper_rect.x = upper_x
        self.upper_rect.height = upper_height
        self.lower_rect.x = lower_x
        self.lower_rect.y = gap_y + gap
        self.stop_updating = False
        self.speed = 5
        self.score = 0
        self.passed = False



    def draw(self, screen):
        # Upper pipe: stretch to fit its rectangle and flip it
        upper_image = pygame.transform.scale(
            self.image,
            (self.upper_rect.width, self.upper_rect.height)
        )
        upper_image = pygame.transform.flip(upper_image, False, True)
        screen.blit(upper_image, self.upper_rect.topleft)

        # Lower pipe: stretch to fit the visible part of the screen
        lower_height = 600 - self.lower_rect.y

        if lower_height > 0:
            lower_image = pygame.transform.scale(
                self.image,
                (self.lower_rect.width, lower_height)
            )
            screen.blit(lower_image, self.lower_rect.topleft)