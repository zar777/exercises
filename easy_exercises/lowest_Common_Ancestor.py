from classic_tree import ClassicTree, Node


# the lowest common ancestor is the element between the v1 and v2 value number GENIALE
def lowest_ancestor(root, v1, v2):
    if root.value > v1 and root.value > v2:
        return lowest_ancestor(root.left, v1, v2)
    if root.value < v1 and root.value < v2:
        return lowest_ancestor(root.right, v1, v2)
    return root.value

if __name__ == '__main__':
    node = Node(None, None, None)
    classic_tree = ClassicTree(node)
    classic_tree.value = 4
    classic_tree.left = Node(2, Node(1, None, None), Node(3, None, None))
    classic_tree.right = Node(7, None, None)
    print lowest_ancestor(classic_tree, 1, 3)