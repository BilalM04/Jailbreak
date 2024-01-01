import pygame
import sys
from player import Player
from cell import draw_text

def zoom_lock(screen, inv, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    cellfrontblur = pygame.image.load('images/cellfrontblur.png')
    cellfrontblur = pygame.transform.scale(cellfrontblur, (1000, 600))
    screen.blit(cellfrontblur, (0,0))

    pygame.draw.rect(screen, (40,40,40), pygame.Rect(350, 100, 300, 400))

    doorzoom = pygame.image.load('images/doorzoom.png')
    doorzoom = pygame.transform.scale(doorzoom, (250, 350))
    screen.blit(doorzoom, (375,125))

    pygame.draw.line(screen, (249,194,60), (350, 100), (650, 100), width=2) 
    pygame.draw.line(screen, (249,194,60), (350, 100), (350, 500), width=2) 
    pygame.draw.line(screen, (249,194,60), (350, 500), (650, 500), width=2) 
    pygame.draw.line(screen, (249,194,60), (650, 100), (650, 500), width=2) 

    if inv.two == False:
        draw_text("I need to find a key.", text_font, (255,255,255), screen, 500, 550)
    else:
        if mouse_x >= 542 and mouse_x <= 606 and mouse_y >= 277 and mouse_y <= 339:
            pygame.draw.line(screen, (249,194,60), (542, 277), (606, 277), width=2) 
            pygame.draw.line(screen, (249,194,60), (542, 277), (542, 339), width=2) 
            pygame.draw.line(screen, (249,194,60), (542, 339), (606, 339), width=2) 
            pygame.draw.line(screen, (249,194,60), (606, 277), (606, 339), width=2) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if not(mouse_x >= 350 and mouse_x <= 650 and mouse_y >= 100 and mouse_y <= 500) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "cell_front_screen"
            elif inv.two == True and mouse_x >= 542 and mouse_x <= 606 and mouse_y >= 277 and mouse_y <= 339:
                return "hallway_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False
            
    return "zoom_lock"


def front(screen):
    hall = pygame.image.load('images/hall.jpg')
    hall = pygame.transform.scale(hall, (700, 350))
    screen.blit(hall, (150,125))

    bars = pygame.image.load('images/bars.png')
    bars = pygame.transform.scale(bars, (700, 350))
    screen.blit(bars, (150,125))

    pygame.draw.polygon(screen, (50, 50, 50), [(0, 0), (150, 125), (850, 125), (1000, 0)])
    pygame.draw.polygon(screen, (30, 30, 30), [(0, 600), (150, 475), (850, 475), (1000, 600)])

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_x >= 403 and mouse_x <= 590 and mouse_y >= 232 and mouse_y <= 466:
        pygame.draw.line(screen, (249,194,60), (403, 232), (590, 232), width=2) 
        pygame.draw.line(screen, (249,194,60), (403, 465), (590, 465), width=2) 
        pygame.draw.line(screen, (249,194,60), (403, 232), (403, 465), width=2) 
        pygame.draw.line(screen, (249,194,60), (590, 465), (590, 232), width=2) 

    if mouse_x >= 150 and mouse_x <= 850 and mouse_y >= 125 and mouse_y <= 475 and not(mouse_x >= 403 and mouse_x <= 590 and mouse_y >= 232 and mouse_y <= 466):
        pygame.draw.line(screen, (249,194,60), (150, 125), (150, 475), width=2) 
        pygame.draw.line(screen, (249,194,60), (150, 475), (850, 475), width=2) 
        pygame.draw.line(screen, (249,194,60), (150, 125), (850, 125), width=2) 
        pygame.draw.line(screen, (249,194,60), (850, 475), (850, 125), width=2) 

    lamp = pygame.image.load('images/lamp.png')
    lamp = pygame.transform.scale(lamp, (100, 120))
    screen.blit(lamp, (450,62.5))

def zoom_hallway(width, height, screen, moving_sprites, player, status):
    screen.fill((255,255,255))

    cellfrontblur = pygame.image.load('images/cellfrontblur.png')
    cellfrontblur = pygame.transform.scale(cellfrontblur, (1000, 600))
    screen.blit(cellfrontblur, (0,0))

    pygame.draw.rect(screen, (200,200,200), pygame.Rect(100, 100, 800, 400))

    hallwaybright = pygame.image.load('images/hallwaybright.png')
    hallwaybright = pygame.transform.scale(hallwaybright, (800, 400))
    screen.blit(hallwaybright, (100,100))

    pygame.draw.line(screen, (249,194,60), (100, 100), (900, 100), width=2) 
    pygame.draw.line(screen, (249,194,60), (100, 100), (100, 500), width=2) 
    pygame.draw.line(screen, (249,194,60), (100, 500), (900, 500), width=2) 
    pygame.draw.line(screen, (249,194,60), (900, 100), (900, 500), width=2) 

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if not(mouse_x > 100 and mouse_x < 900 and mouse_y > 100 and mouse_y < 500) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "cell_front_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    text_font = pygame.font.Font("fonts/textfont.ttf", 16)
    draw_text("Hmm... how do I get out there?", text_font, (255,255,255), screen, 500, 550)

    return "zoom_hallway"

def cell_front_screen(screen, moving_sprites, player, inv, status):
    # Colors
    WHITE = (255, 255, 255)
    GRAY2 = (75, 75, 75)
    BLACK = (0,0,0)
    BLUE = (4,124,252)
    GRAY = (150, 150, 150)
    YELLOW = (249,194,60)
    RED = (237,53,91)

    screen.fill((40,40,40))
    mouse_x, mouse_y = pygame.mouse.get_pos()

    
    if mouse_x >= 444 and mouse_x <= 554 and mouse_y >= 566 and mouse_y <= 583:    
        text_font = pygame.font.Font("fonts/textfont.ttf", 20)
    else:
        text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if mouse_x >= 444 and mouse_x <= 554 and mouse_y >= 566 and mouse_y <= 583:
                return "cell_back_screen"
            elif mouse_x >= 150 and mouse_x <= 850 and mouse_y >= 125 and mouse_y <= 475 and not(mouse_x >= 403 and mouse_x <= 590 and mouse_y >= 232 and mouse_y <= 466):
                return "zoom_hallway"
            elif mouse_x >= 403 and mouse_x <= 590 and mouse_y >= 232 and mouse_y <= 466:
                return "zoom_lock"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False
    #     # if event.type == pygame.KEYDOWN:
    #     #     if event.key == pygame.K_DOWN:
    #     #         player.animate("down")
    #     #     elif event.key == pygame.K_UP:
    #     #         player.animate("up")
    #     #     elif event.key == pygame.K_LEFT:
    #     #         player.animate("left")
    #     #     elif event.key == pygame.K_RIGHT:
    #     #         player.animate("right")
    #     # else:
    #     #     player.animate("still")

    front(screen)
    inv.draw_inventory(screen)

    draw_text("Turn Around", text_font, (255,255,255), screen, 500, 575)
    # moving_sprites.draw(screen)
    # moving_sprites.update()

    return "cell_front_screen"