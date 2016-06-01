from tree_implementations.tree import Tree


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
    right = Node(4, None, None)
    left_2 = Node(10, None, None)
    left = Node(3, left_2, None)
    node = Node(2, left, right)
    classic_tree = ClassicTree(node)
    classic_tree.in_order_visit(node)