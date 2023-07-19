from laby import *

EASY = 0
MEDIUM = 1
HARD = 2
VERY_HARD = 3

HARDEST_LENGTH_PERCENT = 0.6

# 1: Gesamt Länge (abs(--)) * Abzweigungen (n: Länge / Länge zum Startpunkt)
# 2: Abzweigungen
#    - Länge / Länge zum Startpunkt

class Search:
    def __init__(self, difficulty):
        self.difficulty

    def _shortest_path_to_start(self, point):

    def search_for_maze(self, width, height, n=50):
        self.labyrinth = Labyrinth(width, height)

        best = self.labyrinth.generate_maze()
        best_diff = self.grade(best)

        for i in range(n):
            self.labyrinth.clear_maze()

            new_laby = self.labyrinth.generate_maze()
            new_diff = self.grade(new_laby)

            if abs(new_diff - self.difficulty) < abs(best_diff - self.difficulty):
                best = new_laby
                best_diff = new_diff

    def grade(self, labyrinth : Labyrinth):
        whole_length = 0# last -> parent -> parent -> ... -> start (n)

        min_length = labyrinth.height + (labyrinth.width - 1)
        max_length = labyrinth.width * labyrinth.height
        hardest_length = HARDEST_LENGTH_PERCENT * max_length

        length_grade = abs(hardest_length - whole_length)

        junction_count = 0# loop tree -> search for more than one children

        junction_grade = 0 #[] ++ loop junctions -> length / length to start
