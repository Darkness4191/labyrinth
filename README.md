# Labyrinth Project

### Quickstart
1. Create a new empty labyrinth with `laby = Labyrinth(width, height)`
2. Auto-generate a maze with `laby.generate_maze()`
3. Create a new Pygame screen to visualize the maze with `game = Game(laby)`
4. Then open maze with `game.show()`

### Animation
You can also watch the generation in real-time by first creating the game window on a different thread 
and then starting the maze generation with a timeout via `laby.generate_maze(timeout)`

### Tree generation and grading
While generating a maze the labyrinth keeps track of tree in `laby.tree`. Note that this tree
can reach beyond the end point. With the Class `Maze_Search` you can now grade a specific labyrinth object
but also generate a number of mazes to automatically pick the closest one to a given difficulty ranging 
from 0 to 1 [[example]](https://github.com/Darkness4191/labyrinth/blob/27b61ec91c76de03d71c1f52ad869c5bb8d9d686/main.py#L14).

### Generation of 3D Objects
By exporting a labyrinth object with pickle as it is done in the [main.py file](https://github.com/Darkness4191/labyrinth/blob/27b61ec91c76de03d71c1f52ad869c5bb8d9d686/main.py#L21)
you can [import it](https://github.com/Darkness4191/labyrinth/blob/27b61ec91c76de03d71c1f52ad869c5bb8d9d686/3d_builder.py#L6) in the 3d_builder.py file and generate a stl 3d object. 