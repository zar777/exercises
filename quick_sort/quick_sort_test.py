import unittest
import random

from quick_sort import QuickSort


class MergeSortTest(unittest.TestCase):

    def test_merge_sort_empty_array(self):

        array = random.sample(range(1, 100), 0)
        array_duplicate = array[:]
        quick = QuickSort(array)
        self.assertIsNotNone(quick.array)
        self.assertEqual(len(quick.array), 0)
        array_duplicate.sort()
        quick.quick_sort_algorithm(0, len(quick.array) - 1)
        self.assertEqual(quick.array, array_duplicate)

    def test_merge_sort_one_element(self):

        array = random.sample(range(1, 100), 1)
        array_duplicate = array[:]
        quick = QuickSort(array)
        self.assertIsNotNone(quick.array)
        self.assertEqual(len(quick.array), 1)
        array_duplicate.sort()
        quick.quick_sort_algorithm(0, len(quick.array) - 1)
        self.assertEqual(quick.array, array_duplicate)

    def test_merge_sort_even_number_elements(self):

        array = random.sample(range(1, 100), 10)
        array_duplicate = array[:]
        quick = QuickSort(array)
        self.assertIsNotNone(quick.array)
        self.assertEqual(len(quick.array), 10)
        array_duplicate.sort()
        self.assertNotEqual(quick.array, array_duplicate)
        quick.quick_sort_algorithm(0, len(quick.array) - 1)
        self.assertEqual(quick.array, array_duplicate)

    def test_merge_odd_number_elements(self):

        array = random.sample(range(1, 100), 9)
        array_duplicate = array[:]
        quick = QuickSort(array)
        self.assertIsNotNone(quick.array)
        self.assertEqual(len(quick.array), 9)
        array_duplicate.sort()
        self.assertNotEqual(quick.array, array_duplicate)
        quick.quick_sort_algorithm(0, len(quick.array) - 1)
        self.assertEqual(quick.array, array_duplicate)
