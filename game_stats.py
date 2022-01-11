class GameStats():
    """ Отслеживание статистики для игры """

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
# Игра запускается в активном состоянии
        self.game_active = False

    def reset_stats(self):
        """ Иниацилизирует статистику , изменяющиеся в ходе игры """
        self.ship_left = self.ai_settings.ship_limit
        self.score=0
        