import numpy
from stl import mesh
from laby import *
import pickle

load = open('matrix.json', "rb")
data = pickle.load(load)

width = data.width + 1      # base_plate
height = data.height + 1    # base_plate

base_plate_height = 1
z = 0                       # axis parameter
h = 1                       # wall height

vertices = numpy.array([                                    #  base_plate: vertices
    [0, 0, 0],
    [int(width) -1, 0, 0],
    [0, int(height - 1), 0],
    [int(width) - 1, int(height) -1, 0],
    [0, 0, base_plate_height],
    [int(width) - 1, 0, base_plate_height],
    [0, int(height - 1), base_plate_height],
    [int(width) - 1, int(height) - 1, base_plate_height]
    ])

faces = numpy.array([                                      #  base_plate: Faces
    [0, 1, 2],
    [1, 2, 3],
    [4, 5, 6],
    [5, 6, 7],
    [0, 4, 2],
    [4, 2, 6],
    [1, 0, 4],
    [4, 5, 1],
    [1, 3, 5],
    [3, 7, 5],
    [2, 6, 3],
    [7, 3, 6]
    ])

for x in range(len(data.matrix)):
    for y in range(len(data.matrix[x])):

        if data.matrix[x][y].walls[TOP]:                                                        # TOP WALLS
            lengh  = len(vertices)
            vertices = numpy.append(vertices, [[x, y, base_plate_height]], axis = z)
            vertices = numpy.append(vertices, [[x+1, y, base_plate_height]], axis = z)
            vertices = numpy.append(vertices, [[x, y, base_plate_height + h]], axis = z)
            vertices = numpy.append(vertices, [[x + 1, y, base_plate_height + h]], axis = z)

            faces = numpy.append(faces, [[1 + lengh, 2 + lengh, lengh]], axis = z)
            faces = numpy.append(faces, [[3 + lengh, 2 + lengh, 1+ lengh]], axis = z)

        if data.matrix[x][y].walls[BOTTOM]:                                                     # BOTTOM
            lengh  = len(vertices)
            vertices = numpy.append(vertices, [[x, y + 1, base_plate_height]], axis = z)
            vertices = numpy.append(vertices, [[x+1, y + 1, base_plate_height]], axis = z)
            vertices = numpy.append(vertices, [[x, y + 1 , base_plate_height + h]], axis = z)
            vertices = numpy.append(vertices, [[x + 1, y +1 , base_plate_height + h]], axis = z)

            faces = numpy.append(faces, [[1 + lengh, 2 + lengh, lengh]], axis = z)
            faces = numpy.append(faces, [[3 + lengh, 2 + lengh, 1+ lengh]], axis = z)

        if data.matrix[x][y].walls[LEFT]:                                                        # LEFT
            lengh  = len(vertices)
            vertices = numpy.append(vertices, [[x, y, base_plate_height]], axis = z)
            vertices = numpy.append(vertices, [[x, y + 1, base_plate_height]], axis = z)
            vertices = numpy.append(vertices, [[x, y, base_plate_height + h]], axis = z)
            vertices = numpy.append(vertices, [[x, y +1 , base_plate_height + h]], axis = z)

            faces = numpy.append(faces, [[1 + lengh, 2 + lengh, lengh]], axis = z)
            faces = numpy.append(faces, [[3 + lengh, 2 + lengh, 1+ lengh]], axis = z)

        if data.matrix[x][y].walls[RIGHT]:                                                      # RIGHT
            lengh  = len(vertices)
            vertices = numpy.append(vertices, [[x + 1, y, base_plate_height]], axis = z)
            vertices = numpy.append(vertices, [[x + 1, y + 1, base_plate_height]], axis = z)
            vertices = numpy.append(vertices, [[x + 1, y, base_plate_height + h]], axis = z)
            vertices = numpy.append(vertices, [[x + 1, y +1 , base_plate_height + h]], axis = z)

            faces = numpy.append(faces, [[1 + lengh, 2 + lengh, lengh]], axis = z)
            faces = numpy.append(faces, [[3 + lengh, 2 + lengh, 1+ lengh]], axis = z)

print(vertices)
print(faces)

stl_object = mesh.Mesh(numpy.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))          
for i, f in enumerate(faces):
    for j in range(3):
        stl_object.vectors[i][j] = vertices[f[j],:]

stl_object.save('file.stl')
load.close()