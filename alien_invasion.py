import sys
import pygame

def run_game():
    # Инифцилизирует игру и создает объект экрана
    pygame.init()
    screen=pygame.display.set_mode((1200,700))
    pygame.display.set_caption("Alien battle")
    # Запуск основного цикла 
    while True:
        # Отслеживание событий клавиатуры
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана 
        pygame.display.flip()
run_game()