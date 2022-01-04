import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
def run_game():
    # Инифцилизирует игру и создает объект экрана
    pygame.init()
    pygame.display.set_caption("Alien battle")
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()
    # создание пришельца
    alien=Alien(ai_settings, screen)
    # Запуск основного цикла
    while True:
        #   При каждом проходе цикла перерисовывается экран
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship,alien, bullets)

run_game()
