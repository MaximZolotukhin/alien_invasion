import sys
import pygame

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800)) # Создаем экран игры с указанныеми размерами (размер переадем кортежем)
        pygame.display.set_caption("Alien Invasion") # В шапке пишем название игры

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экзепляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
