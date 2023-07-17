from enum import Enum
import json

class Direction(Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.walls = [True] * 4

class Labyrinth:
    def __init__(self, width, height):
        self.matrix = []

        for i in range(height):
            sub = []
            for j in range(width):
                sub.append(Cell(i, j))
            self.matrix.append(sub)

        self.width = width
        self.height = height

    def remove_wall(self, x, y, direc):
        self.matrix[x][y].walls[direc] = False

        if direc % 2 == 0:
            direc += 1
        else:
            direc -= 1

        if x > 0 and x < (self.width - 1) and direc >= 2:
            if direc == Direction.LEFT.value:
                x += 1
            else:
                x -= 1
        elif y > 0 and y < (self.height - 1) and direc <= 1:
            if direc == Direction.TOP.value:
                y += 1
            else:
                y -= 1

        self.matrix[x][y].walls[direc] = False









