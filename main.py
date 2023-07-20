import time

import game, laby, threading, pickle, grade

l = laby.Labyrinth(10, 5)

def show_maze():
    g = game.Game(l)
    g.show()

if __name__ == '__main__':
    search_and_grade = grade.Maze_Search(10, 5)

    best_fit, best_grade = search_and_grade.search_for_maze(1, n=1000)

    l = best_fit

    threading.Thread(target=show_maze).start()

    with open("matrix.json", "wb") as f:
        pickle.dump(l, f)

    # with open("tree.txt", "w", encoding="utf-8") as f:
    #     f.write(l.tree.show(stdout=False))

