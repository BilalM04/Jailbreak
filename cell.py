import pygame

class Status():
    def __init__(self):
        self.bars = True
        self.key = False
        self.alarm = True
        self.timer = 91*45
        self.server = 0
        self.room = 1
        self.music = 'sounds/mainmenu.ogg'
        self.alarmsound = pygame.mixer.Sound('sounds/alarm.ogg')
        self.click = pygame.mixer.Sound('sounds/click.wav')
        self.sound = False

class Inventory():
    
    def __init__(self):
        self.item1 = pygame.image.load('images/empty.png')
        self.item2 = pygame.image.load('images/empty.png')
        self.item3 = pygame.image.load('images/empty.png')
        self.item4 = pygame.image.load('images/empty.png')
        self.one = False
        self.two = False
        self.three = False
        self.four = False

    def set_item1(self, image):
        self.item1 = pygame.image.load(image)
        self.one = True

    def set_item2(self, image):
        self.item2 = pygame.image.load(image)
        self.two = True

    def set_item3(self, image):
        self.item3 = pygame.image.load(image)
        self.three = True

    def set_item4(self, image):
        self.item4 = pygame.image.load(image)
        self.four = True

    def draw_inventory(self, screen):
        pygame.draw.rect(screen, (180,180,180), (20, 20, 50, 50))
        pygame.draw.rect(screen, (180,180,180), (20, 70, 50, 50))
        pygame.draw.rect(screen, (180,180,180), (20, 120, 50, 50))
        pygame.draw.rect(screen, (180,180,180), (20, 170, 50, 50))
        pygame.draw.line(screen, (0,0,0), (20,20), (20,220), 2)
        pygame.draw.line(screen, (0,0,0), (20,20), (70,20), 2)
        pygame.draw.line(screen, (0,0,0), (70,20), (70,220), 2)
        pygame.draw.line(screen, (0,0,0), (20,219), (70,219), 2)
        pygame.draw.line(screen, (0,0,0), (20,170), (70,170), 2)
        pygame.draw.line(screen, (0,0,0), (20,70), (70,70), 2)
        pygame.draw.line(screen, (0,0,0), (20,120), (70,120), 2)
        self.item1 = pygame.transform.scale(self.item1, (40, 40))
        screen.blit(self.item1, (25,25))
        self.item2 = pygame.transform.scale(self.item2, (40, 40))
        screen.blit(self.item2, (25,75))
        self.item3 = pygame.transform.scale(self.item3, (40, 40))
        screen.blit(self.item3, (25,125))

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)