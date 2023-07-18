from enum import Enum
from tree import *
import json, random, time

TOP = (0, -1)
BOTTOM = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.walls = {(1, 0): True,   #RIGHT
                      (-1, 0): True,  #LEFT
                      (0, 1): True,   #TOP
                      (0, -1): True,} #BOTTOM

        self.visited = False

class Labyrinth:
    def __init__(self, width, height):
        self.matrix = []

        for i in range(width):
            sub = []
            for j in range(height):
                sub.append(Cell(i, j))
            self.matrix.append(sub)

        self.width = width
        self.height = height

    def _get_unvisited_neighbours(self, cell):
        r = []

        if cell.x > 0 and not self.matrix[cell.x - 1][cell.y].visited:
            r.append(self.matrix[cell.x - 1][cell.y])
        if cell.y > 0 and not self.matrix[cell.x][cell.y - 1].visited:
            r.append(self.matrix[cell.x][cell.y - 1])
        if cell.x < (self.width - 1) and not self.matrix[cell.x + 1][cell.y].visited:
            r.append(self.matrix[cell.x + 1][cell.y])
        if cell.y < (self.height - 1) and not self.matrix[cell.x][cell.y + 1].visited:
            r.append(self.matrix[cell.x][cell.y + 1])

        return r

    def _check_if_neighbours_visited(self, cell):
        return len(self._get_unvisited_neighbours(cell)) != 0

    def _board_is_visited(self):
        for l in self.matrix:
            for c in l:
                if not c.visited:
                    return False
        return True

    def _remove_wall(self, x, y, direc : (int, int)):
        cell = self.matrix[x][y]
        cell2_x = x + direc[0]
        cell2_y = y + direc[1]

        cell.walls[direc] = False

        if cell2_x >= 0 and cell2_x < self.width and cell2_y >= 0 and cell2_y < self.height:
            self.matrix[cell.x + direc[0]][cell.y + direc[1]].walls[tuple(i * (-1) for i in direc)] = False

    def remove_wall(self, cell1 : Cell, cell2 : Cell):
        dx = cell2.x - cell1.x
        dy = cell2.y - cell1.y

        self._remove_wall(cell1.x, cell1.y, (dx, dy))

    def clear_maze(self):
        self.matrix = []

        for i in range(self.width):
            sub = []
            for j in range(self.height):
                sub.append(Cell(i, j))
            self.matrix.append(sub)

    def generate_maze(self, timeout=0):
        self._remove_wall(0, 0, TOP)
        self._remove_wall(self.width - 1, self.height - 1, BOTTOM)
        current_cell = self.matrix[0][0]
        current_cell.visited = True

        stack = []

        while len(stack) != 0:
            if not current_cell.visited and self._check_if_neighbours_visited(current_cell):
                stack.append(current_cell)

                neighbours = self._get_unvisited_neighbours(current_cell)
                r = random.randrange(0, len(neighbours))

                self.remove_wall(current_cell, neighbours[r])

                current_cell = neighbours[r]
                current_cell.visited = True
            else:
                current_cell = stack.pop()

            time.sleep(timeout)

    def _fill_node(self, node) -> Node:
        for wall, i in enumerate(node.obj.walls):
            if not wall:
                node.set_node(self._fill_node(Node()))


    def to_tree(self) -> Tree:
        return
