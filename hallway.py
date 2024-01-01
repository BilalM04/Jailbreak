import pygame
import sys
from cell import draw_text

def room_game_over(screen, status):
    screen.fill((50,50,50))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    windowgameover = pygame.image.load('images/roomgameover.png')
    windowgameover = pygame.transform.scale(windowgameover, (1000, 500))
    screen.blit(windowgameover, (0,0))

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

    return "room_game_over"

def hallway_screen(screen, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    hallwaybright = pygame.image.load('images/hallwaybright.png')
    hallwaybright = pygame.transform.scale(hallwaybright, (1000, 600))
    screen.blit(hallwaybright, (0,0))

    draw_text("Hmm... which door should I choose?", text_font, (255,255,255), screen, 500, 565)

    if mouse_x >= 111 and mouse_x <= 287 and mouse_y >= 160 and mouse_y <= 520:
        pygame.draw.rect(screen, (249,194,60), (111, 160, 176, 360), width=2)

    if mouse_x >= 426 and mouse_x <= 598 and mouse_y >= 160 and mouse_y <= 520:
        pygame.draw.rect(screen, (249,194,60), (426, 160, 176, 360), width=2)

    if mouse_x >= 740 and mouse_x <= 914 and mouse_y >= 160 and mouse_y <= 520:
        pygame.draw.rect(screen, (249,194,60), (740, 160, 176, 360), width=2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if mouse_x >= 111 and mouse_x <= 287 and mouse_y >= 160 and mouse_y <= 520:
                return "room_game_over"
            elif mouse_x >= 426 and mouse_x <= 598 and mouse_y >= 160 and mouse_y <= 520:
                return "safe_room_screen"
            elif mouse_x >= 740 and mouse_x <= 914 and mouse_y >= 160 and mouse_y <= 520:
                return "safe_room_screen2"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "hallway_screen"