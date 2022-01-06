import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    # Отслеживание событий клавиатуры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Переместить корабль в право
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    aliens.draw(screen)
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(bullets):
    """ Обновляет позиции пуль  и уничтажает старые пули"""
    # Обновляет позиции пуль
    bullets.update()
    # Удаление пуль,вышедших за край экрана
    # Удаление пуль,вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Выпускает пулю ,если максимум еще не достиг """
    # Создание новой пули и включение ее в группу
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)




def create_alien(ai_settings, screen, aliens, alien_number):
    """ Создает пришельца и размещает его в пряду """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width+2*alien_width*alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """ Создание флота пришельцев  """
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
# Создание первого ряда пришельцев
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)

def get_number_alien_x(ai_settings, alien_width):
    """ Вычесляет кол-во пришельцев в ряду """
    available_space_x = ai_settings.screen_width-2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x
