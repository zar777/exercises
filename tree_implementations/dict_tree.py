from tree_implementations.tree import Tree


class DictTree(Tree):
    def __init__(self, root_value, left, right):
        super(DictTree, self).__init__()
        self.tree_dict = {root_value: {left: {}, right: {}}}

    def add_node(self):
        self.tree_dict[].values().