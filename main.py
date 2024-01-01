import pygame
import sys
from MainScreen import main_screen
from cell_back import cell_back_screen, toilet_zoom_normal, toilet_zoom_open, window_zoom, window_game_over, sink_zoom, bed_zoom
from cell_front import cell_front_screen, zoom_hallway, zoom_lock
from player import Player
from hallway import hallway_screen, room_game_over
from cell import Inventory, Status
from saferoom import safe_room_screen, safe_room_screen2
from securityroom import security_room_screen, connect_game_screen, security_exit_room
from game import Block
from server import server_screen
from winner import winner_screen, loser_screen
from instructions import instructions_screen
import asyncio

pygame.init()

width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jailbreak!')

programIcon = pygame.image.load('images/logo.jpg')
pygame.display.set_icon(programIcon)

async def main():
    
    moving_sprites = pygame.sprite.Group()
    player = Player(100, 500)
    moving_sprites.add(player)

    inv = Inventory()
    status = Status()
    clock = pygame.time.Clock()

    block1 = Block('images/darkbulb.png', 0)
    block2 = Block('images/threelight.png', 3)
    block3 = Block('images/straightdark.png', 0)
    block4 = Block('images/straightlight.png', 1)
    block5 = Block('images/darkbulb.png', 2)
    block6 = Block('images/bulblight.png', 0)
    block7 = Block('images/darkbulb.png', 1)
    block8 = Block('images/cornerdark.png', 0)
    block9 = Block('images/cornerlight.png', 2)
    block10 = Block('images/darkbulb.png', 2)
    block11 = Block('images/cornerlight.png', 3)
    block12 = Block('images/threedark.png', 1)
    block13 = Block('images/cornerlight.png', 0)
    block14 = Block('images/bulblight.png', 2)
    block15 = Block('images/threedark.png', 3)
    block16 = Block('images/bulblight.png', 3)
    block17 = Block('images/bulblight.png', 2)
    block18 = Block('images/cornerdark.png', 0)
    block19 = Block('images/bulblight.png', 0)
    block20 = Block('images/darkbulb.png', 0)
    block21 = Block('images/bulblight.png', 2)
    block22 = Block('images/straightdark.png', 1)

    currentScreen = "main_screen"

    pygame.mixer.music.load('sounds/mainmenu.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.pause()

    running = True
    while running:
        if currentScreen == "main_screen":
            currentScreen = main_screen(width, height, screen, status)
            inv.set_item1('images/empty.png')
            inv.set_item2('images/empty.png')
            inv.set_item3('images/empty.png')
            inv.set_item4('images/empty.png')
            inv.one = False
            inv.two = False
            inv.three = False
            inv.four = False
            status.bars = True
            status.key = False
            status.alarm = True
            status.timer = 91*45
            status.room = 1
        elif currentScreen == "instructions_screen":
            currentScreen = instructions_screen(screen, status)
        elif currentScreen == "cell_front_screen":
            currentScreen = cell_front_screen(screen, moving_sprites, player, inv, status)
        elif currentScreen == "cell_back_screen":
            currentScreen = cell_back_screen(screen, moving_sprites, player, inv, status)
        elif currentScreen == "zoom_hallway":
            currentScreen = zoom_hallway(width, height, screen, moving_sprites, player, status)
        elif currentScreen == "zoom_toilet_normal":
            currentScreen = toilet_zoom_normal(screen, status)
        elif currentScreen == "zoom_toilet_open":
            currentScreen = toilet_zoom_open(screen, inv, status)
        elif currentScreen == "zoom_window":
            currentScreen = window_zoom(screen, inv, status)
        elif currentScreen == "window_game_over":
            currentScreen = window_game_over(screen, status)
        elif currentScreen == "zoom_sink":
            currentScreen = sink_zoom(screen, status)
        elif currentScreen == "zoom_bed":
            currentScreen = bed_zoom(screen, inv, status)
        elif currentScreen == "zoom_lock":
            currentScreen = zoom_lock(screen, inv, status)
        elif currentScreen == "hallway_screen":
            currentScreen = hallway_screen(screen, status)
        elif currentScreen == "room_game_over":
            currentScreen = room_game_over(screen, status)
        elif currentScreen == "safe_room_screen":
            currentScreen = safe_room_screen(screen, status)
        elif currentScreen == "safe_room_screen2":
            currentScreen = safe_room_screen2(screen, status)
        elif currentScreen == "security_room_screen":
            currentScreen = security_room_screen(screen, inv, status)
        elif currentScreen == "connect_game_screen":
            currentScreen = connect_game_screen(screen, status, block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, block14, block15, block16, block17, block18, block19, block20, block21, block22)
        elif currentScreen == "security_exit_room":
            currentScreen = security_exit_room(screen, inv, status)
        elif currentScreen == "server_screen":
            currentScreen = server_screen(screen, status)
        elif currentScreen == "winner_screen":
            currentScreen = winner_screen(screen, status)
        elif currentScreen == "loser_screen":
            currentScreen = loser_screen(screen, status)

        if status.sound == True:
            soundicon = pygame.image.load('images/soundon.png')
            status.alarmsound.set_volume(1)
            status.click.set_volume(1)
        else:
            soundicon = pygame.image.load('images/mute.png')
            pygame.mixer.music.pause()
            status.alarmsound.set_volume(0)
            status.click.set_volume(0)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_x >= 925 and mouse_x <= 975 and mouse_y >= 25 and mouse_y <= 75:
            soundicon = pygame.transform.scale(soundicon, (60, 60))
            screen.blit(soundicon, (920, 20))
        else:
            soundicon = pygame.transform.scale(soundicon, (50, 50))
            screen.blit(soundicon, (925, 25))

        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

asyncio.run(main())
