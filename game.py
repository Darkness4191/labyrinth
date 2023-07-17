import pygame
from laby import Labyrinth, Cell, Direction

WIDTH = 1280
HEIGHT = 720

MATRIX_WIDTH = 640
MATRIX_HEIGHT = 640

class Game:
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

    def draw_line(self, x1, y1, x2, y2):
        pygame.draw.line(self.screen, (255, 255, 255), pygame.Vector2(x1, y1), pygame.Vector2(x2, y2))

    def show(self):
        start_x = WIDTH / 2 - MATRIX_WIDTH / 2
        start_y = HEIGHT / 2 - MATRIX_HEIGHT / 2
        step_x = MATRIX_WIDTH / self.labyrinth.width
        step_y = MATRIX_HEIGHT / self.labyrinth.height

        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            self.screen.fill((0, 0, 0))

            for i in range(len(self.labyrinth.matrix)):
                for j in range(len(self.labyrinth.matrix[i])):
                    if self.labyrinth.matrix[i][j].walls[Direction.TOP.value]:
                        self.draw_line(start_x + step_x * i, start_y + step_y * j, start_x + step_x * (i + 1), start_y + step_y * j)
                    if self.labyrinth.matrix[i][j].walls[Direction.BOTTOM.value]:
                        self.draw_line(start_x + step_x * i, start_y + step_y * (j + 1), start_x + step_x * (i + 1), start_y + step_y * (j + 1))
                    if self.labyrinth.matrix[i][j].walls[Direction.LEFT.value]:
                        self.draw_line(start_x + step_x * i, start_y + step_y * j, start_x + step_x * i, start_y + step_y * (j + 1))
                    if self.labyrinth.matrix[i][j].walls[Direction.RIGHT.value]:
                        self.draw_line(start_x + step_x * (i + 1), start_y + step_y * j, start_x + step_x * (i + 1), start_y + step_y * (j + 1))

            self.clock.tick(30)  # limits FPS to 60

            pygame.display.flip()

        pygame.quit()
