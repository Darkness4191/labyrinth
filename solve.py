import math
from queue import PriorityQueue
from laby import Labyrinth

class AStarSolver:
    OPENLIST_COLOR = (0, 0, 150)
    CLOSEDLIST_COLOR = (80, 0, 100)

    def __init__(self, labyrinth):
        self.labyrinth : Labyrinth = labyrinth

    def _expand_node(self, current_node):
        for node in self.labyrinth.tree.children(f"{current_node.x},{current_node.y}"):
            if not self.closedlist.__contains__(node.data):
                continue

            tentative_g = math.sqrt(node.data.x**2 + node.data.y**2)



    def solve(self):
        self.openlist = PriorityQueue()
        self.closedlist = set()

        self.openlist.put((0, self.labyrinth.matrix[0][0]))
        self.labyrinth.matrix[0][0].color = self.OPENLIST_COLOR

        while not self.openlist.empty():
            current_node = self.openlist.get()

            if current_node[1] == self.labyrinth.matrix[self.labyrinth.width - 1][self.labyrinth.height - 1]:
                return True

            self.closedlist.add(current_node[1])
            self._expand_node(current_node[1])

        return False


