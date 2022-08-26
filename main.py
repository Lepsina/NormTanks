import pygame
import control_all_project
from Ship_my import ship_my

def Display_D():
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Ships_battle")
    bg_color = (0, 0, 0)
    ship = ship_my(screen)
    while True:
        control_all_project.all_control(ship)
        ship.update_ship()
        screen.fill(bg_color)
        ship.risovka()
        pygame.display.flip()
Display_D()

