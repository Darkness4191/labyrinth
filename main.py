import time

import game, laby, json, threading, pickle

l = laby.Labyrinth(30, 30)

def gen_maze(name):
    time.sleep(1)
    l.generate_maze(0.005)

if __name__ == '__main__':
    #l.remove_wall(l.matrix[0][0], l.matrix[1][0])
    #threading.Thread(target=gen_maze, args=(1,)).start()
    l.generate_maze()

    with open("matrix.json", "wb") as f:
        pickle.dump(l, f)

    g = game.Game(l)
    g.show()
