class Node:
    def __init__(self, obj):
        self.obj = obj
        self.nodes = {}

    def set_node(self, node, direc):
        self.nodes[direc] = node

class Tree(Node):
    def __init__(self, root):
        Node.__init__(root)