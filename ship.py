import pygame


class Ship():
    def __init__(self, screen):
        """ Инифцилизирует корабль и задает его начальную позицию """
        self.screen = screen
        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load("images/ship2.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Обновляет позицию коробля с учетом флага """
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """ Рисует корабль в текущей позиции """
        self.screen.blit(self.image, self.rect)
