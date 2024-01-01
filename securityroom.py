import pygame
import sys
from cell import draw_text

def security_exit_room(screen, inv, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)

    securityroom = pygame.image.load('images/securityroomexit.jpg')
    securityroom = pygame.transform.scale(securityroom, (1000, 600))
    screen.blit(securityroom, (0,0))

    arrow = pygame.image.load('images/arrow.png')
    arrow = pygame.transform.rotate(arrow, 180)

    inv.draw_inventory(screen)

    if inv.three == True:
        if mouse_x >= 0 and mouse_x <= 205 and mouse_y >= 250 and mouse_y <= 476:
            pygame.draw.line(screen, (249,194,60), (0, 250), (206, 250), width=2)
            pygame.draw.line(screen, (249,194,60), (206, 250), (215, 476), width=2)
    else:
        draw_text("This door requires a key card.", text_font, (255,255,255), screen, 500, 565)

    if mouse_x >= 548 and mouse_x <= 599 and mouse_y >= 250 and mouse_y <= 470:
        pygame.draw.polygon(screen, (249,194,60), [(548, 250), (600, 249), (599, 470), (546, 464)], width=2)

    if mouse_x >= 621 and mouse_x <= 675 and mouse_y >= 250 and mouse_y <= 471:
        pygame.draw.polygon(screen, (249,194,60), [(621, 250), (675, 251), (675, 476), (620, 471)], width=2)
    
    if mouse_x >= 697 and mouse_x <= 756 and mouse_y >= 250 and mouse_y <= 480:
        pygame.draw.polygon(screen, (249,194,60), [(697, 250), (756, 250), (758, 485), (692, 480)], width=2)

    if mouse_x >= 782 and mouse_x <= 845 and mouse_y >= 250 and mouse_y <= 487:
        pygame.draw.polygon(screen, (249,194,60), [(782, 250), (846, 248), (845, 493), (777, 487)], width=2)

    if mouse_x >= 875 and mouse_x <= 975 and mouse_y >= 270 and mouse_y <= 315:
        arrow = pygame.transform.scale(arrow, (110, 80))
        screen.blit(arrow, (870,260))
    else:
        arrow = pygame.transform.scale(arrow, (100, 70))
        screen.blit(arrow, (875,265))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if mouse_x >= 875 and mouse_x <= 975 and mouse_y >= 270 and mouse_y <= 315:
                return "security_room_screen"
            elif mouse_x >= 548 and mouse_x <= 599 and mouse_y >= 250 and mouse_y <= 470:
                status.server = 1
                return "server_screen"
            elif mouse_x >= 621 and mouse_x <= 675 and mouse_y >= 250 and mouse_y <= 471:
                status.server = 2
                return "server_screen"
            elif mouse_x >= 697 and mouse_x <= 756 and mouse_y >= 250 and mouse_y <= 480:
                status.server = 3
                return "server_screen"
            elif mouse_x >= 782 and mouse_x <= 845 and mouse_y >= 250 and mouse_y <= 487:
                status.server = 4
                return "server_screen"
            elif inv.three == True and mouse_x >= 0 and mouse_x <= 205 and mouse_y >= 250 and mouse_y <= 476:
                return "winner_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "security_exit_room"

def connect_game_screen(screen, status, block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, block14, block15, block16, block17, block18, block19, block20, block21, block22):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)
    timer_font = pygame.font.Font("fonts/textfont.ttf", 18)

    securityblur = pygame.image.load('images/securityblur.png')
    securityblur = pygame.transform.scale(securityblur, (1000, 600))
    screen.blit(securityblur, (0,0))

    pygame.draw.rect(screen, (40,40,40), pygame.Rect(150, 50, 700, 500))
    pygame.draw.rect(screen, (249,194,60), pygame.Rect(150, 50, 700, 500), width=2)


    connectgame = pygame.image.load('images/connectgame.png')
    screen.blit(connectgame, (200,100))

    if status.alarm == True:
        status.timer -= 1
        if int(status.timer/45) < 0:
            pygame.mixer.Sound.stop(status.alarmsound)
            return "loser_screen"
        lock = pygame.image.load('images/lock.png')
        draw_text("Looks like I need to complete the circuit.", text_font, (255,255,255), screen, 500, 525)
    else:
        lock = pygame.image.load('images/unlock.png')

    lock = pygame.transform.scale(lock, (50, 50))
    screen.blit(lock, (228,419))
    
    draw_text(str(int(status.timer/45)), timer_font, (0,0,0), screen, 248, 160)
    
    block1.draw(screen, 298, 108)
    block2.draw(screen, 353, 108)
    block3.draw(screen, 407, 108)
    block4.draw(screen, 462, 108)
    block5.draw(screen, 517, 108)
    block6.draw(screen, 572, 108)
    block7.draw(screen, 627, 108)

    block8.draw(screen, 353, 163)
    block9.draw(screen, 407, 163)
    block10.draw(screen, 462, 163)
    block11.draw(screen, 517, 163)
    block12.draw(screen, 572, 163)
    block13.draw(screen, 627, 163)

    block14.draw(screen, 353, 218)
    block15.draw(screen, 407, 218)
    block16.draw(screen, 462, 218)
    block17.draw(screen, 572, 218)
    block18.draw(screen, 627, 218)
    block19.draw(screen, 682, 218)

    block20.draw(screen, 353, 273)
    block21.draw(screen, 627, 273)
    block22.draw(screen, 682, 273)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            before = status.alarm
            if not(mouse_x >= 150 and mouse_x <= 850 and mouse_y >= 50 and mouse_y <= 550) and not(mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75):
                return "security_room_screen"
            elif mouse_x >= 298 and mouse_x <= 353 and mouse_y >= 108 and mouse_y <= 163:
                block1.change()
            elif mouse_x > 353 and mouse_x <= 407 and mouse_y >= 108 and mouse_y <= 163:
                block2.change()
            elif mouse_x > 407 and mouse_x <= 462 and mouse_y >= 108 and mouse_y <= 163:
                block3.change()
            elif mouse_x > 462 and mouse_x <= 517 and mouse_y >= 108 and mouse_y <= 163:
                block4.change()
            elif mouse_x > 517 and mouse_x <= 572 and mouse_y >= 108 and mouse_y <= 163:
                block5.change()
            elif mouse_x > 572 and mouse_x <= 627 and mouse_y >= 108 and mouse_y <= 163:
                block6.change()
            elif mouse_x > 627 and mouse_x <= 682 and mouse_y >= 108 and mouse_y <= 163:
                block7.change()
            elif mouse_x > 353 and mouse_x <= 407 and mouse_y > 163 and mouse_y <= 218:
                block8.change()
            elif mouse_x > 407 and mouse_x <= 462 and mouse_y > 163 and mouse_y <= 218:
                block9.change()
            elif mouse_x > 462 and mouse_x <= 517 and mouse_y > 163 and mouse_y <= 218:
                block10.change()
            elif mouse_x > 517 and mouse_x <= 572 and mouse_y > 163 and mouse_y <= 218:
                block11.change()
            elif mouse_x > 572 and mouse_x <= 627 and mouse_y > 163 and mouse_y <= 218:
                block12.change()
            elif mouse_x > 627 and mouse_x <= 682 and mouse_y > 163 and mouse_y <= 218:
                block13.change()
            elif mouse_x > 353 and mouse_x <= 407 and mouse_y > 218 and mouse_y <= 273:
                block14.change()
            elif mouse_x > 407 and mouse_x <= 462 and mouse_y > 218 and mouse_y <= 273:
                block15.change()
            elif mouse_x > 462 and mouse_x <= 517 and mouse_y > 218 and mouse_y <= 273:
                block16.change()
            elif mouse_x > 572 and mouse_x <= 627 and mouse_y > 218 and mouse_y <= 273:
                block17.change()
            elif mouse_x > 627 and mouse_x <= 682 and mouse_y > 218 and mouse_y <= 273:
                block18.change()
            elif mouse_x > 682 and mouse_x <= 737 and mouse_y > 218 and mouse_y <= 273:
                block19.change()
            elif mouse_x > 353 and mouse_x <= 407 and mouse_y > 273 and mouse_y <= 328:
                block20.change()
            elif mouse_x > 627 and mouse_x <= 682 and mouse_y > 273 and mouse_y <= 328:
                block21.change()
            elif mouse_x > 682 and mouse_x <= 737 and mouse_y > 273 and mouse_y <= 328:
                block22.change()
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

            if (block1.index == 3 and block2.index == 0 and (block3.index == 0 or block3.index == 2) and (block4.index == 0 or block4.index == 2) and block5.index == 1 and block6.index == 0 and block7.index == 3 and
                block8.index == 2 and block9.index == 0 and block10.index == 1 and block11.index == 0 and block12.index == 2 and block13.index == 1 and
                block14.index == 3 and block15.index == 1 and block16.index == 0 and block17.index == 0 and block18.index == 3 and block19.index == 1 and
                block20.index == 1 and block21.index == 3 and (block22.index == 0 or block22.index == 2)):
                pygame.mixer.Sound.stop(status.alarmsound)
                status.alarm = False
            else:
                status.alarm = True
            
            if before == False and status.alarm == True:
                status.alarmsound.play()
            

    return "connect_game_screen"

def security_room_screen(screen, inv, status):
    screen.fill((255,255,255))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_font = pygame.font.Font("fonts/textfont.ttf", 16)
    timer_font = pygame.font.Font("fonts/textfont.ttf", 50)

    securityroom = pygame.image.load('images/securityroom.jpg')
    securityroom = pygame.transform.scale(securityroom, (1000, 600))
    screen.blit(securityroom, (0,0))
    arrow = pygame.image.load('images/arrow.png')

    if status.alarm == True:
        status.timer -= 1
        if int(status.timer/45) < 0:
            pygame.mixer.Sound.stop(status.alarmsound)
            return "loser_screen"
        draw_text("I set off the alarm! How do I disarm it?", text_font, (255,255,255), screen, 500, 565)
        lock = pygame.image.load('images/lock.png')
    else:
        lock = pygame.image.load('images/unlock.png')
        if mouse_x >= 25 and mouse_x <= 125 and mouse_y >= 270 and mouse_y <= 315:
            arrow = pygame.transform.scale(arrow, (110, 80))
            screen.blit(arrow, (20,260))
        else:
            arrow = pygame.transform.scale(arrow, (100, 70))
            screen.blit(arrow, (25,265))

        inv.draw_inventory(screen)

        if inv.three == False:
            if mouse_x >= 852 and mouse_x <= 872 and mouse_y >= 518 and mouse_y <= 538:
                keycard = pygame.image.load('images/keycarddarkborder.png')
            else:
                keycard = pygame.image.load('images/keycarddark.png')
            keycard = pygame.transform.scale(keycard, (20, 20))
            screen.blit(keycard, (852,518))

    draw_text(str(int(status.timer/45)), timer_font, (0,0,0), screen, 685, 290)

    lock = pygame.transform.scale(lock, (50, 50))
    screen.blit(lock, (505,255))

    if mouse_x >= 193 and mouse_x <= 243 and mouse_y >= 254 and mouse_y <= 451:
        pygame.draw.polygon(screen, (249,194,60), [(193, 254), (243, 254), (247, 445), (195, 451)], width=2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if mouse_x >= 193 and mouse_x <= 243 and mouse_y >= 254 and mouse_y <= 451:
                return "connect_game_screen"
            elif status.alarm == False and mouse_x >= 25 and mouse_x <= 125 and mouse_y >= 270 and mouse_y <= 315:
                return "security_exit_room"
            elif status.alarm == False and inv.three == False and mouse_x >= 852 and mouse_x <= 872 and mouse_y >= 518 and mouse_y <= 538:
                inv.set_item3('images/keycard.png')
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False

    return "security_room_screen"