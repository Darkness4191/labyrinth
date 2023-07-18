import time

import game, laby, json, threading

l = laby.Labyrinth(15, 15)

def gen_maze(name):
    time.sleep(1)
    l.generate_maze(0.0001)

if __name__ == '__main__':
    #l.remove_wall(l.matrix[0][0], l.matrix[1][0])
    threading.Thread(target=gen_maze, args=(1,)).start()
    #l.generate_maze()

    # with open("matrix.json", "w") as f:
    #     f.write(json.dumps(l, indent=4, default=vars))

    g = game.Game(l)
    g.show()
