from tree_implementations.tree import Tree


class DictTree(Tree):
    def __init__(self):
        super(DictTree, self).__init__()
        self.root = {}