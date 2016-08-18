from classic_tree import ClassicTree,Node

# non capisco perche svuota la queue
def trasversal(tree, queue):
    if tree.left is not None and tree.right is not None:
        queue.append(tree.left)
        queue.append(tree.right)
        print tree.value
    if queue:
        trasversal(queue.pop(), queue)


if __name__ == '__main__':
    array = []
    node = Node(None, None, None)
    classic_tree = ClassicTree(node)
    classic_tree.value = 3
    classic_tree.left = Node(5, Node(1, None, None), Node(4, None, None))
    classic_tree.right = Node(2, Node(6, None, None), None)
    print trasversal(classic_tree, array)