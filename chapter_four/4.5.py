"""Write an algorithm to find the ‘next’ node (i.e., in-order successor) of a given node in
a binary search tree where each node has a link to its parent.
non ho sviluppato la soluzione corretta ho completamente sbagliato a capire il testo e tutt'ora non l'ho capito"""

def in_order_method(tree, root, list_result):
    if tree[root] is None:
        return
    value = root * 2
    if value < len(tree):
        in_order_method(tree, value, list_result)
    list_result.append(tree[root])
    if value < len(tree):
        in_order_method(tree, value + 1, list_result)


def find_next(list_result, tree, root, element_finder):
    in_order_method(tree, root, list_result)
    next_element = None
    if list_result.index(element_finder) < len(list_result)-1:
       next_element = list_result[list_result.index(element_finder) + 1]
    elif list_result.index(element_finder) == len(list_result)-1:
        return next_element
    return next_element

if __name__ == '__main__':
    tree = [0, 3, 2, 7, 1, 4, 6, 8]
    result_array = []
    # in_order_method(tree, 1, result_array)
    print result_array
    print find_next(result_array, tree, 1, 4)
    print result_array