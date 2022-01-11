class Settings():
    """ Класс для хранения настроек игры """

    def __init__(self):
        """ Иниацилизирует настройки игры """
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (90, 90, 90)
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        self.fleet_deriction = 1
        self.ship_limit = 3
        self.speedup_scale = 1.3  # Это ускорение игры Илюх меня под себя
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ иниацилизирует настройки меняющиеся в ходе игры  """
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        self.fleet_deriction = 1
        # Подсчет очков
        self.alien_points = 2

    def increase_speed(self):
        """ Увеличивает настройки скорости """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
