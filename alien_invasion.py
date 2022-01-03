import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    # Инифцилизирует игру и создает объект экрана
    pygame.init()
    pygame.display.set_caption("Alien battle")
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship=Ship(screen)
    
    # Запуск основного цикла
    while True:
    #   При каждом проходе цикла перерисовывается экран
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()
