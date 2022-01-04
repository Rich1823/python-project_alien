import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """ Класс представляющий одного пришельца """
    def __init__(self,ai_settings,screen):
        """ Инифцилизирует пришельца и задает его начальную позицию """
        super(Alien, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        # загрузка изображения пришельца и назначение rect
        self.image=pygame.image.load('images/sip.bmp')
        self.rect=self.image.get_rect()
        # каждый новый пришелец появляется в верхнем левом углу
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        # Сохранение точной позиции пришельца
        self.x=float(self.rect.x)    
    def blitme(self):
        """ Выводит пришельца в текущую позицию """
        self.screen.blit(self.image,self.rect)