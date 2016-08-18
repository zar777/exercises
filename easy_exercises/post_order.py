s = ""


def postOrder(root):
    s += root.data
    if root.left is not None:
        postOrder(root.left)
    if root.right is not None:
        postOrder(root.right)
    print root.data