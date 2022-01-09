import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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


def update_screen(ai_settings, screen,stats, ship, aliens, bullets,play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """ Обновляет позиции пуль  и уничтажает старые пули"""
    # Обновляет позиции пуль
    bullets.update()
    # Удаление пуль,вышедших за край экрана
    # Удаление пуль,вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_colisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_colisions(ai_settings, screen, ship, aliens, bullets):
    # Удаляет и пулю и пришельца
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Уничтожение сужествующих пуль и создание нового флота
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Выпускает пулю ,если максимум еще не достиг """
    # Создание новой пули и включение ее в группу
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Создает пришельца и размещает его в пряду """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width+2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ Создание флота пришельцев  """
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)
# Создание флота
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_alien_x(ai_settings, alien_width):
    """ Вычесляет кол-во пришельцев в ряду """
    available_space_x = ai_settings.screen_width-2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """ определяет кол-во рядов помещающихся на экране """
    available_space_y = (ai_settings.screen_height -
                         (5*alien_height)-ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """ Реагирует на достижение края экрана """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ Опускает весь флот и меняет направление  """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_deriction *= -1


def update_aliens(ai_settings,stats,screen,  ship, aliens,bullets):
    """ Обновляет позиции всех во флоте """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Проверка коализий "Пришелец-корабль"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # Проверка пришельцев добравшихся до нижнего края экрана
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ Обрабатывает столкновение корабля с пришельцем  """
    if stats.ship_left >0:  
        # уменьшение ship_left
        stats.ship_left -= 1
        # очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()
        # Создание нового флота и размещение корабля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Пауза
        sleep(0.5)
    else:
        stats.game_active=False
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """ Проверяет добрались ли пришельцы до нижнего края экрана """
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            # Происходит то же,что при столкновении с кораблем
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break