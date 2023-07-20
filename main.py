import time

import game, laby, threading, pickle, grade

l = laby.Labyrinth(6, 6)

def show_maze():
    g = game.Game(l)
    g.show()

if __name__ == '__main__':
    search_and_grade = grade.Maze_Search(10, 5)

    best_fit, best_grade = search_and_grade.search_for_maze(0, n=1000)

    # with open("matrix.json", "wb") as f:
    #     pickle.dump(l, f)
    #

    l = best_fit

    with open("tree.txt", "w", encoding="utf-8") as f:
        f.write(l.tree.show(stdout=False))

    threading.Thread(target=show_maze).start()

    #l.generate_maze(1)

