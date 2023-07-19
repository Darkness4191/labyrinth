import pygame, math
from laby import *

WIDTH = 1280
HEIGHT = 720

MAX_WIDTH = 1200
MAX_HEIGHT = 640

class Game:
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

    def draw_line(self, x1, y1, x2, y2):
        pygame.draw.line(self.screen, (255, 255, 255), pygame.Vector2(x1, y1), pygame.Vector2(x2, y2))

    def draw_matrix(self):
        ratio_matrix = self.labyrinth.width / self.labyrinth.height
        ratio_max = MAX_WIDTH / MAX_HEIGHT

        if ratio_matrix > ratio_max:
            MATRIX_WIDTH = MAX_WIDTH
            MATRIX_HEIGHT = MAX_WIDTH / ratio_matrix
        elif ratio_matrix < ratio_max:
            MATRIX_WIDTH = MAX_HEIGHT * ratio_matrix
            MATRIX_HEIGHT = MAX_HEIGHT

        start_x = WIDTH / 2 - MATRIX_WIDTH / 2
        start_y = HEIGHT / 2 - MATRIX_HEIGHT / 2

        step_x = step_y = MATRIX_WIDTH / self.labyrinth.width

        for i in range(len(self.labyrinth.matrix)):
            for j in range(len(self.labyrinth.matrix[i])):
                if self.labyrinth.matrix[i][j].walls[TOP]:
                    self.draw_line(start_x + step_x * i, start_y + step_y * j, start_x + step_x * (i + 1), start_y + step_y * j)
                if self.labyrinth.matrix[i][j].walls[BOTTOM]:
                    self.draw_line(start_x + step_x * i, start_y + step_y * (j + 1), start_x + step_x * (i + 1), start_y + step_y * (j + 1))
                if self.labyrinth.matrix[i][j].walls[LEFT]:
                    self.draw_line(start_x + step_x * i, start_y + step_y * j, start_x + step_x * i, start_y + step_y * (j + 1))
                if self.labyrinth.matrix[i][j].walls[RIGHT]:
                    self.draw_line(start_x + step_x * (i + 1), start_y + step_y * j, start_x + step_x * (i + 1), start_y + step_y * (j + 1))


    def show(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            self.screen.fill((0, 0, 0))

            self.draw_matrix()

            self.clock.tick(60)  # limits FPS to 60

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.event.pump()

            pygame.display.flip()

        pygame.quit()
