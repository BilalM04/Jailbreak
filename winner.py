import pygame
import sys
from cell import draw_text

def winner_screen(screen, status):
    screen.fill((50,50,50))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    prisonescape = pygame.image.load('images/prisonescape.png')
    prisonescape = pygame.transform.scale(prisonescape, (1000, 500))
    screen.blit(prisonescape, (0,0))

    draw_text("Congratulations! You successfully esacped.", text_font, (255,255,255), screen, 500, 550)

    button = pygame.Rect(800, 525, 150, 50)
    if button.collidepoint(mouse_x, mouse_y):
        button = pygame.Rect(795, 520, 160, 60)
        text_font = pygame.font.Font("fonts/textfont.ttf", 19)

    pygame.draw.rect(screen, (249,194,60), button, border_radius = 5)
    draw_text("Main Menu", text_font, (255,255,255), screen, button.centerx, button.centery)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if button.collidepoint(mouse_x, mouse_y):
                pygame.mixer.music.load('sounds/mainmenu.ogg')
                pygame.mixer.music.play(-1)
                return "main_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "winner_screen"

def loser_screen(screen, status):
    screen.fill((50,50,50))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    prisonescape = pygame.image.load('images/securitygameover.png')
    prisonescape = pygame.transform.scale(prisonescape, (1000, 600))
    screen.blit(prisonescape, (0,0))

    pygame.draw.rect(screen, (50,50,50), pygame.Rect(0,500,1000,100))

    draw_text("You got caught! Game over.", text_font, (255,255,255), screen, 500, 550)

    button = pygame.Rect(800, 525, 150, 50)
    if button.collidepoint(mouse_x, mouse_y):
        button = pygame.Rect(795, 520, 160, 60)
        text_font = pygame.font.Font("fonts/textfont.ttf", 19)

    pygame.draw.rect(screen, (249,194,60), button, border_radius = 5)
    draw_text("Main Menu", text_font, (255,255,255), screen, button.centerx, button.centery)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if button.collidepoint(mouse_x, mouse_y):
                pygame.mixer.music.load('sounds/mainmenu.ogg')
                pygame.mixer.music.play(-1)
                return "main_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "loser_screen"