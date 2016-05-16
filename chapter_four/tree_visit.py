def pre_order_visit(tree, n):
    if tree[n] is None:
        return
    print tree[n]
    value = n * 2
    if value < len(tree):
        pre_order_visit(tree, value)
        pre_order_visit(tree, value + 1)


def in_order_visit(tree, n):
    if tree[n] is None:
        return
    value = n * 2
    if value < len(tree):
        in_order_visit(tree, value)
    print tree[n]
    if value < len(tree):
        in_order_visit(tree, value + 1)


def post_order_visit(tree, n):
    if tree[n] is None:
        return
    value = n * 2
    if value < len(tree):
        post_order_visit(tree, value)
        post_order_visit(tree, value + 1)
    print tree[n]


if __name__ == '__main__':
    tree = [0, 1, 3, 7, 2, 4, 5, 6]
    # print tree[n * 2: len(tree)+1]
    # print pre_order_visit(tree, 1)
    # print in_order_visit(tree, 1)
    print post_order_visit(tree, 1)
