import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ Класс представляющий одного пришельца """

    def __init__(self, ai_settings, screen):
        """ Инифцилизирует пришельца и задает его начальную позицию """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # загрузка изображения пришельца и назначение rect
        self.image = pygame.image.load('images/sip.bmp')
        self.rect = self.image.get_rect()
        # каждый новый пришелец появляется в верхнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def update(self):
        """ Перемещает пришельца вправо и влево """
        self.x += (self.ai_settings.alien_speed_factor *
                  self.ai_settings.fleet_deriction)
        self.rect.x = self.x

    def check_edges(self):
        """ Возвращвет True ,если пришелец  находиться у края экрана """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """ Выводит пришельца в текущую позицию """
        self.screen.blit(self.image, self.rect)
