import unittest
import random

from binary_search import BinarySearch

class BinarySearchTest(unittest.TestCase):

    def test_binary_search_empty_array(self):

        array = random.sample(range(1, 100), 0)
        binary = BinarySearch(array)
        self.assertIsNotNone(binary.array)
        self.assertEqual(len(binary.array), 0)
        binary.array.sort()
        self.assertEqual(binary.binary_search_algorithm(0, len(binary.array) - 1, 3), -1)

    def test_binary_search_one_element(self):

        array = [20]
        binary = BinarySearch(array)
        self.assertIsNotNone(binary.array)
        self.assertEqual(len(binary.array), 1)
        self.assertEqual(binary.binary_search_algorithm(0, len(binary.array) - 1, 20), 0)

    def test_binary_search_even_number_elements(self):

        array = [20, 30, 40, 50]
        binary = BinarySearch(array)
        self.assertIsNotNone(binary.array)
        self.assertEqual(len(binary.array), 4)
        self.assertEqual(binary.binary_search_algorithm(0, len(binary.array) - 1, 40), 2)

    def test_binary_search_odd_number_elements(self):

        array = [20, 30, 40, 50, 99]
        binary = BinarySearch(array)
        self.assertIsNotNone(binary.array)
        self.assertEqual(len(binary.array), 5)
        self.assertEqual(binary.binary_search_algorithm(0, len(binary.array) - 1, 99), 4)