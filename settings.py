class Settings():
    """ Класс для хранения настроек игры """

    def __init__(self):
        """ Иниацилизирует настройки игры """
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (90, 90, 90)
        self.ship_speed_factor =3
        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
