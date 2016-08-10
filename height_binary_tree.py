import math
from tree_implementations import classic_tree


def pre_order_visit(tree_object, root, count):
    if root is None:
        return []
    return [root.value + pre_order_visit(tree, root.left, count) + pre_order_visit(tree, root.left, count)]


def height(tree):
    count = 0
    return math.ceil(math.sqrt(len(pre_order_visit(tree, tree.root, count))))


if __name__ == '__main__':
    right = Node(4, None, None)
    left_2 = Node(10, None, None)
    left = Node(3, left_2, None)
    node = Node(2, left, right)
    classic_tree = ClassicTree(node)
    classic_tree.in_order_visit(node)
