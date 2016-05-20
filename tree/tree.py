"""Tree rapresentation"""
class Tree(object):
    def __init__(self, root_tree, tree_left, tree_right):
        self.root = root_tree
        self.child_left = tree_left
        self.child_right = tree_right


    def __str__(self):
        str(self.child_left) + " <--- " + str(self.root) + " ---> " + str(self.child_right)

class Vertex(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        str(self.value)

if __name__ == '__main__':
    root = Vertex()
    tree = Tree()

