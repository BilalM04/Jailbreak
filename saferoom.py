import pygame
import sys
from cell import draw_text

def safe_room_screen(screen, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    saferoom = pygame.image.load('images/saferoom.png')
    saferoom = pygame.transform.scale(saferoom, (1000, 600))
    screen.blit(saferoom, (0,0))

    if mouse_x >= 381 and mouse_x <= 622 and mouse_y >= 505 and mouse_y <= 570:
        pygame.draw.line(screen, (249,194,60), (381, 505), (622, 505), width=3)
        pygame.draw.line(screen, (249,194,60), (659, 570), (622, 505), width=3)
        pygame.draw.line(screen, (249,194,60), (659, 570), (332, 570), width=3)
        pygame.draw.line(screen, (249,194,60), (381, 505), (332, 570), width=3)

    flashlight = pygame.image.load('images/flashlight.png')
    flashlight = pygame.transform.scale(flashlight, (300, 300))
    screen.blit(flashlight, (mouse_x - 150, mouse_y - 150))

    s1 = pygame.Surface((2000, 600))  
    s1.set_alpha(234)             
    s1.fill((0,0,0))
    s2 = pygame.Surface((850, 300))  
    s2.set_alpha(234)             
    s2.fill((0,0,0))
    s3 = pygame.Surface((850, 300))  
    s3.set_alpha(234)             
    s3.fill((0,0,0))
    s4 = pygame.Surface((2000, 600))  
    s4.set_alpha(234)             
    s4.fill((0,0,0))          
    screen.blit(s1, (mouse_x - 1000, mouse_y - 750))
    screen.blit(s2, (mouse_x - 1000, mouse_y - 150))
    screen.blit(s3, (mouse_x + 150, mouse_y - 150))
    screen.blit(s4, (mouse_x - 1000, mouse_y + 150))

    draw_text("I need to find an exit.", text_font, (255,255,255), screen, 500, 565)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if mouse_x >= 381 and mouse_x <= 622 and mouse_y >= 505 and mouse_y <= 570:
                if status.room == 1:
                    status.room = 2
                    return "safe_room_screen2"
                else:
                    status.alarmsound.play()
                    return "security_room_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "safe_room_screen"

def safe_room_screen2(screen, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    saferoom = pygame.image.load('images/saferoom2.png')
    saferoom = pygame.transform.scale(saferoom, (1000, 600))
    screen.blit(saferoom, (0,0))

    if mouse_x >= 774 and mouse_x <= 834 and mouse_y >= 177 and mouse_y <= 228:
        pygame.draw.rect(screen, (249,194,60), pygame.Rect(774, 177, 60, 51), width=3)

    flashlight = pygame.image.load('images/flashlight.png')
    flashlight = pygame.transform.scale(flashlight, (300, 300))
    screen.blit(flashlight, (mouse_x - 150, mouse_y - 150))

    s1 = pygame.Surface((2000, 600))  
    s1.set_alpha(234)             
    s1.fill((0,0,0))
    s2 = pygame.Surface((850, 300))  
    s2.set_alpha(234)             
    s2.fill((0,0,0))
    s3 = pygame.Surface((850, 300))  
    s3.set_alpha(234)             
    s3.fill((0,0,0))
    s4 = pygame.Surface((2000, 600))  
    s4.set_alpha(234)             
    s4.fill((0,0,0))          
    screen.blit(s1, (mouse_x - 1000, mouse_y - 750))
    screen.blit(s2, (mouse_x - 1000, mouse_y - 150))
    screen.blit(s3, (mouse_x + 150, mouse_y - 150))
    screen.blit(s4, (mouse_x - 1000, mouse_y + 150))

    draw_text("I need to find an exit.", text_font, (255,255,255), screen, 500, 565)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if mouse_x >= 774 and mouse_x <= 834 and mouse_y >= 177 and mouse_y <= 228:
                if status.room == 1:
                    status.room = 2
                    return "safe_room_screen"
                else:
                    status.alarmsound.play()
                    return "security_room_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "safe_room_screen2"