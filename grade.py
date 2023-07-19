from laby import *
import copy

EASY = 0
MEDIUM = 1
HARD = 2
VERY_HARD = 3

HARDEST_LENGTH_PERCENT = 0.6
LENGTH_COEFFICIENT = 3

# 1: Gesamt Länge (abs(--)) * Abzweigungen (n: Länge / Länge zum Startpunkt)
# 2: Abzweigungen
#    - Länge / Länge zum Startpunkt

class Search:
    def __init__(self, difficulty=MEDIUM):
        self.difficulty = difficulty

    # def _get_leafs(self, tree, node):
    #     leafs = []
    #     current_node = node
    #     stack = []
    #
    #     while len(stack) != 0 or not tree.is_leaf(current_node.identifier):
    #         if tree.is_leaf(current_node.identifier):
    #             leafs.append(current_node)
    #             current_node = stack.pop()
    #         elif len(tree.children(current_node)) > 1:
    #             for i, node in enumerate(len(tree.children(current_node)), start=1):
    #                 stack.append(node)
    #
    #         current_node = tree.children(current_node)[0]


    def _shortest_path_to_start(self, tree, node) -> int:
        return tree.depth(node)

    def search_for_maze(self, width, height, n=50):
        labyrinth = Labyrinth(width, height)

        best = labyrinth.generate_maze()
        best_diff = self.grade(best)

        for i in range(n):
            labyrinth.clear_maze()

            new_laby = labyrinth.generate_maze()
            new_diff = self.grade(new_laby)

            if abs(new_diff - self.difficulty) < abs(best_diff - self.difficulty):
                best = new_laby
                best_diff = new_diff

    def grade(self, labyrinth : Labyrinth):
        if labyrinth.tree == None or len(labyrinth.tree.all_nodes()) == 0:
            raise RuntimeError("Cannot grade an empty maze!")

        tree = copy.deepcopy(labyrinth.tree)

        end_node = tree.get_node(f"{labyrinth.width - 1},{labyrinth.height - 1}")
        start_node = tree.get_node(f"0,0")

        whole_length = self._shortest_path_to_start(tree, end_node)

        min_length = labyrinth.height + (labyrinth.width - 1)
        max_length = labyrinth.width * labyrinth.height
        hardest_length = HARDEST_LENGTH_PERCENT * max_length

        length_grade = abs(hardest_length - whole_length)

        junction_grade = 0 #[] ++ loop junctions -> length / length to start

        leafs = tree.leaves()

        for leaf in leafs:
            junction_grade += abs(whole_length - self._shortest_path_to_start(tree, leaf))

        return length_grade * LENGTH_COEFFICIENT + junction_grade

        # current_node = start_node

        # junctions = []
        # for node in tree.all_nodes():
        #     if len(tree.children(node.identifier)) > 1:
        #         junctions.append(node)
        #
        # for t in junctions:
        #     leafs = self._get_leafs(t)


        # current_node = end_node
        # visited_branches = []
        #
        # while current_node != start_node:
        #     if len(current_node.children) > 0:
        #         for c in current_node.children:
        #             if c not in visited_branches:
        #                 current_node = _get_leaf
        #
        #         junction_grade += -1 / self._shortest_path_to_start(tree, current_node)
        #     else:
        #         current_node = tree.parent(current_node)
