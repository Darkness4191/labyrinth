from enum import Enum
from treelib import Node, Tree
import random, time

TOP = (0, -1)
BOTTOM = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.walls = {(1, 0): True,
                      (-1, 0): True,
                      (0, 1): True,
                      (0, -1): True,}

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

    def _get_next_cell(self, cell, direc):
        cell2_x = cell.x + direc[0]
        cell2_y = cell.y + direc[1]

        if cell2_x >= 0 and cell2_x < self.width and cell2_y >= 0 and cell2_y < self.height:
            return self.matrix[cell2_x][cell2_y]
        else:
            return None

    def _remove_wall(self, x, y, direc : (int, int)):
        cell = self.matrix[x][y]
        cell2 = self._get_next_cell(cell, direc)

        cell.walls[direc] = False

        if cell2 != None:
            cell2.walls[tuple(i * (-1) for i in direc)] = False

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

        self.tree = Tree()
        self.tree.create_node(tag=f"{current_cell.x},{current_cell.y}",
                              identifier=f"{current_cell.x},{current_cell.y}",
                              data=current_cell) # root node

        stack = []
        first = True

        while len(stack) != 0 or first:
            neighbours = self._get_unvisited_neighbours(current_cell)

            if len(neighbours) > 0:
                stack.append(current_cell)

                r = random.randrange(0, len(neighbours))

                self.remove_wall(current_cell, neighbours[r])

                self.tree.create_node(tag=f"{neighbours[r].x},{neighbours[r].y}",
                                      identifier=f"{neighbours[r].x},{neighbours[r].y}",
                                      parent=f"{current_cell.x},{current_cell.y}",
                                      data=current_cell)

                current_cell = neighbours[r]
                current_cell.visited = True
            else:
                current_cell = stack.pop()

            first = False

            if timeout > 0:
                time.sleep(timeout)
