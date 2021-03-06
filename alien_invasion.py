import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboarde import Scoreboarde

def run_game():
    # Инифцилизирует игру и создает объект экрана
    pygame.init()
    pygame.display.set_caption("Alien battle")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    stats = GameStats(ai_settings)
    sb= Scoreboarde(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)
    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Погнали!")
    # Создание группы для хранения пуль
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings, screen)
    # создание пришельца
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла
    while True:
        #   При каждом проходе цикла перерисовывается экран
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen,sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats,sb, ship,
                         aliens, bullets, play_button)


run_game()
