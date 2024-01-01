import pygame
import sys
import webbrowser

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def instructions_screen(screen, status):
    WHITE = (255, 255, 255)
    BLACK = (10, 10, 10)

    title_font = pygame.font.Font("fonts/jailfont.ttf", 100)
    text_font = pygame.font.Font("fonts/textfont.ttf", 26)

    screen.fill((88,110,124))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if mouse_x >= 50 and mouse_x <= 125 and mouse_y >= 50 and mouse_y <= 100:
                return "main_screen"
            elif mouse_x >= 825 and mouse_x <= 875 and mouse_y >= 525 and mouse_y <= 575:
                webbrowser.open("https://bilalm04.github.io/")
            elif mouse_x >= 900 and mouse_x <= 950 and mouse_y >= 525 and mouse_y <= 575:
                webbrowser.open("https://www.linkedin.com/in/mohammadbilal7/")
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False
            
    draw_text("Description", title_font, BLACK, screen, 500, 150)
    draw_text("Jailbreak! Find clues, collect items, and solve", text_font, WHITE, screen, 500, 250)
    draw_text("puzzles to escape the prison. Items that are", text_font, WHITE, screen, 500, 300)
    draw_text("highlighted when hovered over are interactable.", text_font, WHITE, screen, 500, 350)
    draw_text("Good luck and have fun!", text_font, WHITE, screen, 500, 450)

    back = pygame.image.load('images/back.png')

    if mouse_x >= 50 and mouse_x <= 125 and mouse_y >= 50 and mouse_y <= 100:
        back = pygame.transform.scale(back, (85, 60))
        screen.blit(back, (45,45))
    else:
        back = pygame.transform.scale(back, (75, 50))
        screen.blit(back, (50,50))

    linkedin = pygame.image.load('images/linkedin.png')

    if mouse_x >= 900 and mouse_x <= 950 and mouse_y >= 525 and mouse_y <= 575:
        linkedin = pygame.transform.scale(linkedin, (60, 60))
        screen.blit(linkedin, (895,520))
    else:
        linkedin = pygame.transform.scale(linkedin, (50, 50))
        screen.blit(linkedin, (900,525))

    initials = pygame.image.load('images/initials.png')

    if mouse_x >= 825 and mouse_x <= 875 and mouse_y >= 525 and mouse_y <= 575:
        initials = pygame.transform.scale(initials, (60, 60))
        screen.blit(initials, (820,520))
    else:
        initials = pygame.transform.scale(initials, (50, 50))
        screen.blit(initials, (825,525))

    return "instructions_screen"