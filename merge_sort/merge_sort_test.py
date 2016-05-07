import unittest
import random

from merge_sort import MergeSort


class MergeSortTest(unittest.TestCase):

    def test_merge_sort_empty_array(self):

        array = random.sample(range(1, 100), 0)
        array_duplicate = array[:]
        merge = MergeSort(array)
        self.assertIsNotNone(merge.array)
        self.assertEqual(len(merge.array), 0)
        array_duplicate.sort()
        merge.merge_sort_algorithm(0, len(merge.array) - 1)
        self.assertEqual(merge.array, array_duplicate)

    def test_merge_sort_one_element(self):
        array = random.sample(range(1, 100), 1)
        array_duplicate = array[:]
        merge = MergeSort(array)
        self.assertIsNotNone(merge.array)
        self.assertEqual(len(merge.array), 1)
        array_duplicate.sort()
        merge.merge_sort_algorithm(0, len(merge.array) - 1)
        self.assertEqual(merge.array, array_duplicate)

    def test_merge_sort_even_number_elements(self):
        array = random.sample(range(1, 100), 10)
        array_duplicate = array[:]
        merge = MergeSort(array)
        self.assertIsNotNone(merge.array)
        self.assertEqual(len(merge.array), 10)
        array_duplicate.sort()
        self.assertNotEqual(merge.array, array_duplicate)
        merge.merge_sort_algorithm(0, len(merge.array) - 1)
        self.assertEqual(merge.array, array_duplicate)

    def test_merge_odd_number_elements(self):
        array = random.sample(range(1, 100), 9)
        array_duplicate = array[:]
        merge = MergeSort(array)
        self.assertIsNotNone(merge.array)
        self.assertEqual(len(merge.array), 9)
        array_duplicate.sort()
        self.assertNotEqual(merge.array, array_duplicate)
        merge.merge_sort_algorithm(0, len(merge.array) - 1)
        self.assertEqual(merge.array, array_duplicate)
