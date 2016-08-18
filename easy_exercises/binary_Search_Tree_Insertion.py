from classic_tree import ClassicTree, Node


def insertion_bst(root, value, array):
    if root is None:
        node = Node(value, None, None)
        root = node
        array.append(root.value)
    elif value > root.value:
        array.append(root.value)
        insertion_bst(root.right, value, array)
    else:
        array.append(root.value)
        insertion_bst(root.left, value, array)
    return array

if __name__ == '__main__':
    node = Node(None, None, None)
    classic_tree = ClassicTree(node)
    classic_tree.value = 4
    classic_tree.left = Node(2, Node(1, None, None), Node(3, None, None))
    classic_tree.right = Node(7, None, None)
    array = []
    print insertion_bst(classic_tree, 6, array)