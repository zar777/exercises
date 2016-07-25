import unittest
import random

from all_binary_search import binary_iter_multi, binary_iter_multi, binary_iter_multi, binary_iter_multi


class BinarySearchTest(unittest.TestCase):

    def test_binary_search_empty_array(self):
        array = random.sample(range(1, 100), 0)
        self.assertIsNotNone(array)
        self.assertEqual(len(array), 0)
        array.sort()
        self.assertEqual(binary_iter_multi.binary_iter_multi(0, 0, 1, array), -1)

    def test_binary_search_one_element(self):
        array = [20]
        self.assertIsNotNone(array)
        self.assertEqual(len(array), 1)
        array.sort()
        self.assertEqual(binary_iter_multi.binary_iter_multi(20, 0, 1, array), 0)

    def test_binary_search_even_number_elements(self):
        array = [20, 30, 40, 50]
        self.assertIsNotNone(array)
        self.assertEqual(len(array), 4)
        array.sort()
        self.assertEqual(binary_iter_multi.binary_iter_multi(30, 0, 1, array), 1)

    def test_binary_search_odd_number_elements(self):
        array = [20, 30, 40, 50, 99, 100]
        self.assertIsNotNone(array)
        self.assertEqual(len(array), 6)
        array.sort()
        self.assertEqual(binary_iter_multi.binary_iter_multi(100, 0, 1, array), 5)

    def test_binary_search_no_element_middle(self):
        array = [20, 30, 40, 50, 99, 100]
        self.assertIsNotNone(array)
        self.assertEqual(len(array), 6)
        array.sort()
        self.assertEqual(binary_iter_multi.binary_iter_multi(25, 0, 1, array), -1)

    def test_binary_search_no_element_end(self):
        array = [20, 30, 40, 50, 99, 100]
        self.assertIsNotNone(array)
        self.assertEqual(len(array), 6)
        array.sort()
        self.assertEqual(binary_iter_multi.binary_iter_multi(110, 0, 1, array), -1)
