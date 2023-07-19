import time

import game, laby, threading, pickle

l = laby.Labyrinth(12, 12)

def gen_maze(name):
    time.sleep(1)
    l.generate_maze(0.005)

if __name__ == '__main__':
    #l.remove_wall(l.matrix[0][0], l.matrix[1][0])
    #threading.Thread(target=gen_maze, args=(1,)).start()
    l.generate_maze()

    with open("matrix.json", "wb") as f:
        pickle.dump(l, f)

    # Get the descendants of the node
    descendants = l.tree.children(f"{l.width - 1},{l.height - 1}")

    # Delete the descendants
    for descendant in descendants:
        l.tree.remove_subtree(descendant.identifier)

    with open("tree.txt", "w") as f:
        f.write(l.tree.show(stdout=False))

    g = game.Game(l)
    g.show()
