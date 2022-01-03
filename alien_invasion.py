import sys
import pygame
from settings import Settings
from ship import Ship

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
        # Отслеживание событий клавиатуры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    #   При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()


run_game()
