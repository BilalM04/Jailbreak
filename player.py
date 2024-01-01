import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.sprites = []
        self.state = "still"
        self.sprites.append(pygame.image.load('images/front_0.png'))
        self.sprites.append(pygame.image.load('images/front_1.png'))
        self.sprites.append(pygame.image.load('images/back_4.png'))
        self.sprites.append(pygame.image.load('images/back_5.png'))
        self.sprites.append(pygame.image.load('images/left_2.png'))
        self.sprites.append(pygame.image.load('images/left_3.png'))
        self.sprites.append(pygame.image.load('images/right_6.png'))
        self.sprites.append(pygame.image.load('images/right_7.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def animate(self, state):
        self.state = state

    def update(self):
        if self.state == "down":
            if self.y < 780:
                self.y += 5
            if self.current_sprite == 0:
                self.current_sprite = 1
            else:
                self.current_sprite = 0
            pygame.time.delay(100)
        elif self.state == "up":
            if self.y > 0:
                self.y -= 5
            if self.current_sprite == 2:
                self.current_sprite = 3
            else:
                self.current_sprite = 2
            pygame.time.delay(100)
        elif self.state == "left":
            self.x -= 5
            if self.current_sprite == 4:
                self.current_sprite = 5
            else:
                self.current_sprite = 4
            pygame.time.delay(100)
        elif self.state == "right":
            self.x += 5
            if self.current_sprite == 6:
                self.current_sprite = 7
            else:
                self.current_sprite = 6
            pygame.time.delay(100)
        else:
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.rect.topleft = [self.x, self.y]