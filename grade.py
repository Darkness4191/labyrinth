from laby import *
import copy

EASY = 0
MEDIUM = 0.5
HARD = 1

HARDEST_LENGTH_PERCENT = 0.5
LENGTH_COEFFICIENT = 50 # 0.0001
FACTOR = 1

class Maze_Search:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def _shortest_path_to_start(self, tree, node) -> int:
        return tree.depth(node)

    def _distance_to_next_junction(self, tree, leaf):
        current_node = leaf
        while current_node != None and len(tree.children(current_node.identifier)) <= 1:
            current_node = tree.parent(current_node.identifier)
        return abs(self._shortest_path_to_start(tree, leaf) - self._shortest_path_to_start(tree, current_node))

    def search_for_maze(self, difficulty, n=1000):
        mazes = {}

        for i in range(n):
            labyrinth = Labyrinth(self.width, self.height)
            labyrinth.generate_maze()

            mazes[self.grade(labyrinth)] = labyrinth

        sorted_keys = sorted(mazes)

        best_fit = mazes[sorted_keys[0]]
        best_grade = sorted_keys[0]
        for k in mazes:
            if abs(k / sorted_keys[len(sorted_keys) - 1] - difficulty) < abs(best_grade / sorted_keys[len(sorted_keys) - 1] - difficulty):
                best_fit = mazes[k]
                best_grade = k

        return best_fit, best_grade


    def grade(self, labyrinth : Labyrinth):
        if labyrinth.tree == None or len(labyrinth.tree.all_nodes()) == 0:
            raise RuntimeError("Cannot grade an empty maze!")

        tree = copy.deepcopy(labyrinth.tree)

        end_node = tree.get_node(f"{labyrinth.width - 1},{labyrinth.height - 1}")
        start_node = tree.get_node(f"0,0")

        whole_length = self._shortest_path_to_start(tree, end_node)

        min_length = labyrinth.height + (labyrinth.width - 2)
        max_length = labyrinth.width * labyrinth.height
        hardest_length = HARDEST_LENGTH_PERCENT * abs(max_length - min_length) + min_length

        length_grade = 1 / abs(hardest_length - whole_length)
        junction_grade = 0

        leafs = tree.leaves()
        for leaf in leafs:
            if leaf != end_node:
                junction_grade += self._distance_to_next_junction(tree, leaf) / self._shortest_path_to_start(tree, leaf)

        final_grade = length_grade * LENGTH_COEFFICIENT + junction_grade

        return final_grade
