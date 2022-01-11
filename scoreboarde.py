import pygame.font


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
        self.prep_score()

    def prep_score(self):
        """ Преобразует текущий счет в графическое изображение """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.ai_settings.bg_color)
        # ВЫвод счета в правой верхней части
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def show_score(self):
        """ ВЫводит счет на экран """
        self.screen.blit(self.score_image,self.score_rect)
