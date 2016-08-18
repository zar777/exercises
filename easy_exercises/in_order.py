s = ""

def inOrder(root):
    s += root.data
    if root.left is not None:
        inOrder(root.left)
    print root.data
    if root.right is not None:
        inOrder(root.right)
    print s