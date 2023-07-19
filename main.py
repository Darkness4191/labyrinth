import time

import game, laby, threading, pickle, grade

l = laby.Labyrinth(5, 5)

def gen_maze():
    time.sleep(1)
    l.generate_maze(0.005)

def show_maze():
    g = game.Game(l)
    g.show()

if __name__ == '__main__':
    #l.remove_wall(l.matrix[0][0], l.matrix[1][0])
    #threading.Thread(target=gen_maze).start()
    search_and_grade = grade.Search()

    mazes = {}

    for i in range(1000):
        maze = laby.Labyrinth(5, 5)
        maze.generate_maze()

        g = search_and_grade.grade(maze)

        mazes[g] = maze

        print(g)

    sorted_keys = sorted(mazes)
    print(mazes)

    # with open("matrix.json", "wb") as f:
    #     pickle.dump(l, f)
    #
    # # Get the descendants of the node
    # descendants = l.tree.children(f"{l.width - 1},{l.height - 1}")
    #
    # # Delete the descendants
    # for descendant in descendants:
    #     l.tree.remove_subtree(descendant.identifier)
    #
    # with open("tree.txt", "w") as f:
    #     f.write(l.tree.show(stdout=False))

    threading.Thread(target=show_maze).start()

    # for i, key in enumerate(sorted_keys):
    #     new_maze = mazes[key]
    #     l.matrix = new_maze.matrix
    #     print(i)
    #
    #     time.sleep(0.5)

    while True:
        new_maze = mazes[sorted_keys[0]]
        l.matrix = new_maze.matrix

        time.sleep(1)

        new_maze = mazes[sorted_keys[len(sorted_keys) - 1]]
        l.matrix = new_maze.matrix

        time.sleep(1)
