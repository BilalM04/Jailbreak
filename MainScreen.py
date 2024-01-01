import pygame
import sys

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_screen(width, height, screen, status):
    WHITE = (255, 255, 255)
    BLACK = (10, 10, 10)
    BLUE = (4,124,252)
    YELLOW = (249,194,60)
    RED = (237,53,91)

    title_font = pygame.font.Font("fonts/jailfont.ttf", 156)
    text_font = pygame.font.Font("fonts/textfont.ttf", 26)

    mainBackground = pygame.image.load('images/mainBackground.jpg')
    mainBackground = pygame.transform.scale(mainBackground, (1000, 600))

    screen.fill(WHITE)
    screen.blit(mainBackground, (0,0))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    start_button = pygame.Rect(width//2 - 100, 300, 200, 50)
    instructions_button = pygame.Rect(width//2 - 100, 400, 200, 50)
    quit_button = pygame.Rect(width//2 - 100, 500, 200, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            status.click.play()
            if start_button.collidepoint(mouse_x, mouse_y):
                pygame.mixer.music.load('sounds/game.ogg')
                pygame.mixer.music.play(-1)
                return "cell_front_screen"
            if instructions_button.collidepoint(mouse_x, mouse_y):
                return "instructions_screen"
            if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
                if status.sound == False:
                    status.sound = True
                    pygame.mixer.music.unpause()
                else:
                    status.sound = False
            if quit_button.collidepoint(mouse_x, mouse_y):
                pygame.quit()
                sys.exit()

    draw_text("Jailbreak!", title_font, BLACK, screen, width // 2, height // 4)

    if start_button.collidepoint(mouse_x, mouse_y):
        start_button = pygame.Rect(width//2 - 105, 295, 210, 60)
    if instructions_button.collidepoint(mouse_x, mouse_y):
        instructions_button = pygame.Rect(width//2 - 105, 395, 210, 60)
    if quit_button.collidepoint(mouse_x, mouse_y):
        quit_button = pygame.Rect(width//2 - 105, 495, 210, 60)

    pygame.draw.rect(screen, BLUE, start_button, border_radius = 5)
    draw_text("Start", text_font, WHITE, screen, start_button.centerx, start_button.centery)
    pygame.draw.rect(screen, YELLOW, instructions_button, border_radius = 5)
    draw_text("Description", text_font, WHITE, screen, instructions_button.centerx, instructions_button.centery)
    pygame.draw.rect(screen, RED, quit_button, border_radius = 5)
    draw_text("Quit", text_font, WHITE, screen, quit_button.centerx, quit_button.centery)

    return "main_screen"