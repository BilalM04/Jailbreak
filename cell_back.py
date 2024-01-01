import pygame
import sys
from player import Player
from cell import draw_text

def bed_zoom(screen, inv, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    cellfrontblur = pygame.image.load('images/cellbackblur.png')
    cellfrontblur = pygame.transform.scale(cellfrontblur, (1000, 600))
    screen.blit(cellfrontblur, (0,0))

    plank = pygame.image.load('images/plank.png')
    plank = pygame.transform.scale(plank, (800, 400))
    screen.blit(plank, (100,100))

    if inv.one == False:
        draw_text("I need some sort of tool to investigate this.", text_font, (255,255,255), screen, 500, 550)

    if inv.one == True and status.key == False:
        draw_text("Maybe this wrench could be useful.", text_font, (255,255,255), screen, 500, 550)

    if  status.key == False and inv.one == True and mouse_x >= 644 and mouse_x <= 669 and mouse_y >= 357 and mouse_y <= 394:
        pygame.draw.line(screen, (249,194,60), (644, 357), (669, 357), width=2) 
        pygame.draw.line(screen, (249,194,60), (644, 357), (644, 394), width=2) 
        pygame.draw.line(screen, (249,194,60), (644, 394), (669, 394), width=2) 
        pygame.draw.line(screen, (249,194,60), (669, 357), (669, 394), width=2)

    if inv.two == False and status.key == True and mouse_x >= 644 and mouse_x <= 669 and mouse_y >= 357 and mouse_y <= 394:
        key = pygame.image.load('images/keyborder.png')
        key = pygame.transform.scale(key, (20, 30))
        screen.blit(key, (647,360))
    elif inv.two == False and status.key == True: 
        key = pygame.image.load('images/key.png')
        key = pygame.transform.scale(key, (20, 30))
        screen.blit(key, (647,360))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if not(mouse_x >= 100 and mouse_x <= 900 and mouse_y >= 100 and mouse_y <= 500) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "cell_back_screen"
            elif status.key == False and inv.two == False and inv.one == True and mouse_x >= 644 and mouse_x <= 669 and mouse_y >= 357 and mouse_y <= 394:
                status.key = True
            elif status.key == True and inv.two == False and mouse_x >= 644 and mouse_x <= 669 and mouse_y >= 357 and mouse_y <= 394:
                inv.set_item2('images/keyinv.png')
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False


    return "zoom_bed"

def window_game_over(screen, status):
    screen.fill((50,50,50))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    windowgameover = pygame.image.load('images/windowgameover.png')
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

    return "window_game_over"

def sink_zoom(screen, status):
    screen.fill((255,255,255))

    cellfrontblur = pygame.image.load('images/cellbackblur.png')
    cellfrontblur = pygame.transform.scale(cellfrontblur, (1000, 600))
    screen.blit(cellfrontblur, (0,0))

    pygame.draw.rect(screen, (30,30,30), pygame.Rect(200, 60, 600, 500))

    sinkzoom = pygame.image.load('images/sinkzoom.png')
    sinkzoom = pygame.transform.scale(sinkzoom, (700, 600))
    screen.blit(sinkzoom, (150,0))

    spider = pygame.image.load('images/spider.png')
    spider = pygame.transform.scale(spider, (60, 60))
    screen.blit(spider, (600,320))

    penny = pygame.image.load('images/penny.png')
    penny = pygame.transform.scale(penny, (50, 50))
    screen.blit(penny, (400,290))

    screw = pygame.image.load('images/screw.png')
    screw = pygame.transform.scale(screw, (60, 60))
    screen.blit(screw, (500,370))

    pygame.draw.line(screen, (249,194,60), (200, 60), (800, 60), width=2) 
    pygame.draw.line(screen, (249,194,60), (200, 60), (200, 560), width=2) 
    pygame.draw.line(screen, (249,194,60), (200, 560), (800, 560), width=2) 
    pygame.draw.line(screen, (249,194,60), (800, 60), (800, 560), width=2)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if not(mouse_x >= 200 and mouse_x <= 800 and mouse_y >= 60 and mouse_y <= 560) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "cell_back_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "zoom_sink"


def window_zoom(screen, inv, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)
 
    cellfrontblur = pygame.image.load('images/cellbackblur.png')
    cellfrontblur = pygame.transform.scale(cellfrontblur, (1000, 600))
    screen.blit(cellfrontblur, (0,0))

    if status.bars == True:
        windowzoom = pygame.image.load('images/windowzoom.png')
    else: 
        windowzoom = pygame.image.load('images/windowzoomnobar.png')
    windowzoom = pygame.transform.scale(windowzoom, (800, 400))
    screen.blit(windowzoom, (100,100))

    if inv.one == True and status.bars == True:
        draw_text("Maybe this wrench could be useful.", text_font, (255,255,255), screen, 500, 550)

    if status.bars == False:
        if mouse_x >= 286 and mouse_x <= 712 and mouse_y >= 205 and mouse_y <= 393:
            pygame.draw.line(screen, (249,194,60), (286, 205), (712, 205), width=2) 
            pygame.draw.line(screen, (249,194,60), (286, 393), (712, 393), width=2) 
            pygame.draw.line(screen, (249,194,60), (286, 205), (286, 393), width=2) 
            pygame.draw.line(screen, (249,194,60), (712, 393), (712, 205), width=2)

    if inv.one == False:
        draw_text("I need some sort of tool to pry this open.", text_font, (255,255,255), screen, 500, 550)
    else:
        if status.bars == True and (mouse_x >= 309 and mouse_x <= 329 or mouse_x >= 384 and mouse_x <= 404 or mouse_x >= 454 and mouse_x <= 474 or mouse_x >= 529 and mouse_x <= 549 or mouse_x >= 599 and mouse_x <= 619 or mouse_x >= 674 and mouse_x <= 694) and mouse_y >= 179 and mouse_y <= 419:
            pygame.draw.line(screen, (249,194,60), (309, 179), (329, 179), width=2) 
            pygame.draw.line(screen, (249,194,60), (309, 419), (329, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (309, 179), (309, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (329, 419), (329, 179), width=2)

            pygame.draw.line(screen, (249,194,60), (384, 179), (404, 179), width=2) 
            pygame.draw.line(screen, (249,194,60), (384, 419), (404, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (384, 179), (384, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (404, 419), (404, 179), width=2)

            pygame.draw.line(screen, (249,194,60), (454, 179), (474, 179), width=2) 
            pygame.draw.line(screen, (249,194,60), (454, 419), (474, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (454, 179), (454, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (474, 419), (474, 179), width=2)

            pygame.draw.line(screen, (249,194,60), (529, 179), (549, 179), width=2) 
            pygame.draw.line(screen, (249,194,60), (529, 419), (549, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (529, 179), (529, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (549, 419), (549, 179), width=2)

            pygame.draw.line(screen, (249,194,60), (599, 179), (619, 179), width=2) 
            pygame.draw.line(screen, (249,194,60), (599, 419), (619, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (599, 179), (599, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (619, 419), (619, 179), width=2)

            pygame.draw.line(screen, (249,194,60), (674, 179), (694, 179), width=2) 
            pygame.draw.line(screen, (249,194,60), (674, 419), (694, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (674, 179), (674, 419), width=2) 
            pygame.draw.line(screen, (249,194,60), (694, 419), (694, 179), width=2)

            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if not(mouse_x > 100 and mouse_x < 900 and mouse_y > 100 and mouse_y < 500) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "cell_back_screen"
            elif status.bars == True and inv.one == True and (mouse_x >= 309 and mouse_x <= 329 or mouse_x >= 384 and mouse_x <= 404 or mouse_x >= 454 and mouse_x <= 474 or mouse_x >= 529 and mouse_x <= 549 or mouse_x >= 599 and mouse_x <= 619 or mouse_x >= 674 and mouse_x <= 694) and mouse_y >= 179 and mouse_y <= 419:
                status.bars = False
            elif status.bars == False and mouse_x >= 286 and mouse_x <= 712 and mouse_y >= 205 and mouse_y <= 393:
                return "window_game_over"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "zoom_window"

def toilet_zoom_normal(screen, status):
    screen.fill((255,255,255))

    cellfrontblur = pygame.image.load('images/cellbackblur.png')
    cellfrontblur = pygame.transform.scale(cellfrontblur, (1000, 600))
    screen.blit(cellfrontblur, (0,0))

    pygame.draw.rect(screen, (30,30,30), pygame.Rect(300, 60, 400, 500))

    toiletzoom = pygame.image.load('images/toiletzoom.png')
    toiletzoom = pygame.transform.scale(toiletzoom, (600, 600))
    screen.blit(toiletzoom, (200,0))

    pygame.draw.line(screen, (249,194,60), (300, 60), (700, 60), width=2) 
    pygame.draw.line(screen, (249,194,60), (300, 60), (300, 560), width=2) 
    pygame.draw.line(screen, (249,194,60), (300, 560), (700, 560), width=2) 
    pygame.draw.line(screen, (249,194,60), (700, 60), (700, 560), width=2)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_x >= 355 and mouse_x <= 644 and mouse_y >= 91 and mouse_y <= 195:
        pygame.draw.line(screen, (249,194,60), (355, 91), (644, 91), width=3) 
        pygame.draw.line(screen, (249,194,60), (355, 91), (355, 195), width=3) 
        pygame.draw.line(screen, (249,194,60), (355, 195), (644, 195), width=3) 
        pygame.draw.line(screen, (249,194,60), (644, 91), (644, 195), width=3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if not(mouse_x >= 300 and mouse_x <= 700 and mouse_y >= 60 and mouse_y <= 560) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "cell_back_screen"
            elif mouse_x >= 355 and mouse_x <= 644 and mouse_y >= 91 and mouse_y <= 195:
                return "zoom_toilet_open"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "zoom_toilet_normal"

def toilet_zoom_open(screen, inv, status):
    screen.fill((255,255,255))

    cellfrontblur = pygame.image.load('images/cellbackblur.png')
    cellfrontblur = pygame.transform.scale(cellfrontblur, (1000, 600))
    screen.blit(cellfrontblur, (0,0))

    pygame.draw.rect(screen, (30,30,30), pygame.Rect(300, 60, 400, 500))

    toilettank = pygame.image.load('images/toilettank.png')
    toilettank = pygame.transform.scale(toilettank, (600, 600))
    screen.blit(toilettank, (200,0))

    pygame.draw.line(screen, (249,194,60), (300, 60), (700, 60), width=2) 
    pygame.draw.line(screen, (249,194,60), (300, 60), (300, 560), width=2) 
    pygame.draw.line(screen, (249,194,60), (300, 560), (700, 560), width=2) 
    pygame.draw.line(screen, (249,194,60), (700, 60), (700, 560), width=2) 

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if inv.one == False and mouse_x >= 559 and mouse_x <= 606 and mouse_y >= 123 and mouse_y <= 174:
        wrench = pygame.image.load('images/wrenchborder.png')
        wrench = pygame.transform.scale(wrench, (50, 60))
        screen.blit(wrench, (560,120))
    elif inv.one == False:
        wrench = pygame.image.load('images/wrench.png')
        wrench = pygame.transform.scale(wrench, (50, 60))
        screen.blit(wrench, (560,120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if not(mouse_x >= 300 and mouse_x <= 700 and mouse_y >= 60 and mouse_y <= 560) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "cell_back_screen"
            elif inv.one == False and mouse_x >= 559 and mouse_x <= 606 and mouse_y >= 123 and mouse_y <= 174:
                inv.one = True
                inv.set_item1("images/wrench.png")
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "zoom_toilet_open"

def back(screen):
    pygame.draw.polygon(screen, (50, 50, 50), [(0, 0), (150, 125), (850, 125), (1000, 0)])
    pygame.draw.polygon(screen, (30, 30, 30), [(0, 600), (150, 475), (850, 475), (1000, 600)])
    pygame.draw.line(screen, (50, 50, 50), (150,125), (150, 475), width=2)
    pygame.draw.line(screen, (50, 50, 50), (850,125), (850, 475), width=2)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_x >= 558 and mouse_x <= 901 and mouse_y >= 412 and mouse_y <= 485:
        bed = pygame.image.load('images/bedborder.png')
    else:
        bed = pygame.image.load('images/bed.png')

    bed = pygame.transform.scale(bed, (350, 200))
    screen.blit(bed, (550,330))

    if mouse_x >= 189 and mouse_x <= 255 and mouse_y >= 340 and mouse_y <= 498:
        toilet = pygame.image.load('images/toiletborder.png')
    else:
        toilet = pygame.image.load('images/toilet.png')

    toilet = pygame.transform.scale(toilet, (100, 165))
    screen.blit(toilet, (175,340))

    window = pygame.image.load('images/window.png')
    window = pygame.transform.scale(window, (100, 60))
    screen.blit(window, (250,200))

    if mouse_x >= 250 and mouse_x <= 350 and mouse_y >= 200 and mouse_y <= 260:
        pygame.draw.line(screen, (249,194,60), (250,200), (350, 200), width=2)
        pygame.draw.line(screen, (249,194,60), (250,200), (250, 260), width=2)
        pygame.draw.line(screen, (249,194,60), (350,200), (350, 260), width=2)
        pygame.draw.line(screen, (249,194,60), (250,260), (350, 260), width=2)

    if mouse_x >= 363 and mouse_x <= 429 and mouse_y >= 336 and mouse_y <= 502:
        sink = pygame.image.load('images/sinkborder.png')
    else:
        sink = pygame.image.load('images/sink.png')
    sink = pygame.transform.scale(sink, (100, 180))
    screen.blit(sink, (350,325))

    lamp = pygame.image.load('images/lamp.png')
    lamp = pygame.transform.scale(lamp, (100, 120))
    screen.blit(lamp, (450,62.5))

def cell_back_screen(screen, moving_sprites, player, inv, status):
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

    # Fonts
    title_font = pygame.font.Font("fonts/jailfont.ttf", 156)
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
                return "cell_front_screen"
            elif mouse_x >= 189 and mouse_x <= 255 and mouse_y >= 340 and mouse_y <= 498:
                return "zoom_toilet_normal"
            elif mouse_x >= 250 and mouse_x <= 350 and mouse_y >= 200 and mouse_y <= 260:
                return "zoom_window"
            elif mouse_x >= 363 and mouse_x <= 429 and mouse_y >= 336 and mouse_y <= 502:
                return "zoom_sink"
            elif mouse_x >= 558 and mouse_x <= 901 and mouse_y >= 412 and mouse_y <= 485:
                return "zoom_bed"
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

    back(screen)

    inv.draw_inventory(screen)
    draw_text("Turn Around", text_font, (255,255,255), screen, 500, 575)
    # moving_sprites.draw(screen)
    # moving_sprites.update()

    return "cell_back_screen"