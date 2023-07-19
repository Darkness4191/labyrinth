from laby import *

EASY = 0
MEDIUM = 1
HARD = 2
VERY_HARD = 3

class Search:
    def __init__(self, difficulty):
        self.difficulty

    def search_for_maze(self, width, height, n=50):
        self.labyrinth = Labyrinth(width, height)

        best = self.labyrinth.generate_maze()

        for i in range(n):
            pass


    def grade(self, labyrinth):
