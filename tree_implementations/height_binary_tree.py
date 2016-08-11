from tree_implementations.classic_tree import Node, ClassicTree


def pre_order_visit(tree, count, max_heigth):
        """height tree"""
        count += 1
        if tree.left is not None:
            return pre_order_visit(tree.left, count,max_heigth)
        if tree.right is not None:
            return pre_order_visit(tree.right, count, max_heigth)
        if count > max_heigth:
            max_heigth = count
        count -= 1
        return max_heigth


def height(tree):
    return pre_order_visit(tree, -1, 0)


if __name__ == '__main__':
    node = Node(None, None, None)
    classic_tree = ClassicTree(node)
    classic_tree.value = 5
    classic_tree.left = Node(3, Node(6, None, None), Node(7, None, None))
    classic_tree.right = Node(12, Node(15, None, None), Node(18, None, None))
    classic_tree.left.left.right = Node(9, None, None)
    print height(classic_tree)




# def pre_order_visit(tree_object, root, count, marked):
#         """depth first search algorithm"""
#         marked[root] = True
#         for adj in adj_list[root]:
#             if marked[adj] is not True:
#                 count +=1
#                pre_order_visit(adj)
#             if count > max_heigth:
#                 max_heigth
#         return max_heigth
