from tree import Tree


class ClassicTree(Tree):
    def __init__(self, root_node):
        super(ClassicTree, self).__init__()
        self.root = root_node

    def in_order_visit(self, tree, result):
        if tree.value is None:
            pass
        if tree.left is not None:
            self.in_order_visit(tree.left, result)
        result.append(tree.value)
        if tree.right is not None:
            self.in_order_visit(tree.right, result)


class Node(object):
    def __init__(self, value, left, right):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return self.value

if __name__ == '__main__':
    array = []
    node = Node(None, None, None)
    classic_tree = ClassicTree(node)
    classic_tree.value = 3
    classic_tree.left = Node(5, Node(1, None, None), Node(4, None, None))
    classic_tree.right = Node(2, Node(6, None, None), None)
