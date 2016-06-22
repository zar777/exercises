"""
Given a Binary Search tree of integers, return the number of nodes having values between two given integers.
 You can assume that you already have some extra information at each node
(number of children in left and right subtrees).
"""


def in_order_visit(tree, array, root):

    if root >= len(tree):
        pass
    mid = root * 2
    in_order_visit(tree, array, mid)
    array.append(tree[mid])
    in_order_visit(tree, array, mid+1)


def between_two_int(first, second):
    pass


if __name__ == '__main__':
    pass