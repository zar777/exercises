import unittest

from tree_implementations.array_tree import ArrayTree
from tree_implementations.dict_tree import DictTree
from tree_implementations.classic_tree import ClassicTree, Node


class TreesTest(unittest.TestCase):

    def test_empty_tree(self):
        node = Node(None, None, None)
        array_tree = ArrayTree(1)
        dict_tree = DictTree(0, None, None)
        classic_tree = ClassicTree(node)
        self.assertEqual(array_tree.array_tree, [None, 1])
        self.assertEqual(dict_tree.tree_dict, {0: {None: {}}})
        self.assertEqual(classic_tree.in_order_visit(node), None)

    def test_add_node_array_tree(self):
        array_tree = ArrayTree(1)
        array_tree.add_node(2, 4)
        array_tree.add_node(3, 10)
        self.assertEqual(array_tree.array_tree, [None, 1, 4, 10])

    def test_add_node_classic_tree(self):
        array = []
        node = Node(None, None, None)
        classic_tree = ClassicTree(node)
        classic_tree.value = 5
        classic_tree.left = Node(3, Node(6, None, None), Node(7, None, None))
        classic_tree.right = Node(12, Node(15, None, None), Node(18, None, None))
        classic_tree.left.left.right = Node(9, None, None)
        classic_tree.in_order_visit(classic_tree, array)
        self.assertEqual(array, [6, 9, 3, 7, 5, 15, 12, 18])

    def test_add_node_dict_tree(self):
        dict_tree = DictTree(0, None, None)
        dict_tree['left'] = 5
        dict_left = {3: {}}
        self.assertEqual(dict_tree.tree_dict, "")