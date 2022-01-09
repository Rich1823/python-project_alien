import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_functions as gf
from game_stats import GameStats

def run_game():
    # Инифцилизирует игру и создает объект экрана
    pygame.init()
    pygame.display.set_caption("Alien battle")
    ai_settings = Settings()
    stats=GameStats(ai_settings)

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings, screen)
    # создание пришельца
    gf.create_fleet(ai_settings, screen,ship, aliens)
    # Запуск основного цикла
    while True:
        #   При каждом проходе цикла перерисовывается экран
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
