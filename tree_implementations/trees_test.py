import unittest

from tree_implementations.tree import Tree
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

    def test_add_node(self):
        right = Node(4, None, None)
        left_2 = Node(10, None, None)
        left = Node(3, left_2, None)
        node = Node(2, left, right)
        array_tree = ArrayTree(1)
        dict_tree = DictTree(0, None, None)
        classic_tree = ClassicTree(node)
        array_tree.add_node(2, 4)
        array_tree.add_node(3, 10)
        self.assertEqual(array_tree.array_tree, [None, 1, 4, 10])
        self.assertEqual(dict_tree.tree_dict, {0: {None: {}}})
        self.assertEqual(classic_tree.in_order_visit(node), None)