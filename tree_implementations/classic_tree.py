from tree_implementations.tree import Tree


class ClassicTree(Tree):
    def __init__(self, root_node):
        super(ClassicTree, self).__init__()
        self.root = root_node

    def in_order_visit(self, node):
        if node is None:
            pass
        if node.left is not None:
            self.in_order_visit(node.left)
        print node.value
        if node.right is not None:
            self.in_order_visit(node.right)


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