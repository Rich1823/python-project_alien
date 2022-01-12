import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboarde():
    """ Класс для вывода игровой информации """

    def __init__(self, ai_settings, screen, stats):
        """ Иниацилизирует фтрибуты подсчета очков """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # Настройки шрифта для вывода очков
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 47)
        #Подготовка изображений счетов 
        self.prep_score()
        self.prepr_high_score() 
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        """ Преобразует текущий счет в графическое изображение """
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                            self.text_color, self.ai_settings.bg_color)
        # ВЫвод счета в правой верхней части
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ ВЫводит счет на экран """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen .blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        #вывод кораблей
        self.ships.draw(self.screen)
    def prepr_high_score(self):
        """Преобразует рекордный счет в графическое изобпажение """
        high_score=int(round(self.stats.high_score,-1))
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,
                                self.text_color,self.ai_settings.bg_color)
        #Рекорды выравниваются по центру верхней стороны 
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top
    def prep_level(self):
        """Преабразует уровень в графическое изображение """
        self.level_image=self.font.render(str(self.stats.level),True,
                                self.text_color,self.ai_settings.bg_color)
        #Уровень выводиться под текущим счетом 
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10
    def prep_ships(self):
        """Сообщает кол-во оставшихся кораблей"""
        self.ships=Group()
        for ship_number in range(self.stats.ship_left):
            ship=Ship(self.ai_settings, self.screen)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)