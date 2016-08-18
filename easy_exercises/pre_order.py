s = []
def preOrder(root):
    s.append(root.data)
    if root.left is not None:
        preOrder(root.left)
    if root.right is not None:
        preOrder(root.right)
    if root.right is None and root.left is None:
        print " ".join(str(x) for x in s)

# come faccio a stampare tutto su un'unica linea?
print " ".join(str(x) for x in s)