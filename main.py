import game, laby

if __name__ == '__main__':
    l = laby.Labyrinth(15, 15)
    l.remove_wall(0, 0, laby.Direction.TOP.value)
    l.remove_wall(7, 7, laby.Direction.BOTTOM.value)

    g = game.Game(l)
    g.show()
