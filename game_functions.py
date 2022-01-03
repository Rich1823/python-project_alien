import sys
import pygame


def check_events():
    # Отслеживание событий клавиатуры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()
