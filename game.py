import pygame

class Block():
    def __init__(self, image, start):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.index = 0
        
        for i in range (start):
            self.change()

    def change(self):
        self.index += 1

        if self.index >= 4:
            self.index = 0

        self.image = pygame.transform.rotate(self.image, -90)

    def draw(self, screen, x, y):
        screen.blit(self.image, (x,y))