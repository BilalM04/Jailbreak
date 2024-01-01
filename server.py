import pygame
import sys
from cell import draw_text

def server_screen(screen, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()

    securityblur = pygame.image.load('images/securityroomexitblur.jpg')
    securityblur = pygame.transform.scale(securityblur, (1000, 600))
    screen.blit(securityblur, (0,0))

    if status.server == 1:
        server = pygame.image.load('images/server1.png')
    elif status.server == 2:
        server = pygame.image.load('images/server2.png')
    elif status.server == 3:
        server = pygame.image.load('images/server3.png')
    elif status.server == 4:
        server = pygame.image.load('images/server5.png')

    pygame.draw.rect(screen, (40,40,40), pygame.Rect(325, 50, 350, 500))
    pygame.draw.rect(screen, (249,194,60), pygame.Rect(325, 50, 350, 500), width=2)

    server = pygame.transform.scale(server, (250, 400))
    screen.blit(server, (375,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if not(mouse_x >= 325 and mouse_x <= 675 and mouse_y >= 50 and mouse_y <= 550) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "security_exit_room"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False
            
    return "server_screen"

