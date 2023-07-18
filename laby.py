from enum import Enum
import json, random, time

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

    def _remove_wall(self, x, y, direc):
        val = direc.value
        self.matrix[x][y].walls[val] = False

        changed = False

        if val % 2 == 0:
            val += 1
        else:
            val -= 1

        if val >= 2:
            if val == Direction.LEFT.value and x < (self.width - 1):
                self.matrix[x + 1][y].walls[val] = False
            elif x > 0:
                self.matrix[x - 1][y].walls[val] = False
        elif val <= 1:
            if val == Direction.TOP.value and y < (self.height - 1):
                self.matrix[x][y + 1].walls[val] = False
            elif y > 0:
                self.matrix[x][y - 1].walls[val] = False

        if changed:
            self.matrix[x][y].walls[val] = False

    def remove_wall(self, cell1 : Cell, cell2 : Cell):
        dx = cell2.x - cell1.x
        dy = cell2.y - cell1.y

        if abs(dx) > 1 or abs(dy) > 1:
            raise RuntimeError(f"dx or dy can't be higher than 1 in remove_wall")

        if dy > 0 and dx == 0:
            self._remove_wall(cell2.x, cell2.y, Direction.TOP)
        elif dy < 0 and dx == 0:
            self._remove_wall(cell2.x, cell2.y, Direction.BOTTOM)
        elif dx > 0 and dy == 0:
            self._remove_wall(cell2.x, cell2.y, Direction.LEFT)
        elif dx < 0 and dy == 0:
            self._remove_wall(cell2.x, cell2.y, Direction.RIGHT)

    def clear_maze(self):
        self.matrix = []

        for i in range(self.width):
            sub = []
            for j in range(self.height):
                sub.append(Cell(i, j))
            self.matrix.append(sub)

    def generate_maze(self, timeout=0):
        self._remove_wall(0, 0, Direction.TOP)
        self._remove_wall(self.width - 1, self.height - 1, Direction.BOTTOM)
        current_cell = self.matrix[0][0]
        current_cell.visited = True

        stack = []

        while not self._board_is_visited():
            if self._check_if_neighbours_visited(current_cell):
                stack.append(current_cell)

                neighbours = self._get_unvisited_neighbours(current_cell)
                r = random.randrange(0, len(neighbours))

                if abs(current_cell.x - neighbours[r].x) <= 1 and abs(current_cell.y - neighbours[r].y) <= 1:
                    self.remove_wall(current_cell, neighbours[r])

                current_cell = neighbours[r]
                current_cell.visited = True
            elif not (len(stack) == 0):
                current_cell = stack.pop()

            time.sleep(timeout)











