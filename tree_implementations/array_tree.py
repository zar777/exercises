from tree_implementations.tree import Tree


class ArrayTree(Tree):
    def __init__(self, root_value):
        super(ArrayTree, self).__init__()
        self.array_tree = [None, root_value]

    def add_node(self, i, x):
        self.array_tree.insert(i, x)
