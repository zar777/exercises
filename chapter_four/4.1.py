def balanced(tree, root):
    child = young_child(root)
    lenght_last = len(tree)
    counter = 0
    if child >= lenght_last:
        """confronto tra la somma del numero di nodi del sotto albero di destra  e sinistra
        se il numero di nodi differisce per uno --> ritorna true altrimenti false"""

    for pointer in xrange(0, 2):
        app_child = child + pointer
        if app_child < len(tree) and tree[app_child] != "":
            """volevo contare il numero di nodi nel branch di sinistra e destra ricorsivamente"""
            counter += 1
    balanced(tree, child)
    balanced(tree, child +1)

def young_child(parent):
    """this method is created to return the first child, given his parent"""
    return 2 * parent


"""fallito"""