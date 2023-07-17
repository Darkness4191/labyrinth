import json

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Labyrinth:
    def __init__(self, height, width):
        self.matrix = [[] * width] * height

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = Cell(j, i)




