import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # Создаем экран игры с указанныеми размерами (размер переадем кортежем)
        pygame.display.set_caption("Alien Invasion") # В шапке пишем название игры
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._chek_events()
            # При каждом проходе цикла перерисовывется экран.
            self._update_screen()
            # Отображение последнего прорисованного экрана
            pygame.display.flip()

    def _chek_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Переместить корабль вправо.
                    self.ship.rect.x += 1



    def _update_screen(self):
        """Обновляет изображения на экран и отображеет новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

if __name__ == '__main__':
    # Создание экзепляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
